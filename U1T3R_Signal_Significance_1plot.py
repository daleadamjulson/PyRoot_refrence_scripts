#Z->mu+mu

from ROOT import TCanvas, TGraph, TGraphErrors, TMultiGraph, TPad, TAxis, TLatex, TStyle, gStyle, TLatex, TMathText, TPaveText, TLegend, TColor, kGreen, kMagenta, TLine, TBrowser
from array import array
import numpy as np

c1 = TCanvas("c1", "c1",700,600)

sigma_1 = 1.69
sigma_3 = 3.0
sigma_5 = 5.0

n = 9
zero=[0,0,0,0,0,0,0,0,0]

Chi_t_mass = np.array([500,750,1000,1250,1500,1750,2000,2250,2500], dtype='float64')

#150 lumi values
phi_1_mev_150 = [41.18984051, 12.16856903, 2.75603667, 0.76993068, 0.20379948, 0.06925405, 0.02377175, 0.00729148, 0.00446257]
phi_1_mev_150_err = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# phi_1_25_mev_150 = [53.85, 24.83, 10.01, 5.36, 1.55, 0.64, 0.20]
# phi_1_25_mev_150_err = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

# phi_1_5_mev_150 = [54.03, 25.59, 11.17, 5.39, 2.55, 1.31, 0.57]
# phi_1_5_mev_150_err = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

phi_100_mev_150 = [54.02765450, 25.13994889, 11.19148567, 5.38847437, 2.67386681, 1.36527447, 0.63524619, 0.30229076, 0.22959453]
phi_100_mev_150_err = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

#3000 lumi values
phi_1_mev_3000 = [184.20656673, 54.41949508, 12.32537068, 3.44323467, 0.91141897, 0.30971351, 0.10631051, 0.03260848, 0.01995720]
phi_1_mev_3000_err = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# phi_1_25_mev_3000 = [240.83, 111.05, 44.75, 18.42, 6.91, 2.84, 0.90]
# phi_1_25_mev_3000_err = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

# phi_1_5_mev_3000 = [241.62, 114.46, 49.95, 23.95, 11.41, 5.84, 2.56]
# phi_1_5_mev_3000_err = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

phi_100_mev_3000 = [241.61901627, 114.42926932, 50.04984544, 24.09798996, 11.95789588, 6.10569305, 2.84090735, 1.35188540, 1.02677797]
phi_100_mev_3000_err = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
# Declaration of bins (150 lumi values)
phi_1_mev_150_bins = np.array(phi_1_mev_150, dtype='float64')
phi_1_mev_150_err_bins_x = np.array(zero, dtype='float64')
phi_1_mev_150_err_bins_y = np.array(phi_1_mev_150_err, dtype='float64')

# phi_1_25_mev_150_bins = np.array(phi_1_25_mev_150, dtype='float64')
# phi_1_25_mev_150_err_bins_x = np.array(zero, dtype='float64')
# phi_1_25_mev_150_err_bins_y = np.array(phi_1_25_mev_150_err, dtype='float64')

# phi_1_5_mev_150_bins = np.array(phi_1_5_mev_150, dtype='float64')
# phi_1_5_mev_150_err_bins_x = np.array(zero, dtype='float64')
# phi_1_5_mev_150_err_bins_y = np.array(phi_1_5_mev_150_err, dtype='float64')

phi_100_mev_150_bins = np.array(phi_100_mev_150, dtype='float64')
phi_100_mev_150_err_bins_x = np.array(zero, dtype='float64')
phi_100_mev_150_err_bins_y = np.array(phi_100_mev_150_err, dtype='float64')

# Declaration of bins (3000 lumi values)
phi_1_mev_3000_bins = np.array(phi_1_mev_3000, dtype='float64')
phi_1_mev_3000_err_bins_x = np.array(zero, dtype='float64')
phi_1_mev_3000_err_bins_y = np.array(phi_1_mev_3000_err, dtype='float64')

# phi_1_25_mev_3000_bins = np.array(phi_1_25_mev_3000, dtype='float64')
# phi_1_25_mev_3000_err_bins_x = np.array(zero, dtype='float64')
# phi_1_25_mev_3000_err_bins_y = np.array(phi_1_25_mev_3000_err, dtype='float64')

# phi_1_5_mev_3000_bins = np.array(phi_1_5_mev_3000, dtype='float64')
# phi_1_5_mev_3000_err_bins_x = np.array(zero, dtype='float64')
# phi_1_5_mev_3000_err_bins_y = np.array(phi_1_5_mev_3000_err, dtype='float64')

