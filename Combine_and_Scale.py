import ROOT


input_root_file = ROOT.TFile.Open("outputs/Chi_t_500GeV_phi_100MeV.root","UPDATE")

output_root_file = ROOT.TFile.Open("Combined_files/Chi_t_500GeV_phi_100MeV.root","RECREATE")

signal_events = 1
background_events = 1
lumi = 150

def merge_histos(signal_histo, background_histo, input_root_file, output_root_file):

	opened_signal_histo = input_root_file.Get(signal_histo)
	opened_background_histo = input_root_file.Get(background_histo)

	new_histo_name = signal_histo
	if 'signal' in new_histo_name: new_histo_name = new_histo_name.replace('signal', 'Merged')
	if 'Signal' in new_histo_name: new_histo_name = new_histo_name.replace('Signal', 'Merged')

	number_of_bins = opened_signal_histo.GetNbinsX()
	max_x_bin = opened_signal_histo.GetXaxis().GetXmax()
	min_x_bin = opened_signal_histo.GetXaxis().GetXmin()
	histo_title = opened_signal_histo.GetXaxis().GetTitle()

	if 'signal' in histo_title: histo_title = histo_title.replace('signal', '')
	if 'Signal' in histo_title: histo_title = histo_title.replace('Signal', '')

	opened_signal_histo.SetLineColor(ROOT.kBlue);
	opened_background_histo.SetLineColor(ROOT.kRed);

	c1_name = "Pads_"+new_histo_name

	c1 = ROOT.TCanvas(c1_name, c1_name, 800, 400)

	pad1 = ROOT.TPad("Pad1", "Pad1", 0.0, 0.0, 0.95, 0.95)
	pad1.SetLeftMargin(0.17)
	pad1.Draw()
	pad1.cd()

	hs1 = ROOT.THStack(new_histo_name, new_histo_name)
	hs1.Add(opened_signal_histo)
	hs1.Add(opened_background_histo)
	hs1.Draw("Pads")

	filename = "temp/sbs_"+new_histo_name+".pdf"

	output_root_file.cd()

	c1.Write()

	c2_name ="nostack_"+new_histo_name

	c2 = ROOT.TCanvas(c2_name, c2_name, 500, 400)

	pad2 = ROOT.TPad("Pad2", "Pad2", 0.0, 0.0, 0.95, 0.95)
	pad2.SetLeftMargin(0.17)
	pad2.Draw()
	pad2.cd()

	hs2 = ROOT.THStack(new_histo_name, new_histo_name)
	hs2.Add(opened_signal_histo)
	hs2.Add(opened_background_histo)
	hs2.Draw("nostack")

	#Have to draw the histo before accessing the x-axis
	hs2.GetXaxis().SetTitle(histo_title)

	legend = ROOT.TLegend(0.7, 0.6, .99, .7)
	legend.AddEntry(opened_signal_histo,"m(#chi) = 500 GeV, m(#phi) = 100 MeV")
	legend.AddEntry(opened_background_histo,"P P > t t~ a")

	legend.Draw()

	filename = "temp/stacked_"+new_histo_name+".pdf"

	c2.Write()


root_keys = input_root_file.GetListOfKeys()

histo_list = []

signal_list = [] #contains names of signal histos
background_list= [] #contains names of background histos

for key in root_keys:
	key_obj = key.ReadObj()
	histo_name = key_obj.GetName()
	histo_list.append(histo_name)
	if ("Signal" in histo_name) or ("signal" in histo_name): signal_list.append(histo_name)
	if ("Background" in histo_name) or ("background" in histo_name): background_list.append(histo_name)

for signal_histo, background_histo in zip(signal_list, background_list):

	merge_histos(signal_histo, background_histo, input_root_file, output_root_file)

input_root_file.Purge()
input_root_file.Close()
output_root_file.Close()

