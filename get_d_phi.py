import os
import ROOT as r

VBF = ['VBF1', 'VBF2', 'VBF3']
years = ['2016', '2017', '2018']

#root_file = output.root

def compare_d_phi(root_file):

    total_MC = 0
    cut_MC = 0

    f = r.TFile.Open(root_file)
    canvas = f.Get('NDiJetCombinations/Dphi1')
    #print(canvas)
    top_pad = canvas.GetPad(1)
    #prims = top_pad.GetListOfPrimitives()
    #for prim in prims:
    #    print(prim)
    data = top_pad.GetPrimitive('data_rebin')
    xmin = data.FindBin(-0.5)
    xmax = data.FindBin(0.5)
    MC = top_pad.GetPrimitive('Dphi1')
    #MC_stack = MC.GetStack().Last()
    histos = MC.begin()
    for histo in histos:
        total_MC = total_MC + histo.Integral(-100,100)
        cut_MC = cut_MC + histo.Integral(xmin,xmax)
    #print(data)
    #print(MC)
    total_data = data.Integral(-100,100)
    #total_MC = MC_stack.GetEntries()
    cut_data = data.Integral(xmin,xmax)
    print("total data is: "+str(total_data))
    print("total MC is: "+str(total_MC))
    print("cut data is: "+str(cut_data))
    print("cut MSC is: "+str(cut_MC))
    print("eff in data is: "+str(1.0-(cut_data/total_data)))
    print("eff in MC is: "+str(1.0-(cut_MC/total_MC)))
    f.Close()

    total_MC = 0
    cut_MC = 0

#compare_d_phi('2018/VBF3/VBF_Plots/output.root')
    
for year in years:
    for i in VBF:
        print(year+'   '+i+':')
        compare_d_phi(year+'/'+i+'/VBF_Plots/output.root')
        print('****')
