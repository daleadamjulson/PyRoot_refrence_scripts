#Z->mu+mu

from ROOT import TCanvas, TGraph, TGraphErrors, TMultiGraph, TPad, TAxis, TLatex, TStyle, gStyle, TLatex, TMathText, TPaveText, TLegend, TColor, kGreen, TLine
from array import array
import numpy as np

c1 = TCanvas("c1", "c1",1500,750)

sigma_1 = 1.69
sigma_3 = 3.0
sigma_5 = 5.0

n = 7
zero=[0,0,0,0,0,0,0]

Chi_t_mass = np.array([500,750,1000,1250,1500,1750,2000], dtype='float64')

#150 lumi values
phi_1_mev_150 = [41.19, 12.42, 2.76, 0.77, 0.20, 0.07, 0.02]
phi_1_mev_150_err = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

phi_1_25_mev_150 = [53.85, 24.83, 10.01, 5.36, 1.55, 0.64, 0.20]
phi_1_25_mev_150_err = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

phi_1_5_mev_150 = [54.03, 25.59, 11.17, 5.39, 2.55, 1.31, 0.57]
phi_1_5_mev_150_err = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

phi_100_mev_150 = [54.03, 25.61, 11.19, 5.39, 2.67, 1.37, 0.63]
phi_100_mev_150_err = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

#3000 lumi values
phi_1_mev_3000 = [184.21, 55.53, 12.33, 3.44, 0.91, 0.31, 0.10]
phi_1_mev_3000_err = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

phi_1_25_mev_3000 = [240.83, 111.05, 44.75, 18.42, 6.91, 2.84, 0.90]
phi_1_25_mev_3000_err = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

phi_1_5_mev_3000 = [241.62, 114.46, 49.95, 23.95, 11.41, 5.84, 2.56]
phi_1_5_mev_3000_err = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

phi_100_mev_3000 = [241.62, 114.51, 50.05, 24.10, 11.96, 6.11, 2.81]
phi_100_mev_3000_err = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    
# Declaration of bins (150 lumi values)
phi_1_mev_150_bins = np.array(phi_1_mev_150, dtype='float64')
phi_1_mev_150_err_bins_x = np.array(zero, dtype='float64')
phi_1_mev_150_err_bins_y = np.array(phi_1_mev_150_err, dtype='float64')

phi_1_25_mev_150_bins = np.array(phi_1_25_mev_150, dtype='float64')
phi_1_25_mev_150_err_bins_x = np.array(zero, dtype='float64')
phi_1_25_mev_150_err_bins_y = np.array(phi_1_25_mev_150_err, dtype='float64')

phi_1_5_mev_150_bins = np.array(phi_1_5_mev_150, dtype='float64')
phi_1_5_mev_150_err_bins_x = np.array(zero, dtype='float64')
phi_1_5_mev_150_err_bins_y = np.array(phi_1_5_mev_150_err, dtype='float64')

phi_100_mev_150_bins = np.array(phi_100_mev_150, dtype='float64')
phi_100_mev_150_err_bins_x = np.array(zero, dtype='float64')
phi_100_mev_150_err_bins_y = np.array(phi_100_mev_150_err, dtype='float64')

# Declaration of bins (3000 lumi values)
phi_1_mev_3000_bins = np.array(phi_1_mev_3000, dtype='float64')
phi_1_mev_3000_err_bins_x = np.array(zero, dtype='float64')
phi_1_mev_3000_err_bins_y = np.array(phi_1_mev_3000_err, dtype='float64')

phi_1_25_mev_3000_bins = np.array(phi_1_25_mev_3000, dtype='float64')
phi_1_25_mev_3000_err_bins_x = np.array(zero, dtype='float64')
phi_1_25_mev_3000_err_bins_y = np.array(phi_1_25_mev_3000_err, dtype='float64')

phi_1_5_mev_3000_bins = np.array(phi_1_5_mev_3000, dtype='float64')
phi_1_5_mev_3000_err_bins_x = np.array(zero, dtype='float64')
phi_1_5_mev_3000_err_bins_y = np.array(phi_1_5_mev_3000_err, dtype='float64')

phi_100_mev_3000_bins = np.array(phi_100_mev_3000, dtype='float64')
phi_100_mev_3000_err_bins_x = np.array(zero, dtype='float64')
phi_100_mev_3000_err_bins_y = np.array(phi_100_mev_3000_err, dtype='float64')
    
bottom_left_pad = TPad("bottom_left_pad", "center_pad",0.05,0.0,0.5,0.9)
bottom_left_pad.SetGridx()
bottom_left_pad.SetGridy()
bottom_left_pad.SetLogy()
bottom_left_pad.Draw()
    
bottom_right_pad = TPad("bottom_right_pad", "center_pad",0.55,0.0,1,0.9)
bottom_right_pad.SetGridx()
bottom_right_pad.SetGridy()
bottom_right_pad.SetLogy()
bottom_right_pad.Draw()

# 150 lumi TGraphs.
h1 = TGraphErrors(n, Chi_t_mass, phi_1_mev_150_bins, phi_1_mev_150_err_bins_x, phi_1_mev_150_err_bins_y)
h2 = TGraphErrors(n, Chi_t_mass, phi_1_25_mev_150_bins, phi_1_25_mev_150_err_bins_x, phi_1_25_mev_150_err_bins_y)
h3 = TGraphErrors(n, Chi_t_mass, phi_1_5_mev_150_bins, phi_1_5_mev_150_err_bins_x, phi_1_5_mev_150_err_bins_y)
h4 = TGraphErrors(n, Chi_t_mass, phi_100_mev_150_bins, phi_100_mev_150_err_bins_x, phi_100_mev_150_err_bins_y)

