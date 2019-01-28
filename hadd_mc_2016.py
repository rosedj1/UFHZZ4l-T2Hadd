import os,argparse,glob

def makedirs(dir):
    if not os.path.exists(dir):
        os.makedirs(os.path.abspath(dir))

#inputDir = "/cms/data/store/user/dsperka/UFHZZAnalysisRun2/MC80X_M17_4l_Feb21"
#outputDir = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_4l_Feb21/"

#inputDir = "/cms/data/store/user/dsperka/UFHZZAnalysisRun2/MC80X_M17_2l_Feb21/"
#outputDir = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_2l_Feb21/"

inputDir = "/cms/data/store/user/hmei/UFHZZAnalysisRun2/Data_80XM17_Feb21/"
outputDir = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/Data_80XM17_Feb21/"

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
