import ROOT

input_root_file = ROOT.TFile.Open("Analyzer_output.root","UPDATE")

output_root_file = ROOT.TFile.Open("temp/Edited_output.root","RECREATE")

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

signal_leptonic_bottom_lepton_neutrino_invariant_mass = input_root_file.Get("signal_leptonic_bottom_lepton_neutrino_invariant_mass")
background_leptonic_bottom_lepton_neutrino_invariant_mass = input_root_file.Get("background_leptonic_bottom_lepton_neutrino_invariant_mass")

signal_leptonic_bottom_lepton_neutrino_invariant_mass.SetLineColor(ROOT.kBlue)
background_leptonic_bottom_lepton_neutrino_invariant_mass.SetLineColor(ROOT.kRed)

c1 = ROOT.TCanvas("Bottom Lepton Neutrino Invariant Mass", "Bottom Lepton Neutrino Invariant Mass", 600, 400)

pad1 = ROOT.TPad("Pad1", "Pad1", 0.0, 0.0, 0.95, 0.95)
pad1.Draw()
pad1.cd()

signal_leptonic_bottom_lepton_neutrino_invariant_mass.Scale(1.0/signal_leptonic_bottom_lepton_neutrino_invariant_mass.Integral(0,10000))
background_leptonic_bottom_lepton_neutrino_invariant_mass.Scale(1.0/background_leptonic_bottom_lepton_neutrino_invariant_mass.Integral(0,10000))

th1 = ROOT.THStack("'Leptonic' Bottom Lepton Neutrino Invariant Mass", "'Leptonic' Bottom Lepton Neutrino Invariant Mass")
th1.Add(signal_leptonic_bottom_lepton_neutrino_invariant_mass)
th1.Add(background_leptonic_bottom_lepton_neutrino_invariant_mass)
th1.Draw("Hist nostack")

th1.GetXaxis().SetTitle("m(b,l,#nu) (GeV)")
th1.GetYaxis().SetTitle("a.u.")

legend1 = ROOT.TLegend(0.7, 0.6, .99, .7)
legend1.AddEntry(signal_leptonic_bottom_lepton_neutrino_invariant_mass,"m(#chi) = 500 GeV, m(#phi) = 100 MeV")
legend1.AddEntry(background_leptonic_bottom_lepton_neutrino_invariant_mass,"P P > t t~ a")
legend1.Draw()

c1.Write()

############################
# b+l+nu transverse mass 
############################

signal_leptonic_bottom_lepton_neutrino_normal_mass = input_root_file.Get("signal_leptonic_bottom_lepton_neutrino_normal_mass")
background_leptonic_bottom_lepton_neutrino_normal_mass = input_root_file.Get("background_leptonic_bottom_lepton_neutrino_normal_mass")

signal_leptonic_bottom_lepton_neutrino_normal_mass.SetLineColor(ROOT.kBlue)
background_leptonic_bottom_lepton_neutrino_normal_mass.SetLineColor(ROOT.kRed)

c2 = ROOT.TCanvas("Bottom Lepton Neutrino Tranverse Mass", "Bottom Lepton Neutrino Transverse Mass", 600, 400)
c2.cd()

pad2 = ROOT.TPad("Pad2", "Pad2", 0.0, 0.0, 0.95, 0.95)
pad2.Draw()
pad2.cd()

signal_leptonic_bottom_lepton_neutrino_normal_mass.Scale(1.0/signal_leptonic_bottom_lepton_neutrino_normal_mass.Integral(0,10000))
background_leptonic_bottom_lepton_neutrino_normal_mass.Scale(1.0/background_leptonic_bottom_lepton_neutrino_normal_mass.Integral(0,10000))

th2 = ROOT.THStack("'Leptonic' Bottom Lepton Neutrino Transverse Mass", "'Leptonic' Bottom Lepton Neutrino Transverse Mass")
th2.Add(signal_leptonic_bottom_lepton_neutrino_normal_mass)
th2.Add(background_leptonic_bottom_lepton_neutrino_normal_mass)
th2.Draw("Hist nostack")

th2.GetXaxis().SetTitle("m_{T}(b,l,#nu) (GeV)")
th2.GetYaxis().SetTitle("a.u.")

