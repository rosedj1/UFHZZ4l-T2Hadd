import os,argparse,glob

def makedirs(dir):
    if not os.path.exists(dir):
        os.makedirs(os.path.abspath(dir))

#inputDir = "/cms/data/store/user/dsperka/UFHZZAnalysisRun2/MC2017_M19_Feb19_fixGENjet_bestCandLegacy/"
#outputDir = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC2017_M19_Feb19_fixGENjet_bestCandLegacy/"

inputDir = "/cms/data/store/user/dsperka/UFHZZAnalysisRun2/MC2018_M19_Feb19_fixGENjet_bestCandLegacy/"
outputDir = "/cms/data/store/user/t2/users/rosedj1/Higgs/HZZ4l/NTuple/Run2/MC2018_M19_Mar5_3l_2018Jets_bestCandLegacy/"

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
