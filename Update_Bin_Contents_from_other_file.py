import ROOT


root_file = ROOT.TFile.Open("scalefactorsPUID_81Xtraining.root","UPDATE")

# f.ls(option="-d") #Will get the entire list contents
# e = f.GetDirectory("/") #Will return directory contents

first_bin_contents = []

second_bin_contents = []

third_bin_contents = []

fourth_bin_contents = []

def get_bin_contents(histo, root_file, list):
	opened_histo = root_file.Get(histo)
	x_bins = opened_histo.GetNbinsX()
	y_bins = opened_histo.GetNbinsY()
	for i in range(x_bins):
		for j in range(y_bins):
			bin_content = opened_histo.GetBinContent((i+1),(j+1))
			list.append([i+1,j+1,bin_content])

# def write_to_bins(histo, root_file, x, y, bin_content):
# 	opened_histo = root_file.Get(histo)
# 	print(histo+" will have "+str(bin_content)+" written to ("+str(x)+","+str(y)+")")
# 	opened_histo.SetBinContent(x,y,bin_content)
# 	opened_histo.Write()

def write_contents_to(first_list, second_list, target_histo):
	opened_histo = root_file.Get(target_histo)
	for i in range(len(first_list)):
		updated_value = first_list[i][2] - second_list[i][2]
		x = first_list[i][0]
		y = first_list[i][1]
		opened_histo.SetBinContent(x, y, updated_value)
		opened_histo.Write()

root_keys = root_file.GetListOfKeys()

for key in root_keys:
	key_obj = key.ReadObj()
	histo_name = key_obj.GetName()

get_bin_contents("h2_eff_sf2016_T", root_file, first_bin_contents)

get_bin_contents("h2_eff_sf2016_T_Systuncty", root_file, second_bin_contents)

write_contents_to(first_bin_contents, second_bin_contents, "h2_eff_sf2016_T")

get_bin_contents("h2_mistag_sf2016_T", root_file, third_bin_contents)

get_bin_contents("h2_mistag_sf2016_T_Systuncty", root_file, fourth_bin_contents)

write_contents_to(third_bin_contents, fourth_bin_contents, "h2_mistag_sf2016_T")

# root_file.Write()
root_file.Purge()
root_file.Close()

