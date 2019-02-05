import os,argparse,glob

def makedirs(dir):
    if not os.path.exists(dir):
        os.makedirs(os.path.abspath(dir))

#inputDir = "/cms/data/store/user/dsperka/UFHZZAnalysisRun2/MC2018_M19_Feb1_noCorrections/"
#outputDir = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC2018_M19_Feb1_noCorrections/"

inputDir = "/cms/data/store/user/dsperka/UFHZZAnalysisRun2/MC2018_M19_Feb1_noCorrections_bestCandLegacy/"
outputDir = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC2018_M19_Feb1_noCorrections_bestCandLegacy/"

pdNames = glob.glob(inputDir+"/")

for pdDir in pdNames:
    pdName = pdDir.split("/")[-2]
    makedirs(os.path.join(outputDir,pdName))
    for crabDir in glob.glob(pdDir+"*/"):
        dataset_name = crabDir.split("/")[-2].replace("crab_","")
        cmd = "hadd -f "+os.path.join(outputDir,pdName,dataset_name+".root")+" "+crabDir+"*/*/*/*.root"
        print "="*50
        print cmd
        os.system(cmd)
