import ROOT 
#from numpy import array
from array import array

c1 = ROOT.TCanvas( 'c1', 'A Simple Graph Example', 200, 10, 700, 500 )
 
c1.SetFillColor( 42 )
c1.SetGrid()
 

x_points = [40,50,60]
x = array('d')
y_points = [7.5612, 7.5673, 7.5593]
y = array('d')
n = len(x_points)

for i in range(n):
    x.append(x_points[i])
    y.append(y_points[i])

gr = ROOT.TGraph( n, x, y)
gr.SetLineColor( 2 )
gr.SetLineWidth( 4 )
gr.SetMarkerColor( 4 )
gr.SetMarkerStyle( 21 )
gr.SetTitle( 'Bottom Dijet Invariant Mass Window Cut Signal Significance (150 lumi, 0% Uncty)' )
gr.GetXaxis().SetTitle( 'Bottom Dijet Invariant Mass Window Cut (GeV)' )
gr.GetYaxis().SetTitle( 'Signal Significance S/{sqrt(S+B)}' )
gr.Draw( 'ACP' )
 
# TCanvas.Update() draws the frame, after which one can change it
c1.Update()
c1.GetFrame().SetFillColor( 21 )
c1.GetFrame().SetBorderSize( 12 )
c1.Modified()
c1.Update()
# If the graph does not appear, try using the "i" flag, e.g. "python3 -i graph.py"
# This will access the interactive mode after executing the script, and thereby persist
# long enough for the graph to appear.
