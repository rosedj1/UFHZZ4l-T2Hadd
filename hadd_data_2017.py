import os,argparse,glob

def makedirs(dir):
    if not os.path.exists(dir):
        os.makedirs(os.path.abspath(dir))

#inputDir = "/cms/data/store/user/muahmad/2018data/UFHZZAnalysisRun2/Data2018ABCD_v1/"
inputDir = "/cms/data/store/user/klo/DarkPhoton_Moriond17_NTuple/ZXData_Early2017/"
outputDir = "/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/ZPlusX_Early2017_v1/"

pdNames = glob.glob(inputDir+"*/")

for pdDir in pdNames:
    if "SingleMuon" in pdDir: continue
    pdName = pdDir.split("/")[-2]
    makedirs(os.path.join(outputDir,pdName))
    for crabDir in glob.glob(pdDir+"*/"):
        dataset_name = crabDir.split("/")[-2].replace("crab_","")
        cmd = "hadd -f "+os.path.join(outputDir,pdName,dataset_name+".root")+" "+crabDir+"*/*/*.root"
        #print cmd
        #print "hadd -f "+os.path.join(outputDir,pdName,dataset_name+".root")
        os.system(cmd)
