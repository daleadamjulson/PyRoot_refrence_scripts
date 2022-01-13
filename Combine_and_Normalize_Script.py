import ROOT

input_root_file1 = ROOT.TFile.Open("2016_100_25p00_WZ_2016.root ","UPDATE")
input_root_file2 = ROOT.TFile.Open("2016_100_50p00_WZ_2016.root ","UPDATE")
input_root_file3 = ROOT.TFile.Open("2016_100_80p00_WZ_2016.root ","UPDATE")
input_root_file4= ROOT.TFile.Open("2016_100_95p00_WZ_2016.root ","UPDATE")
input_root_file5 = ROOT.TFile.Open("2016_100_99p00_WZ_2016.root ","UPDATE")
input_root_file6 = ROOT.TFile.Open("2016_100_99p50_WZ_2016.root ","UPDATE")

output_root_file = ROOT.TFile.Open("Combined.root","RECREATE")

root_colors = [ROOT.kBlue, ROOT.kRed, ROOT.kGreen+3, ROOT.kCyan-3, ROOT.kMagenta, ROOT.kYellow+2]
# root_names = ["100_25p00 (dM 75)", "100_50p00", "100_80p00", "100_95p00", "100_99p00", "100_99p50"]
# root_names = ["(dM 75)", "(dM 50)", "(dM 20)", "(dM 5)", "(dM 1)", "(dM 0.5)"]
root_names = ["(dM 50)", "(dM 20)", "(dM 5)", "(dM 1)", "(dM 0.5)"]
root_styles = [1, 2, 4, 5, 8, 10]

def merge_histos(histo, output_root_file, *input_root_file):

	ROOT.gStyle.SetOptStat("e")

	c = ROOT.TCanvas(histo, histo, 500, 400)

	pad = ROOT.TPad("Pad", "Pad", 0.0, 0.0, 0.95, 0.95)
	pad.SetLeftMargin(0.17)
	pad.Draw()
	pad.cd()

	hs = ROOT.THStack(histo, histo)
	hs.Draw()

	legend = ROOT.TLegend(0.8, 0.65, .99, .85)
	legend.Draw()

	for enum, root_file in enumerate(input_root_file):

		opened_histo = root_file.Get(histo)
		opened_histo.SetLineColor(root_colors[enum])
		opened_histo.SetLineWidth(3)
		opened_histo.SetLineStyle(root_styles[enum])

		hs.Add(opened_histo)
		legend.AddEntry(opened_histo, root_names[enum])

	hs.GetXaxis().SetTitle(histo)
	hs.Draw("nostack Hist")
	legend.Draw()

	output_root_file.cd()
	c.Write()

def normalize_histos(histo, output_root_file, *input_root_file):

	ROOT.gStyle.SetOptStat("e")

	c = ROOT.TCanvas("Normalized_"+histo, "Normalized_"+histo, 500, 400)

	pad = ROOT.TPad("Pad", "Pad", 0.0, 0.0, 0.95, 0.95)
	pad.SetLeftMargin(0.17)
	pad.Draw()
	pad.cd()

	hs = ROOT.THStack("Normalized_"+histo, "Normalized_"+histo)
	hs.Draw()

	legend = ROOT.TLegend(0.8, 0.65, .99, .85)
	legend.Draw()

	for enum, root_file in enumerate(input_root_file):

		opened_histo = root_file.Get(histo)
		opened_histo.SetLineColor(root_colors[enum])
		opened_histo.Scale(1/opened_histo.Integral(-10000,10000))

		hs.Add(opened_histo)
		legend.AddEntry(opened_histo, root_names[enum])

	hs.GetXaxis().SetTitle("Normalized "+histo)
	hs.Draw("nostack Hist")
	legend.Draw()

	output_root_file.cd()
	c.Write()


# root_keys1 = input_root_file1.GetListOfKeys()
# root_keys2 = input_root_file2.GetListOfKeys()
# root_keys3 = input_root_file3.GetListOfKeys()
# root_keys4 = input_root_file4.GetListOfKeys()
# root_keys5 = input_root_file5.GetListOfKeys()
# root_keys6 = input_root_file6.GetListOfKeys()

# for key in root_keys1:
# 	key_obj = key.ReadObj()
# 	histo_name = key_obj.GetName()

# for key in root_keys2:
# 	key_obj = key.ReadObj()
# 	histo_name = key_obj.GetName()

# for key in root_keys3:
# 	key_obj = key.ReadObj()
# 	histo_name = key_obj.GetName()

# for key in root_keys4:
# 	key_obj = key.ReadObj()
# 	histo_name = key_obj.GetName()

# for key in root_keys5:
# 	key_obj = key.ReadObj()
# 	histo_name = key_obj.GetName()

# for key in root_keys6:
# 	key_obj = key.ReadObj()
# 	histo_name = key_obj.GetName()

list_of_histos = ["NGenElectron/NGenMuon", "NGenMuon/GenMuonPt", "NGenMuon/GenMuonEta", "NRecoMuon1/Muon1Pt", "NRecoMuon1/Muon1Eta", 
"NRecoMuon1/DiMuonReconstructableMass", "NRecoMuon2/Muon1Pt", "NRecoMuon2/Muon1Eta", "NRecoMuon2/DiMuonReconstructableMass", "NRecoJet1/Jet1Pt", 
"NRecoJet1/Jet1Eta", "NRecoJet1/FirstLeadingJetEta", "NRecoJet1/FirstLeadingJetPt", "NRecoJet1/LargestDiJetMass", "NRecoJet1/LargestMassDiJetDeltaEta", 
"NRecoJet1/MetPhi", "NRecoJet1/Jet1Phi", "NRecoJet1/Jet1Eta", "NRecoJet1/Jet1Pt", "NRecoJet2/Jet1Pt", "NRecoJet2/Jet1Eta", "NRecoJet2/FirstLeadingJetEta", 
"NRecoJet2/FirstLeadingJetPt", "NRecoJet2/LargestDiJetMass", "NRecoJet2/LargestMassDiJetDeltaEta", "NRecoJet2/MetPhi", "NRecoJet2/Jet1Phi", "NRecoJet2/Jet1Eta", "NRecoJet2/Jet1Pt"]

for histo in list_of_histos:
	print(histo)
	# merge_histos(histo, output_root_file, input_root_file1, input_root_file2, input_root_file3, input_root_file4, input_root_file5, input_root_file6)
	# normalize_histos(histo, output_root_file, input_root_file1, input_root_file2, input_root_file3, input_root_file4, input_root_file5, input_root_file6)
	merge_histos(histo, output_root_file, input_root_file2, input_root_file3, input_root_file4, input_root_file5, input_root_file6)
	normalize_histos(histo, output_root_file, input_root_file2, input_root_file3, input_root_file4, input_root_file5, input_root_file6)

input_root_file1.Purge()
input_root_file1.Close()

input_root_file2.Purge()
input_root_file2.Close()

input_root_file3.Purge()
input_root_file3.Close()

input_root_file4.Purge()
input_root_file4.Close()

input_root_file5.Purge()
input_root_file5.Close()

input_root_file6.Purge()
input_root_file6.Close()

output_root_file.Close()

