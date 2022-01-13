#!/usr/bin/env python

import numpy as np
import argparse, sys

def open_log_file(file_name):
    """Takes in a log.txt file, returns the process_names and
    number of events after the final applied cut in list form.
    """
    final_cut_values_list = []
    with open(file_name, "r") as input_file:
        data_raw=input_file.readlines()
        #del data_raw[0]
        #del data_raw[0]
        #process_names.append(data_raw[0])
        for elem in data_raw[2::]:
            temp_var1 = elem.split("\\\\")
            cut_values = temp_var1[0]
            cut_values = cut_values.split(" & ")
            final_cut_values_list.append(cut_values)
       
    return   final_cut_values_list

def convert_files(input_file):
    total_Data = []
    for i, elem1 in enumerate(input_file):
        individual_data = []
        for j, elem2 in enumerate(elem1):
            if j == 0:
                continue
            tempvar_3 = elem2.split(" $\pm$ ")
            individual_data.append(tempvar_3[0])
        total_Data.append(individual_data)
    return total_Data
            
#            temp_var3.split

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", dest="input", nargs="+", help="The input file(s)")
args = parser.parse_args()


files = open_log_file(args.input[0])
names = files[0]
cut_names = []
del names[0]
del files[0] #get rid of process names
del files[len(files)-1] # gets rid of "\end{tabular}"
values = convert_files(files)

for i in files:
    cut_names.append(i[0])

Total_efficiencies = []
for i, elem in enumerate(values):
    individual_efficiencies = []
    if i == 0:
        Total_efficiencies.append([1] * len(elem))
        temp_efficiencies = elem
    else:
        for j, elem2 in enumerate(elem):
            individual_efficiencies.append(float(elem2)/float(temp_efficiencies[j]))
        temp_efficiencies = elem
        Total_efficiencies.append(individual_efficiencies)

processes_list = str(list(range(len(Total_efficiencies))))
cuts_list = str(list(range(len(Total_efficiencies[0]))))

#print(names)
#print(cut_names)

#print(processes_list)
#print(cuts_list)

source = """from ROOT import TCanvas, TPad, TH2F, TLatex, TStyle, gStyle
from array import array
import numpy as np

c1 = TCanvas("c1", "c1",1500,750)
gStyle.SetOptStat(0)\n"""

source += "processes_list="+processes_list+"\n"
source += "cuts_list="+cuts_list+"\n"

source += """Number_processes = len(processes_list)-1
Number_cuts = len(cuts_list)-1
Cuts = np.array(cuts_list, dtype='float64')
Processes = np.array(processes_list, dtype='float64')
    
bottom_left_pad = TPad("bottom_left_pad", "center_pad",0.0,0.0,0.95,0.95)
bottom_left_pad.SetLogz()
bottom_left_pad.Draw()
bottom_left_pad.SetLeftMargin(0.17)

# Create, fill and project a 2D histogram.
h1 = TH2F("h1","",Number_processes,Processes,Number_cuts,Cuts)\n"""


for i, elem1 in enumerate(Total_efficiencies):
    for j, elem2 in enumerate(elem1):
        source += "h1.SetBinContent("+str(j+1)+","+str(len(Total_efficiencies)-i)+","+str(elem2)+")\n"

source += """h1.GetZaxis().SetRangeUser(10e-4,1)
x = h1.GetXaxis()\n"""

source += "x.SetNdivisions("+str(2*len(names)+1)+")\n"

for i, elem1 in enumerate(names):
    source += "x.ChangeLabel("+str(2*i+1)+",0.,0.03,-1,-1,-1,\" \")\n"
    source += "x.ChangeLabel("+str(2*i+2)+",0.,0.03,-1,-1,-1,\""+elem1+"\")\n"
    if (i == len(names)-1):
        source += "x.ChangeLabel("+str(2*i+3)+",0.,0.03,-1,-1,-1,\" \")\n"

source += """x.SetTickLength(0)
x.SetLabelOffset(0.03)

y = h1.GetYaxis()\n
"""

source += "y.SetNdivisions("+str(2*len(cut_names)+1)+")\n"

for i, elem1 in enumerate(cut_names):
    source += "y.ChangeLabel("+str(2*len(cut_names)-(2*i)+1)+",0.,0.03,-1,-1,-1,\" \")\n"
    source += "y.ChangeLabel("+str(2*len(cut_names)-(2*i))+",0.,0.03,-1,-1,-1,\""+elem1+"\")\n"
    if (i == len(cut_names)-1):
        source += "y.ChangeLabel("+str(2*len(cut_names)-(2*i)-1)+",0.,0.03,-1,-1,-1,\" \")\n"

source += """y.SetTickLength(0)
y.SetLabelOffset(0.005)


# Drawing left pad
bottom_left_pad.cd()
gStyle.SetPalette(1)
#h1.Draw("LEGO2Z")
h1.Draw("COLZ text E")

c1.Print("Cutflow_efficiency_plot.pdf")\n
"""

#print(source)
exec(source)