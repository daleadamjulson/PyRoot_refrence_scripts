import sys, os
import ROOT as r

signs = ['OS', 'LS']
regions = ['Region1', 'Region2', 'Region3', 'Region4']

output_root_file = r.TFile.Open('2016_e_mu_LargestDiJetMass_histos.root','RECREATE')

def grab_plot(sign, region):
    
    #2016_e_mu/Region1/LS/output.root
    root_file = '2016_e_mu/'+region+'/'+sign+'/output.root'
    f = r.TFile.Open(root_file)
    histo = f.Get("NDiJetCombinations/LargestDiJetMass")

    output_root_file.cd()
    histo.SetName(sign+'_'+region+'_LargestDiJetMass')
    histo.Write()
    f.Close()

for i in signs:
    for j in regions:
        grab_plot(i, j)
