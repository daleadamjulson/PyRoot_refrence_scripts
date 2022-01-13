import ROOT
import matplotlib.pyplot as plt
import numpy as np

root_file_1 = ROOT.TFile.Open("PUjetID_No_Weights.root","READ")

root_keys_1 = root_file_1.GetListOfKeys()

# print(type(root_keys_1))

# file_1_folder_list = []

for key in root_keys_1:
	key_obj = key.ReadObj()
	folder_name = key_obj.GetName()
	# file_1_folder_list.append(folder_name)

# print(file_1_folder_list)

root_file_1.cd("NDiJetCombinations")

# root_keys_2 = root_file_1.GetListOfKeys()

# for key in root_keys_2:
# 	key_obj = key.ReadObj()
# 	folder_name = key_obj.GetName()
# 	file_1_folder_list.append(folder_name)

# print(file_1_folder_list)

canvas_1 = root_file_1.Get("NDiJetCombinations/FirstLeadingJetEta")

# list_1 = canvas_1.GetListOfPrimitives()

# for name in list_1:
# 	print(name.GetName())
# 	print(type(name))

top_1 = canvas_1.GetPrimitive("top")

# top_list = top.GetListOfPrimitives()

# print("Top list: ")
# for name in top_list:
# 	print(name.GetName())
# 	print(type(name))

MC_histos_1 = top_1.GetPrimitive("FirstLeadingJetEta")

# MC_list = MC_histos.ls()
MC_sum_1 = MC_histos_1.GetStack().Last()

number_of_bins_1 = MC_sum_1.GetNbinsX()

PU_Jet_No_Weights = []

for i in range(number_of_bins_1+1):
	bin_content = MC_sum_1.GetBinContent(i)
	# print("Bin "+str(i)+" has: "+str(bin_content))
	PU_Jet_No_Weights.append(bin_content)

root_file_1.Close()

######### 2nd root file #########

root_file_2 = ROOT.TFile.Open("PUJetID_with_Weights.root","READ")

root_keys_2 = root_file_2.GetListOfKeys()

for key in root_keys_2:
	key_obj = key.ReadObj()
	folder_name = key_obj.GetName()

root_file_2.cd("NDiJetCombinations")

canvas_2 = root_file_2.Get("NDiJetCombinations/FirstLeadingJetEta")

top_2 = canvas_2.GetPrimitive("top")

MC_histos_2 = top_2.GetPrimitive("FirstLeadingJetEta")

MC_sum_2 = MC_histos_2.GetStack().Last()

number_of_bins_2 = MC_sum_2.GetNbinsX()

PU_Jet_With_Weights = []

for i in range(number_of_bins_2+1):
	bin_content = MC_sum_2.GetBinContent(i)
	# print("Bin "+str(i)+" has: "+str(bin_content))
	PU_Jet_With_Weights.append(bin_content)

ratio = []
event_diff = []

for i, j in zip(PU_Jet_No_Weights, PU_Jet_With_Weights):
	if i == 0.0:
		ratio.append(1)
	# elif (j/i) > 5 :
	# 	ratio.append(1)
	else:
		ratio.append(j/i)
	event_diff.append(j-i)

# for i in range(len(ratio)):
# 	print("Bin "+str(i)+" has ratio: "+str(ratio[i]))

# x_points = list(range(len(ratio)))
x_points = np.linspace(-5,5,101)
list(x_points.tolist())

print(ratio)
# del x_points[0]
# del ratio[0]

# plt.scatter(x_points, event_diff)
# plt.show()

plt.scatter(x_points, ratio)
plt.axhline(y=1.0, color='r', linestyle='-')
plt.suptitle("Ratio of with Weights to No Weights in FirstLeadingJetEta")
plt.show()


# max_content = MC_sum.GetMaximum()
# print(max_content)

# print("MC histos list: ")
# for name in MC_list:
# 	print(name.GetName())
# 	print(type(name))

# bottom = canvas_1.GetPrimitive("bottom")

# bottom_list = bottom.GetListOfPrimitives()

# print("Bottom list: ")
# for name in bottom_list:
# 	print(name.GetName())
# 	print(type(name))


# root_file.Purge()
root_file_2.Close()
