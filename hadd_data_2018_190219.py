import os,argparse,glob

def makedirs(dir):
    if not os.path.exists(dir):
        os.makedirs(os.path.abspath(dir))

inputDir = "/cms/data/store/user/klo/HZZ4l/ZXData_Run2018/"
outputDir = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/ZXData_Run2018/"

pdNames = glob.glob(inputDir+"/")

makedirs(os.path.join(outputDir,))
for crabDir in glob.glob(inputDir+"*/"):
    for datasetDir in glob.glob(crabDir+"*/"):
        if "SingleMuon_Run2018D-PromptReco-v2" not in datasetDir: continue
        outFileName = datasetDir.split("/")[-2].replace("crab_","")
        cmd = "hadd -f -k "+os.path.join(outputDir,outFileName+".root")+" "+datasetDir+"*/*/*.root"
        print "="*50
        print cmd
        #os.system(cmd)
