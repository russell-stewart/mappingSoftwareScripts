#hisat_map.py
#Russell O. Stewart
#7/18/2017
#Executes HISAT mapping software for trimmed fastq files (outputted by skewer)
#Before running this, make sure that you have built a HISAT index:
#/path/to/hisat/directory/hisat-build -f /data/reference/iGenomes/Homo_sapiens/UCSC/hg38/Sequence/WholeGenomeFasta/genome.fa Homo_sapiens
#HISAT reference manual:
#http://ccb.jhu.edu/software/hisat/manual.shtml
#Download HISAT on Github:
#https://github.com/infphilo/hisat.git
import os
import time
import subprocess

#make sure to update these!!!
srcDir = '/Seibold/proj/Russell_playground/skewer'
destDir = '/Seibold/proj/Russell_playground/hiSatAligner'
runThreadN = 12
hisatIndexNamePrefix = 'Homo_sapiens'
email = 'russells98@gmail.com'
gtfFile='/data/reference/iGenomes/Homo_sapients/UCSC/hg38/Annotation/Genes/genes.gtf'

#makes and returns a new directory with given directory path and name of dir
def mkDir(path , name):
    newDir = os.path.join(path , name)
    if not os.path.isdir(newDir):
        os.makedirs(newDir)
    return(newDir)

folders = os.listdir(srcDir)
hisatResultsDir = mkDir(destDir , 'hisatResults')

#find the trimmed fastq files and turn them into a vector of samples.
#this uses the file heirarchy outputted by skewer.
samples = []
sampleDestDir = []
i = 0
for folder in folders:
    files = os.listdir(srcDir + '/' + folder)
    samples.append([])
    for f in files:
        if not f.find('untrimmed') > 0 and f.find('.fastq.gz') > 0:
            samples[i].append(folder + '/' + f)
            tempName = f[:f.find('-trimmed')]
    sampleDestDir.append(mkDir(hisatResultsDir , tempName))
    i += 1

#run HISAT for each sample
j = 0
for sample in samples:
    command = "bsub -u %s -R \"rusage[mem=30000]\" '/Seibold/proj/Russell_playground/hiSatAligner/hisat/hisat -q -t -p %d --known-splicesite-infile %s -x %s -1 %s -2 %s -S %s'" % (email , runThreadN , gtfFile , hisatIndexNamePrefix , srcDir + '/' + sample[0] , srcDir + '/' + sample[1] , sampleDestDir[j] + '/' + sample[0][:sample[0].find('trimmed')] + '_SAM_out.sam')
    print command + '\n'
    coreID = subprocess.check_output(command , shell=True)
    print coreID
    j += 1
    time.sleep(3)
