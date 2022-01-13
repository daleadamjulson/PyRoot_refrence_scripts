import argparse, sys, numpy

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", dest="input", nargs="+", help="The input file(s)")
parser.add_argument("-c", "--cut_level", dest="cut_level", help="Cut level")
args = parser.parse_args()

if args.input == None:
    print("Please provide input log.txt files, exiting program.")
    sys.exit()
else:
    print("input file(s) is: "+str(args.input))

def sum_together(item1,item2):
    total = item1 + item2
    return total

def square(item1,item2):
    total = numpy.sqrt(item1**2+item2**2)
    return total
        
def open_file(file_name, cut_level):

    return_list = []
    with open(file_name,"r") as input_file:
        raw_input = input_file.readlines()
        for elem in raw_input:
            if str(cut_level) in elem:
                return_list.append(elem)
                return return_list
        print("Cut level not found.")
        sys.exit()

def split_info(list1):
    split_list = list1[0].split("\\\\")
    del split_list[-1]
    split_list = split_list[0].split("&")
    del split_list[0]
    return split_list

def get_processes():
    with open (args.input[0],"r") as input_file:
        lines = input_file.readlines()
        split_lines = lines[2].split("&")
        del split_lines[0]
        del split_lines[-1]
        split_lines.append("t#bar{t}")
        return split_lines

process_names = get_processes()
#print(process_names)
large_list = []
large_list.append(process_names)
data_list = []

for files in args.input:
    
    info = open_file(files, args.cut_level)
    new_list = split_info(info)
    large_list.append(new_list)
    data_list.append(new_list)
    
transposed_list = list(map(list, zip(*large_list)))

for elem1 in transposed_list:
    print(elem1[0]+" & "+elem1[1]+" & "+elem1[2]+" & "+elem1[3]+" \\\\")

del data_list[0][0]
del data_list[1][0]
del data_list[2][0]

final_total_MC = []
final_total_err = []

for i in data_list:
    total_MC = 0
    total_err = 0
    for j in i:
        total_MC = sum_together(total_MC,float(j.split("$\\pm$")[0]))
        total_err = square(total_err,float(j.split("$\\pm$")[1]))
    final_total_MC.append(round(total_MC,1))
    final_total_err.append(round(total_err,1))
    
print("Total MC & "+str(final_total_MC[0])+" $\\pm$ "+str(final_total_err[0])+" & "+str(final_total_MC[1])+" $\\pm$ "+str(final_total_err[1])+" & "+str(final_total_MC[2])+" $\\pm$ "+str(final_total_err[2]))