legend2 = ROOT.TLegend(0.7, 0.6, .99, .7)
legend2.AddEntry(signal_leptonic_bottom_lepton_neutrino_normal_mass,"m(#chi) = 500 GeV, m(#phi) = 100 MeV")
legend2.AddEntry(background_leptonic_bottom_lepton_neutrino_normal_mass,"P P > t t~ a")
legend2.Draw()

c2.Write()

############################
# lepton pt 
############################

signal_lepton_pt = input_root_file.Get("Signal_lepton_pt")
background_lepton_pt = input_root_file.Get("background_lepton_pt")

signal_lepton_pt.SetLineColor(ROOT.kBlue)
background_lepton_pt.SetLineColor(ROOT.kRed)

c3 = ROOT.TCanvas("Lepton Pt ", "Lepton Pt", 600, 400)
c3.cd()

pad3 = ROOT.TPad("Pad3", "Pad3", 0.0, 0.0, 0.95, 0.95)
pad3.Draw()
pad3.cd()

signal_lepton_pt.Scale(1.0/signal_lepton_pt.Integral(0,10000))
background_lepton_pt.Scale(1.0/background_lepton_pt.Integral(0,10000))

th3 = ROOT.THStack("Lepton Pt", "Lepton Pt")
th3.Add(signal_lepton_pt)
th3.Add(background_lepton_pt)
th3.Draw("Hist nostack")

th3.GetXaxis().SetTitle("Lepton p_{T} (GeV)")
th3.GetYaxis().SetTitle("a.u.")

legend3 = ROOT.TLegend(0.7, 0.6, .99, .7)
legend3.AddEntry(signal_lepton_pt,"m(#chi) = 500 GeV, m(#phi) = 100 MeV")
legend3.AddEntry(background_lepton_pt,"P P > t t~ a")
legend3.Draw()

c3.Write()

############################
# MET
############################

signal_MET = input_root_file.Get("Signal MET")
background_MET = input_root_file.Get("Background MET")

signal_MET.SetLineColor(ROOT.kBlue)
background_MET.SetLineColor(ROOT.kRed)

c4 = ROOT.TCanvas("MET ", "MET", 600, 400)
c4.cd()

pad4 = ROOT.TPad("Pad4", "Pad4", 0.0, 0.0, 0.95, 0.95)
pad4.Draw()
pad4.cd()

signal_MET.Scale(1.0/signal_MET.Integral(0,10000))
background_MET.Scale(1.0/background_MET.Integral(0,10000))

th4 = ROOT.THStack("MET", "MET")
th4.Add(signal_MET)
th4.Add(background_MET)
th4.Draw("Hist nostack")

th4.GetXaxis().SetTitle("MET (GeV)")
th4.GetYaxis().SetTitle("a.u.")

legend4 = ROOT.TLegend(0.7, 0.6, .99, .7)
legend4.AddEntry(signal_MET,"m(#chi) = 400 GeV, m(#phi) = 100 MeV")
legend4.AddEntry(background_MET,"P P > t t~ a")
legend4.Draw()

c4.Write()

############################
# lepton + neutrino delta phi
############################

signal_lepton_neutrino_delta_phi = input_root_file.Get("signal_lepton_neutrino_delta_phi")
background_lepton_neutrino_delta_phi = input_root_file.Get("background_lepton_neutrino_delta_phi")

signal_lepton_neutrino_delta_phi.SetLineColor(ROOT.kBlue)
background_lepton_neutrino_delta_phi.SetLineColor(ROOT.kRed)

c5 = ROOT.TCanvas("Lepton Neutrino Delta Phi ", "Lepton Neutrino Delta Phi", 600, 400)
c5.cd()

pad5 = ROOT.TPad("Pad5", "Pad5", 0.0, 0.0, 0.95, 0.95)
pad5.Draw()
pad5.cd()

signal_lepton_neutrino_delta_phi.Scale(1.0/signal_lepton_neutrino_delta_phi.Integral(0,10000))
background_lepton_neutrino_delta_phi.Scale(1.0/background_lepton_neutrino_delta_phi.Integral(0,10000))

