#!/Users/dalejulson/Desktop/VandyResearch/Dark_photon/venv/bin/python


"""

THE ACTUAL USEFUL SCRIPT IS INSIDE DARK_PHOTON/VENV/BIN. THIS IS JUST A REFERENCE!!!!!!!

"""

import sys
import ROOT as r

print(sys.argv[1])
root_file = sys.argv[1]

f = r.TFile.Open(root_file)

VBF = "VBF1"
set_year = 2016

lumi = [35.9, 41.5, 59.7]
legend_nColumn = 3

def replot(cut_level, specific_plot, year, set_log_y = True, change_y_range = False, auto_y = True, y_min = 0, y_max = 10e6, change_x_range = False, x_min = 0, x_max = 100, change_b_range = False, b_min = 0, b_max = 2.5):

	dir_cut_level = f.Get(cut_level)
	canvas = dir_cut_level.Get(specific_plot) #Gets the canvas

	top_pad = canvas.GetPad(1) #gets the top pad, TLists start at 1 and not 0.
	bottom_pad = canvas.GetPad(2) #gets the bottom pad.


	histo_plot = top_pad.GetPrimitive(specific_plot) #Get Histogram
	ratio_plot = bottom_pad.GetPrimitive("error_rebin") # get ratio plot

	lumi_text = top_pad.GetListOfPrimitives()[3]
	lumi_text.Clear()
	lumi_text.AddText("{} fb^{} (13 TeV)".format(lumi[abs(2018-(year+2))],"{-1}"))

	histo_title = top_pad.GetListOfPrimitives()[1]
	histo_title.Clear()

	legend = top_pad.GetListOfPrimitives()[7]
	legend.SetNColumns(legend_nColumn)
	legend.SetTextSize(0.03)
	legend.SetY1(0.3)

	if legend_nColumn > 1:
		legend.SetX1(0.8-legend_nColumn*0.06)
		legend.SetY1(0.5+legend_nColumn*0.06)

	if change_y_range:
		if set_log_y:
			top_pad.SetLogy()
			if auto_y:
				histo_plot.SetMaximum(histo_plot.GetMaximum()*150)
				histo_plot.SetMinimum(10**(-1))
			else:
				histo_plot.SetMaximum(y_max)
				histo_plot.SetMinimum(y_min)
		else:
			if auto_y:
				histo_plot.SetMaximum(histo_plot.GetMaximum()+10)
			else:
				histo_plot.SetMaximum(y_max)
				histo_plot.SetMinimum(y_min)

	if change_x_range:
		histo_plot.GetXaxis().SetRangeUser(x_min, x_max)
		ratio_plot.GetXaxis().SetRangeUser(x_min, x_max)

	if change_b_range:
		ratio_plot.SetMaximum(b_max)
		ratio_plot.SetMinimum(b_min)

	top_pad.Modified()
	top_pad.Update()

	bottom_pad.Modified()
	bottom_pad.Update()

	canvas.Modified()
	canvas.Update()

	outfile = "{}{}_{}_{}".format(year,VBF,cut_level,specific_plot)
	canvas.SaveAs("{}.pdf".format(outfile))


###Central Selection Plots
replot("NRecoTau1", "Muon1Pt", set_year, set_log_y = True, change_y_range = True, auto_y = True, y_min = 10e-2, y_max = 5e6, change_x_range = True, x_min=0, x_max=500, change_b_range = True, b_min = 0, b_max = 2.9)
replot("NRecoTau1", "Muon1Eta", set_year, set_log_y = True, change_y_range = True, auto_y = False,  y_min = 10e-2, y_max = 5e6, change_x_range = False, x_min=0, x_max=500, change_b_range = True, b_min = 0, b_max = 2.9)
replot("NRecoTau1", "Met", set_year, set_log_y = True, change_y_range = True, auto_y = True, y_min = 10e-2, y_max = 5e6, change_x_range = True, x_min=250, x_max=1000, change_b_range = True, b_min = 0, b_max = 2.9)
replot("NRecoTau1", "Muon1MetMt", set_year, set_log_y = True, change_y_range = True, auto_y = True, y_min = 10e-2, y_max = 5e6, change_x_range = True, x_min=60, x_max=100, change_b_range = True, b_min = 0, b_max = 2.9)

###VBF Selection Plots
replot("NDiJetCombinations", "Jet1Pt", set_year, set_log_y = True, change_y_range = True, auto_y = True, y_min = 10e-2, y_max = 5e6, change_x_range = True, x_min=50, x_max=500, change_b_range = True, b_min = 0, b_max = 2.9)
replot("NDiJetCombinations", "Jet1Eta", set_year, set_log_y = True, change_y_range = True, auto_y = True,  y_min = 10e-2, y_max = 5e6, change_x_range = True, x_min=-4.7, x_max=4.7, change_b_range = True, b_min = 0, b_max = 2.9)
replot("NDiJetCombinations", "Met", set_year, set_log_y = True, change_y_range = True, auto_y = False, y_min = 10e-4, y_max = 5e3, change_x_range = True, x_min=250, x_max=1000, change_b_range = True, b_min = 0, b_max = 2.9)
replot("NDiJetCombinations", "FirstLeadingJetPt", set_year, set_log_y = True, change_y_range = True, auto_y = False, y_min = 10e-4, y_max = 1e2, change_x_range = True, x_min=50, x_max=1000, change_b_range = True, b_min = 0, b_max = 2.9)
replot("NDiJetCombinations", "FirstLeadingJetEta", set_year, set_log_y = True, change_y_range = True, auto_y = True,  y_min = 10e-2, y_max = 5e6, change_x_range = True, x_min=-4.7, x_max=4.7, change_b_range = True, b_min = 0, b_max = 2.9)
replot("NDiJetCombinations", "LargestDiJetMass", set_year, set_log_y = True, change_y_range = True, auto_y = False, y_min = 10e-4, y_max = 100, change_x_range = True, x_min=1000, x_max=5000, change_b_range = True, b_min = 0, b_max = 2.9)
replot("NDiJetCombinations", "LargestMassDiJetDeltaEta", set_year, set_log_y = True, change_y_range = True, auto_y = True,  y_min = 10e-4, y_max = 5e3, change_x_range = True, x_min=6, x_max=9, change_b_range = True, b_min = 0, b_max = 2.9)


f.Close()
