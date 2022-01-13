import ROOT

input_root_file = ROOT.TFile.Open("WZ_2016.root","UPDATE")

output_root_file = ROOT.TFile.Open("Edited_output.root","RECREATE")

root_keys = input_root_file.GetListOfKeys()

for key in root_keys:
	key_obj = key.ReadObj()
	# histo_name = key_obj.GetName()
	# print(histo_name)
	# print(type(histo_name))

# ROOT.gStyle.SetLineStyleString(1,"400 200")

output_root_file.cd()

############################
# b+l+nu invariant mass 
############################

NMuon1 = input_root_file.Get("NGenElectron/NMuon1")

NMuon1.SetLineColor(ROOT.kBlue)

c1 = ROOT.TCanvas("NMuon1", "NMuon1", 600, 400)

pad1 = ROOT.TPad("Pad1", "Pad1", 0.0, 0.0, 0.95, 0.95)
pad1.Draw()
pad1.cd()

NMuon1.Scale(1.0/NMuon1.Integral(0,10000))

th1 = ROOT.THStack()
th1.Add(NMuon1)
th1.Draw("Hist text")

th1.GetXaxis().SetTitle("NMuon1")
th1.GetYaxis().SetTitle("a.u.")


c1.Write()


input_root_file.Purge()
input_root_file.Close()
output_root_file.Close()