# 150 lumi TGraph line styles
h1.SetLineColor(1)
h1.SetLineStyle(1)
h1.SetLineWidth(1)#5
# h2.SetLineColor()
# h3.SetLineColor()
h4.SetLineColor(1)#kGreen+3
h4.SetLineStyle(8)
h4.SetLineWidth(1)#6

# 3000 lumi TGraphs.
h5 = TGraphErrors(n, Chi_t_mass, phi_1_mev_3000_bins, phi_1_mev_3000_err_bins_x, phi_1_mev_3000_err_bins_y)
h6 = TGraphErrors(n, Chi_t_mass, phi_1_25_mev_3000_bins, phi_1_25_mev_3000_err_bins_x, phi_1_25_mev_3000_err_bins_y)
h7 = TGraphErrors(n, Chi_t_mass, phi_1_5_mev_3000_bins, phi_1_5_mev_3000_err_bins_x, phi_1_5_mev_3000_err_bins_y)
h8 = TGraphErrors(n, Chi_t_mass, phi_100_mev_3000_bins, phi_100_mev_3000_err_bins_x, phi_100_mev_3000_err_bins_y)

# 3000 lumi TGraph line styles
h5.SetLineColor(1)
h5.SetLineStyle(1)
h5.SetLineWidth(1)#5
# h6.SetLineColor()
# h7.SetLineColor()
h8.SetLineColor(1)#kGreen+3
h8.SetLineStyle(8)
h8.SetLineWidth(1)#6

bottom_left_pad.cd()
mg1  = TMultiGraph()
mg1.SetTitle("Signal Significance (L_{int} = 150 fb^{1})")
mg1.Add(h1)
# mg1.Add(h2)
# mg1.Add(h3)
mg1.Add(h4)
mg1.GetYaxis().SetRangeUser(1.0e-02,300)
# mg1.GetXaxis().SetNdivisions(5)
mg1.GetXaxis().SetTitle("#chi_{t} Mass (GeV)")
mg1.GetYaxis().SetTitle("Signal Significance")
mg1.GetYaxis().SetTitleOffset(1.5)
mg1.Draw("APL")

line1 = TLine(500,sigma_1,2000,sigma_1)
line1.SetLineColor(2)
line1.SetLineWidth(1)#2
line1.SetLineStyle(9)

line2 = TLine(500,sigma_3,2000,sigma_3)
line2.SetLineColor(2)
line2.SetLineWidth(1)#2
line2.SetLineStyle(9)

line3 = TLine(500,sigma_5,2000,sigma_5)
line3.SetLineColor(2)
line3.SetLineWidth(1)#2
line3.SetLineStyle(9)

line1.Draw("same")
line2.Draw("same")
line3.Draw("same")

text1 = TLatex()
text1.SetTextSize(0.025)
text1.SetTextColor(2)
text1.DrawLatex(675,(sigma_1+0.1),"1.69#sigma")
text1.DrawLatex(605,(sigma_3+0.1),"3#sigma")
text1.DrawLatex(500,(sigma_5+0.2),"5#sigma")
        
T1 = TLegend(0.6,0.75,0.88,0.89)
T1.SetTextSize(0.03)
T1.AddEntry(h1,"#phi mass 1 MeV")
# T1.AddEntry(h2,"#phi mass 1.25 MeV")
# T1.AddEntry(h3,"#phi mass 1.5 MeV")
T1.AddEntry(h4,"#phi mass 100 MeV")
T1.Draw()

# Drawing right pad
bottom_right_pad.cd()
mg2  = TMultiGraph()
mg2.SetTitle("Signal Significance (L_{int} = 3000 fb^{1})")
mg2.Add(h5)
# mg2.Add(h6)
# mg2.Add(h7)
mg2.Add(h8)
mg2.GetYaxis().SetRangeUser(1.0e-02,300)
# mg2.GetXaxis().SetNdivisions(5)
mg2.GetXaxis().SetTitle("#chi_{t} Mass (GeV)");
mg2.GetYaxis().SetTitle("Signal Significance")
mg2.GetYaxis().SetTitleOffset(1.5)
mg2.Draw("APL")

line1.Draw("same")
line2.Draw("same")
line3.Draw("same")

text2 = TLatex()
text2.SetTextSize(0.025)
text2.SetTextColor(2)
text2.DrawLatex(675,(sigma_1+0.1),"1.69#sigma")
text2.DrawLatex(605,(sigma_3+0.1),"3#sigma")
text2.DrawLatex(500,(sigma_5+0.2),"5#sigma")

T2 = TLegend(0.6,0.75,0.88,0.89)
T2.SetTextSize(0.03)
T2.AddEntry(h5,"#phi mass 1 MeV")
# T2.AddEntry(h6,"#phi mass 1.25 MeV")
# T2.AddEntry(h7,"#phi mass 1.5 MeV")
T2.AddEntry(h8,"#phi mass 100 MeV")
T2.Draw()


c1.Print("U1T3R_Signal_Significance.pdf")