th5 = ROOT.THStack("Lepton, Neutrino Delta Phi", "Lepton, Neutrino Delta Phi")
th5.Add(signal_lepton_neutrino_delta_phi)
th5.Add(background_lepton_neutrino_delta_phi)
th5.Draw("Hist nostack")

th5.GetXaxis().SetTitle("#Delta #phi ( l, #nu)")
th5.GetYaxis().SetTitle("a.u.")

legend5 = ROOT.TLegend(0.7, 0.6, .99, .7)
legend5.AddEntry(signal_lepton_neutrino_delta_phi,"m(#chi) = 500 GeV, m(#phi) = 100 MeV")
legend5.AddEntry(background_lepton_neutrino_delta_phi,"P P > t t~ a")
legend5.Draw()

c5.Write()

############################
# bottom + lepton delta phi
############################

signal_leptonic_bottom_lepton_delta_phi = input_root_file.Get("signal_leptonic_bottom_lepton_delta_phi")
background_leptonic_bottom_lepton_delta_phi = input_root_file.Get("background_leptonic_bottom_lepton_delta_phi")

signal_leptonic_bottom_lepton_delta_phi.SetLineColor(ROOT.kBlue)
background_leptonic_bottom_lepton_delta_phi.SetLineColor(ROOT.kRed)

c6 = ROOT.TCanvas("Bottom Lepton Delta Phi", "Bottom Lepton Delta Phi", 600, 400)
c6.cd()

pad6 = ROOT.TPad("Pad6", "Pad6", 0.0, 0.0, 0.95, 0.95)
pad6.Draw()
pad6.cd()

signal_leptonic_bottom_lepton_delta_phi.Scale(1.0/signal_leptonic_bottom_lepton_delta_phi.Integral(0,10000))
background_leptonic_bottom_lepton_delta_phi.Scale(1.0/background_leptonic_bottom_lepton_delta_phi.Integral(0,10000))

th6 = ROOT.THStack("'Leptonic' Bottom + Lepton Delta Phi", "'Leptonic' Bottom + Lepton Delta Phi")
th6.Add(signal_leptonic_bottom_lepton_delta_phi)
th6.Add(background_leptonic_bottom_lepton_delta_phi)
th6.Draw("Hist nostack")

th6.GetXaxis().SetTitle("#Delta #phi ( b, l)")
th6.GetYaxis().SetTitle("a.u.")

legend6 = ROOT.TLegend(0.7, 0.6, .99, .7)
legend6.AddEntry(signal_leptonic_bottom_lepton_delta_phi,"m(#chi) = 500 GeV, m(#phi) = 100 MeV")
legend6.AddEntry(background_leptonic_bottom_lepton_delta_phi,"P P > t t~ a")
legend6.Draw()

c6.Write()

############################
# bottom + neutrino delta phi
############################

signal_leptonic_bottom_neutrino_delta_phi = input_root_file.Get("signal_leptonic_bottom_neutrino_delta_phi")
background_leptonic_bottom_neutrino_delta_phi = input_root_file.Get("background_leptonic_bottom_neutrino_delta_phi")

signal_leptonic_bottom_neutrino_delta_phi.SetLineColor(ROOT.kBlue)
background_leptonic_bottom_neutrino_delta_phi.SetLineColor(ROOT.kRed)

c7 = ROOT.TCanvas("Bottom Neutrino Delta Phi", "Bottom Neutrino Delta Phi", 600, 400)
c7.cd()

pad7 = ROOT.TPad("Pad7", "Pad7", 0.0, 0.0, 0.95, 0.95)
pad7.Draw()
pad7.cd()

signal_leptonic_bottom_neutrino_delta_phi.Scale(1.0/signal_leptonic_bottom_neutrino_delta_phi.Integral(0,10000))
background_leptonic_bottom_neutrino_delta_phi.Scale(1.0/background_leptonic_bottom_neutrino_delta_phi.Integral(0,10000))

th7 = ROOT.THStack("'Leptonic' Bottom + Neutrino Delta Phi", "'Leptonic' Bottom + Neutrino Delta Phi")
th7.Add(signal_leptonic_bottom_neutrino_delta_phi)
th7.Add(background_leptonic_bottom_neutrino_delta_phi)
th7.Draw("Hist nostack")