phi_100_mev_3000_bins = np.array(phi_100_mev_3000, dtype='float64')
phi_100_mev_3000_err_bins_x = np.array(zero, dtype='float64')
phi_100_mev_3000_err_bins_y = np.array(phi_100_mev_3000_err, dtype='float64')
    
center_pad = TPad("center_pad", "center_pad",0.05,0.0,1,1)
center_pad.SetGridx()
center_pad.SetGridy()
center_pad.SetLogy()
center_pad.Draw()


# 150 lumi TGraphs.
h1 = TGraphErrors(n, Chi_t_mass, phi_1_mev_150_bins, phi_1_mev_150_err_bins_x, phi_1_mev_150_err_bins_y)
# h2 = TGraphErrors(n, Chi_t_mass, phi_1_25_mev_150_bins, phi_1_25_mev_150_err_bins_x, phi_1_25_mev_150_err_bins_y)
# h3 = TGraphErrors(n, Chi_t_mass, phi_1_5_mev_150_bins, phi_1_5_mev_150_err_bins_x, phi_1_5_mev_150_err_bins_y)
h4 = TGraphErrors(n, Chi_t_mass, phi_100_mev_150_bins, phi_100_mev_150_err_bins_x, phi_100_mev_150_err_bins_y)

# 150 lumi TGraph line styles
h1.SetLineColor(kMagenta+0)
h1.SetLineStyle(1)
h1.SetLineWidth(2)#5
# h2.SetLineColor()
# h3.SetLineColor()
h4.SetLineColor(kMagenta+0)#kGreen+3
h4.SetLineStyle(8)
h4.SetLineWidth(2)#6

# 3000 lumi TGraphs.
h5 = TGraphErrors(n, Chi_t_mass, phi_1_mev_3000_bins, phi_1_mev_3000_err_bins_x, phi_1_mev_3000_err_bins_y)
# h6 = TGraphErrors(n, Chi_t_mass, phi_1_25_mev_3000_bins, phi_1_25_mev_3000_err_bins_x, phi_1_25_mev_3000_err_bins_y)
# h7 = TGraphErrors(n, Chi_t_mass, phi_1_5_mev_3000_bins, phi_1_5_mev_3000_err_bins_x, phi_1_5_mev_3000_err_bins_y)
h8 = TGraphErrors(n, Chi_t_mass, phi_100_mev_3000_bins, phi_100_mev_3000_err_bins_x, phi_100_mev_3000_err_bins_y)

# 3000 lumi TGraph line styles
h5.SetLineColor(kGreen+3)
h5.SetLineStyle(1)
h5.SetLineWidth(2)#5
# h6.SetLineColor()
# h7.SetLineColor()
h8.SetLineColor(kGreen+3)#kGreen+3
h8.SetLineStyle(8)
h8.SetLineWidth(2)#6

center_pad.cd()
mg1  = TMultiGraph()
mg1.SetTitle("Signal Significance")
mg1.Add(h1)
mg1.Add(h4)
mg1.Add(h5)
mg1.Add(h8)
mg1.GetYaxis().SetRangeUser(1.0e-03,300)
# mg1.GetXaxis().SetNdivisions(5)
mg1.GetXaxis().SetTitle("#chi_{t} Mass (GeV)")
mg1.GetYaxis().SetTitle("Signal Significance")
mg1.GetYaxis().SetTitleOffset(1.5)
mg1.Draw("APL")

line1 = TLine(500,sigma_1,2500,sigma_1)
line1.SetLineColor(2)
line1.SetLineWidth(1)#2
line1.SetLineStyle(9)

line2 = TLine(500,sigma_3,2500,sigma_3)
line2.SetLineColor(2)
line2.SetLineWidth(1)#2
line2.SetLineStyle(9)

line3 = TLine(500,sigma_5,2500,sigma_5)
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
        
T1 = TLegend(0.425,0.75,0.88,0.89)
T1.SetTextSize(0.03)
T1.AddEntry(h1,"m(#phi) = 1 MeV, L_{int} = 150b^{-1}")
T1.AddEntry(h4,"m(#phi) = 100 MeV, L_{int} = 150b^{-1}")
T1.AddEntry(h5,"m(#phi) = 1 MeV, L_{int} = 3000b^{-1}")
T1.AddEntry(h8,"m(#phi) = 100 MeV, L_{int} = 3000b^{-1}")
T1.Draw()

# b = TBrowser()

c1.Print("U1T3R_Signal_Significance_1plot.pdf")
