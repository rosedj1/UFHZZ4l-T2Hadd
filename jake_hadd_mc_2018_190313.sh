#!/bin/bash
#####################################################################################################
## PURPOSE: Hadd root files together, produced from UFHZZ Analyzer.
## SYNTAX:  ./<script.sh>  <dir_to_root_files>/  <output_dir>/
## NOTES:   Make sure that <dir_to_root_files> and <output_dir> both have the final `/` at the end.
##          Can also hadd together WplusH and WminusH files on command
## AUTHOR:  Jake Rosenzweig
## DATE:    2019-03-13, Happy birthday, Schwanger.
#####################################################################################################

#____________________________________________________________________________________________________
# Processes
DEBUG=0     # if DEBUG=1, files will NOT be hadded
TahirWH=0   # hadd WplusH and WminusH files together for Tahir

#____________________________________________________________________________________________________
# User Parameters
inDir=$1    # parent dir to all root files which will be hadded
outDir=$2   # dir to store hadded output file

#____________________________________________________________________________________________________
# Main
startDir=`pwd`
cd ${inDir}
dirNames=$(ls)

# make outDir if it doesn't yet exist
if [ ! -d ${outDir} ]; then
    mkdir -p ${outDir}
fi

# Either DEBUG or hadd files
for dirName in ${dirNames}; do
    
    if [ $DEBUG -eq 1 ]; then
        echo "looking in dir: ${dirName}"
        echo
        echo "Command:"
        echo "hadd -f ${outDir}${dirName}.root"  
        echo
        echo "Files to be hadded:"
        ls ${inDir}${dirName}/*/*/*/*.root
        echo 
        echo "Output file: ${outDir}${dirName}.root"
        echo 
    else 

        hadd -f ${outDir}${dirName}.root  ${inDir}${dirName}/*/*/*/*.root
        echo
    fi
done

cd ${startDir}

#____________________________________________________________________________________________________
# hadd WH files together for Tahir
if [ ${TahirWH} -eq 1 ]; then
    cd ${outDir}
    
    WHfile=$( echo $(ls WplusH*) | sed "s/plus//" )
    
    # or DEBUG
    if [ ${DEBUG} -eq 1 ]; then
        echo "These files would be hadded together for Tahir:"
        ls WplusH*.root WminusH*.root
        echo "Output file name: ${WHfile}"
    else
        hadd -f ${WHfile} WplusH*.root WminusH*.root
    fi
fi

cd ${startDir}
