import ROOT 
#from numpy import array
from array import array

c1 = ROOT.TCanvas( 'c1', 'A Simple Graph Example', 200, 10, 700, 500 )
 
# c1.SetFillColor( 42 )
# c1.SetGrid()
# X AXIS POINTS
x_points = [1,2,3,4,5]
x = array('d')

# exl_0 = array('d')
# exh_0 = array('d')

#dM=75 Stuff
UL_points_75 = [22.3750, 25.1250, 22.000, 22.9375, 26.5000] 
y_75 = array('d')
Min_75 = min(UL_points_75)

# UL_err_l_75 = [15.2736, 15.9316, 14.0647, 15.7695, 18.1541]
# eyl_75 = array('d')

# UL_err_h_75 = [33.4343, 37.1061, 32.5888, 34.0005, 39.4925]
# eyh_75 = array('d')

#dM=20 Stuff
UL_points_20 = [6.2500, 5.0469, 3.4844, 4.9531, 6.4062] 
y_20 = array('d')
Min_20 = min(UL_points_20)

# UL_err_l_20 = [4.2416, 3.6452, 2.7314, 3.4053, 4.3730]
# eyl_20 = array('d')

# UL_err_h_20 = [9.3392, 8.6202, 6.4018, 7.3618, 9.5471]
# eyh_20 = array('d')

n = len(x_points)

for i in range(n):

    x.append(x_points[i])

    y_75.append(UL_points_75[i]/Min_75)
    # eyl_75.append((UL_points_75[i] - UL_err_l_75[i])/Min_75)
    # eyh_75.append((UL_err_h_75[i] - UL_points_75[i])/Min_75)

    y_20.append(UL_points_20[i]/Min_20)
    # eyl_20.append((UL_points_20[i] - UL_err_l_20[i])/Min_20)
    # eyh_20.append((UL_err_h_20[i] - UL_points_20[i])/Min_20)

    # exl_0.append(0.0)
    # exh_0.append(0.0)


#gr1 = ROOT.TGraphAsymmErrors( n, x, y_75, exl = exl_0, exh = exh_0, eyl = eyl_75, eyh = eyh_75)
gr1 = ROOT.TGraph( n, x, y_75)
gr1.SetLineColor( ROOT.kAzure-3 )
gr1.SetLineStyle( 10 )
gr1.SetLineWidth( 3 )
gr1.SetMarkerColor( ROOT.kAzure-3 )
gr1.SetMarkerStyle( 25 )

# gr2 = ROOT.TGraphAsymmErrors( n, x, y_20, exl = exl_0, exh = exh_0, eyl = eyl_20, eyh = eyh_20)
gr2 = ROOT.TGraph( n, x, y_20)
gr2.SetLineColor( ROOT.kPink+7 )
gr2.SetLineStyle( 9 )
gr2.SetLineWidth( 3 )
gr2.SetMarkerColor( ROOT.kPink+7 )
gr2.SetMarkerStyle( 26 )

mg1 = ROOT.TMultiGraph()
mg1.Add(gr1)
mg1.Add(gr2)
mg1.SetTitle('Applied Selection [p_{T}(#mu) lower threshold, #mu ID]       VBF SUSY Wino-Bino')
# mg1.SetTitleSize(0.045)
# mg1.GetXaxis().SetTitle( 'Applied Selection [p_{T}(#mu) lower threshold, #mu ID]' )
# mg1.GetXaxis().SetTitleOffset(1.)
# mg1.GetXaxis().SetTitleSize(0.045)
# mg1.GetXaxis().SetLabelSize(0.35)
mg1.GetYaxis().SetTitle( '#sigma_{UL} / #sigma^{min}_{UL}' )
mg1.GetYaxis().SetTitleSize(0.055)
mg1.GetYaxis().SetTitleOffset(0.7)

ROOT.gStyle.SetTitleSize(0.755)

x_axis = mg1.GetXaxis()
x_axis.SetNdivisions(5)
x_axis.ChangeLabel(1,0.,0.03,-1,-1,-1, '#splitline{pt(#mu)#geq8 GeV}{TightID}')
x_axis.ChangeLabel(2,0.,0.03,-1,-1,-1, '#splitline{pt(#mu)#geq8 GeV}{SUSYLeptonID}')
x_axis.ChangeLabel(3,0.,0.03,-1,-1,-1, '#splitline{pt(#mu)#geq5 GeV}{SUSYLeptonID}')
x_axis.ChangeLabel(4,0.,0.03,-1,-1,-1, '#splitline{pt(#mu)#geq5 GeV}{TightID}')
x_axis.ChangeLabel(5,0.,0.03,-1,-1,-1, '#splitline{pt(#mu)#geq8 GeV}{TightID, TightLepVetoID}')
x_axis.SetLabelOffset(0.03)

line = ROOT.TLine(0.8,1,5.2,1)
line.SetLineWidth(2)

T1 = ROOT.TLegend(0.55,0.75,0.88,0.89)
T1.SetTextSize(0.03)
T1.AddEntry(gr1, "m(#tilde{#Chi}^{0}_{2}) = 100GeV, #DeltaM = 75")
T1.AddEntry(gr2, "m(#tilde{#Chi}^{0}_{2}) = 100GeV, #DeltaM = 20")

mg1.Draw('ALP')
line.Draw("same")
T1.Draw("same")

# TCanvas.Update() draws the frame, after which one can change it
c1.Update()
# c1.GetFrame().SetFillColor( 21 )
c1.GetFrame().SetBorderSize( 12 )
c1.Modified()
c1.Update()
# If the graph does not appear, try using the "i" flag, e.g. "python3 -i graph.py"
# This will access the interactive mode after executing the script, and thereby persist
# long enough for the graph to appear.
