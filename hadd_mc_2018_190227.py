#####################################################################################################
## PURPOSE: Hadd NTuples together.
## SYNTAX:  python <script.py>
## NOTES:   This code is pretty specific to a H-->ZdZd-->4lep (HToZdZd) naming scheme.
##          The User should have a look through 'Main' to make sure the correct files will be hadded.
##          Also check the User Parameters below.
## AUTHOR:  Jake Rosenzweig
## DATE:    2019-02-27
#####################################################################################################
import os,argparse,glob,subprocess,sys

def makedirs(dir):
    if not os.path.exists(dir):
        os.makedirs(os.path.abspath(dir))

#____________________________________________________________________________________________________
# User Parameters
inputDir    = "/cms/data/store/user/drosenzw/HToZdZd_NTuple/HToZdZd_UpTo0j_Eps1e-2/"
outputDir   = "/cms/data/store/user/t2/users/rosedj1/Higgs/HToZdZd/HToZdZd_NTuple/"

eps             = "1e-2"
genhaddedname   = "HToZdZd_UpTo0j_Eps"+eps+"_MZDMASS.root"

boolCheck       = 0 # First, check files to-be-hadded. Will exit program after checking.
#____________________________________________________________________________________________________
# Main

## Grab each mZd dir
mZdirlist = glob.glob(inputDir+"*/")

for mZdir in mZdirlist:

    mass            = mZdir.split('MZD')[1].split('_')[0]
    filestobehadded = glob.glob(mZdir + '/*/*/*/*.root')

    if (boolCheck):
        for each in filestobehadded:
            print each
        sys.exit()

    destfile = genhaddedname.replace('MASS',mass)
    makedirs( os.path.join(outputDir,destfile) )

    cmd = ['hadd', '-f'] + [outputDir+destfile] + filestobehadded
    print "="*50
    subprocess.call(cmd)
