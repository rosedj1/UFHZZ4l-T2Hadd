import os
import glob
import subprocess

verbose = 0

out_file = "/cms/data/store/user/t2/users/rosedj1/ForPeeps/ForChenguang/crab_DoubleEG_Run2016B-03Feb2017_fullyhadded.root"
base_path = "/cms/data/store/user/zewang/2018data/UFHZZAnalysisRun2/HZG_Data16/DoubleEG"

dir_list = [
"crab_DoubleEG_Run2016B-03Feb2017_ver2-v2/191228_090221/*/*.root",
"crab_DoubleEG_Run2016C-03Feb2017-v1/191228_090417/*/*.root",
"crab_DoubleEG_Run2016D-03Feb2017-v1/191228_090611/*/*.root",
"crab_DoubleEG_Run2016E-03Feb2017-v1/191228_090807/*/*.root",
"crab_DoubleEG_Run2016F-03Feb2017-v1/191228_091004/*/*.root",
"crab_DoubleEG_Run2016G-03Feb2017-v1/191228_091201/*/*.root",
"crab_DoubleEG_Run2016H-03Feb2017_ver3-v1/191228_091618/*/*.root",
]

total_file_list = []
for dir_k in dir_list:
    if (verbose): print "Searching through ", dir_k
    path_dir_k = os.path.join(base_path, dir_k)
    globbed_list = glob.glob(path_dir_k)
    if (verbose): print "globbed_list has size", len(globbed_list)
    total_file_list += globbed_list
    if (verbose): print "total_file_list has size", len(total_file_list), "\n"

skimmed_total_file_list = list(filter(lambda x : os.path.getsize(x) > 0, total_file_list))
if (verbose): 
    print "skimmed_total_file_list has size =", len(skimmed_total_file_list)
print "Files with 0B found:", len(total_file_list)-len(skimmed_total_file_list)

command_list = ['hadd', '-f'] + [out_file] + skimmed_total_file_list
if (verbose): 
    print "command to be run:", command_list
subprocess.call(command_list)