th7.GetXaxis().SetTitle("#Delta #phi ( b, #nu)")
th7.GetYaxis().SetTitle("a.u.")

legend7 = ROOT.TLegend(0.7, 0.6, .99, .7)
legend7.AddEntry(signal_leptonic_bottom_neutrino_delta_phi,"m(#chi) = 500 GeV, m(#phi) = 100 MeV")
legend7.AddEntry(background_leptonic_bottom_neutrino_delta_phi,"P P > t t~ a")
legend7.Draw()

c7.Write()

############################
# fully merged leptonic bottom pt 
############################

Signal_fully_merged_leptonic_bottom_pt = input_root_file.Get("Signal_fully_merged_leptonic_bottom_pt")
Background_fully_merged_leptonic_bottom_pt = input_root_file.Get("Background_fully_merged_leptonic_bottom_pt")

Signal_fully_merged_leptonic_bottom_pt.SetLineColor(ROOT.kBlue)
Background_fully_merged_leptonic_bottom_pt.SetLineColor(ROOT.kRed)

c8 = ROOT.TCanvas("Fully Merged Leptonic Bottom Pt", "Fully Merged Leptonic Bottom Pt", 600, 400)
c8.cd()

pad8 = ROOT.TPad("Pad8", "Pad8", 0.0, 0.0, 0.95, 0.95)
pad8.Draw()
pad8.cd()

Signal_fully_merged_leptonic_bottom_pt.Scale(1.0/Signal_fully_merged_leptonic_bottom_pt.Integral(0,10000))
Background_fully_merged_leptonic_bottom_pt.Scale(1.0/Background_fully_merged_leptonic_bottom_pt.Integral(0,10000))

th8 = ROOT.THStack("Fully Merged 'Leptonic' Bottom Pt", "Fully Merged 'Leptonic' Bottom Pt")
th8.Add(Signal_fully_merged_leptonic_bottom_pt)
th8.Add(Background_fully_merged_leptonic_bottom_pt)
th8.Draw("Hist nostack")

th8.GetXaxis().SetTitle("Bottom p_{T} (GeV)")
th8.GetYaxis().SetTitle("a.u.")

legend8 = ROOT.TLegend(0.7, 0.6, .99, .7)
legend8.AddEntry(Signal_fully_merged_leptonic_bottom_pt,"m(#chi) = 500 GeV, m(#phi) = 100 MeV")
legend8.AddEntry(Background_fully_merged_leptonic_bottom_pt,"P P > t t~ a")
legend8.Draw()

c8.Write()

############################
# partially merged leptonic bottom pt 
############################

Signal_partially_merged_leptonic_bottom_pt = input_root_file.Get("Signal_partially_merged_leptonic_bottom_pt")
Background_partially_merged_leptonic_bottom_pt = input_root_file.Get("background_partially_merged_leptonic_bottom_pt")

Signal_partially_merged_leptonic_bottom_pt.SetLineColor(ROOT.kBlue)
Background_partially_merged_leptonic_bottom_pt.SetLineColor(ROOT.kRed)

c9 = ROOT.TCanvas("Partially Merged Leptonic Bottom Pt", "Partially Merged Leptonic Bottom Pt", 600, 400)
c9.cd()

pad9 = ROOT.TPad("Pad9", "Pad9", 0.0, 0.0, 0.95, 0.95)
pad9.Draw()
pad9.cd()

Signal_partially_merged_leptonic_bottom_pt.Scale(1.0/Signal_partially_merged_leptonic_bottom_pt.Integral(0,10000))
Background_partially_merged_leptonic_bottom_pt.Scale(1.0/Background_partially_merged_leptonic_bottom_pt.Integral(0,10000))

th9 = ROOT.THStack("Partially Merged 'Leptonic' Bottom Pt", "Partially Merged 'Leptonic' Bottom Pt")
th9.Add(Signal_partially_merged_leptonic_bottom_pt)
th9.Add(Background_partially_merged_leptonic_bottom_pt)
th9.Draw("Hist nostack")

th9.GetXaxis().SetTitle("Bottom p_{T} (GeV)")
th9.GetYaxis().SetTitle("a.u.")

