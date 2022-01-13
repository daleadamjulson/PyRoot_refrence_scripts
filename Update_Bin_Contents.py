import ROOT


root_file = ROOT.TFile.Open("scalefactorsPUID_81Xtraining.root","UPDATE")

# f.ls(option="-d") #Will get the entire list contents
# e = f.GetDirectory("/") #Will return directory contents

list_of_bin_contents = []

def zero_bin_finder(histo, root_file):
	list_of_zero_bins = []
	opened_histo = root_file.Get(histo)
	x_bins = opened_histo.GetNbinsX()
	y_bins = opened_histo.GetNbinsY()
	for i in range(x_bins):
		for j in range(y_bins):
			bin_content = opened_histo.GetBinContent((i+1),(j+1))
			if (bin_content == 0.0):
				print(histo+" has a 0 bin at "+str(i+1)+" and "+str(j+1))
				list_of_zero_bins.append([histo,(i+1),(j+1)])
			list_of_bin_contents.extend([(i+1),bin_content])
	if len(list_of_zero_bins) == 0: print(histo+" has no zero bins.")

def write_to_zero_bin(histo, root_file, x, y, bin_content):
	opened_histo = root_file.Get(histo)
	print(histo+" will have "+str(bin_content)+" written to ("+str(x)+","+str(y)+")")
	opened_histo.SetBinContent(x,y,bin_content)
	opened_histo.Write()

root_keys = root_file.GetListOfKeys()

histo_list = []

for key in root_keys:
	key_obj = key.ReadObj()
	histo_name = key_obj.GetName()
	histo_list.append(histo_name)

# print(histo_list)

for histo in histo_list:
	zero_bin = zero_bin_finder(histo, root_file)

# print(list_of_bin_contents)
# print(list_of_zero_bins)

# write_to_zero_bin("h2_mistag_mc2016_M",root_file,4,8,0.0645)
# write_to_zero_bin("h2_mistag_mc2016_M",root_file,5,9,0.0145)
# write_to_zero_bin("h2_mistag_mc2016_T",root_file,5,4,0.01956752)
# write_to_zero_bin("h2_mistag_mc2016_T",root_file,5,9,0.02661092)
# write_to_zero_bin("h2_mistag_mc2017_T",root_file,5,7,0.0909)
# write_to_zero_bin("h2_mistag_mc2017_T",root_file,5,8,0.0172)

for histo in histo_list:
	zero_bin = zero_bin_finder(histo, root_file)

# print(histo_list)

# root_file.Write()
root_file.Purge()
root_file.Close()