legend9 = ROOT.TLegend(0.7, 0.6, .99, .7)
legend9.AddEntry(Signal_partially_merged_leptonic_bottom_pt,"m(#chi) = 500 GeV, m(#phi) = 100 MeV")
legend9.AddEntry(Background_partially_merged_leptonic_bottom_pt,"P P > t t~ a")
legend9.Draw()

c9.Write()

############################
# Not merged leptonic bottom pt 
############################

Signal_not_merged_leptonic_bottom_pt = input_root_file.Get("Signal_not_merged_leptonic_bottom_pt")
Background_not_merged_leptonic_bottom_pt = input_root_file.Get("background_not_merged_leptonic_bottom_pt")

Signal_not_merged_leptonic_bottom_pt.SetLineColor(ROOT.kBlue)
Background_not_merged_leptonic_bottom_pt.SetLineColor(ROOT.kRed)

c10 = ROOT.TCanvas("Not Merged Leptonic Bottom Pt", "Not Merged Leptonic Bottom Pt", 600, 400)
c10.cd()

pad10 = ROOT.TPad("Pad10", "Pad10", 0.0, 0.0, 0.95, 0.95)
pad10.Draw()
pad10.cd()

Signal_not_merged_leptonic_bottom_pt.Scale(1.0/Signal_not_merged_leptonic_bottom_pt.Integral(0,10000))
Background_not_merged_leptonic_bottom_pt.Scale(1.0/Background_not_merged_leptonic_bottom_pt.Integral(0,10000))

th10 = ROOT.THStack("Not Merged 'Leptonic' Bottom Pt", "Not Merged 'Leptonic' Bottom Pt")
th10.Add(Signal_not_merged_leptonic_bottom_pt)
th10.Add(Background_not_merged_leptonic_bottom_pt)
th10.Draw("Hist nostack")

th10.GetXaxis().SetTitle("Bottom p_{T} (GeV)")
th10.GetYaxis().SetTitle("a.u.")

legend10 = ROOT.TLegend(0.7, 0.6, .99, .7)
legend10.AddEntry(Signal_not_merged_leptonic_bottom_pt,"m(#chi) = 500 GeV, m(#phi) = 100 MeV")
legend10.AddEntry(Background_not_merged_leptonic_bottom_pt,"P P > t t~ a")
legend10.Draw()

c10.Write()

############################
# fully merged bottom dijet pt 
############################

Signal_fully_merged_bottom_dijet_pt = input_root_file.Get("Signal_fully_merged_bottom_dijet_pt")
background_fully_merged_bottom_dijet_pt = input_root_file.Get("background_fully_merged_bottom_dijet_pt")

Signal_fully_merged_bottom_dijet_pt.SetLineColor(ROOT.kBlue)
background_fully_merged_bottom_dijet_pt.SetLineColor(ROOT.kRed)

c11 = ROOT.TCanvas("Fully Merged Bottom Dijet Pt", "Fully Merged Bottom Dijet Pt", 600, 400)
c11.cd()

pad11 = ROOT.TPad("Pad11", "Pad11", 0.0, 0.0, 0.95, 0.95)
pad11.Draw()
pad11.cd()

Signal_fully_merged_bottom_dijet_pt.Scale(1.0/Signal_fully_merged_bottom_dijet_pt.Integral(0,10000))
background_fully_merged_bottom_dijet_pt.Scale(1.0/background_fully_merged_bottom_dijet_pt.Integral(0,10000))

th11 = ROOT.THStack("Fully Merged Bottom Dijet Pt", "Fully Merged Bottom Dijet Pt")
th11.Add(Signal_fully_merged_bottom_dijet_pt)
th11.Add(background_fully_merged_bottom_dijet_pt)
th11.Draw("Hist nostack")

th11.GetXaxis().SetTitle("Bottom Dijet p_{T} (GeV)")
th11.GetYaxis().SetTitle("a.u.")

legend11 = ROOT.TLegend(0.7, 0.6, .99, .7)
legend11.AddEntry(Signal_fully_merged_bottom_dijet_pt,"m(#chi) = 500 GeV, m(#phi) = 100 MeV")
legend11.AddEntry(background_fully_merged_bottom_dijet_pt,"P P > t t~ a")
legend11.Draw()

c11.Write()





input_root_file.Purge()
input_root_file.Close()
output_root_file.Close()

