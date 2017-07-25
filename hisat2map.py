import os
import time
import subprocess

#make sure to update these!!!
pathToHisat2 = '/Seibold/proj/Russell_playground/hisat2/hisat2-2.1.0'
srcDir = '/Seibold/proj/Russell_playground/skewer'
destDir = '/Seibold/proj/Russell_playground/hisat2'
runThreadN = 12
hisatIndexNamePrefix = 'Homo_sapiens_index'
email = 'russells98@gmail.com'
gtfFile='/data/reference/iGenomes/Homo_sapiens/UCSC/hg38/Annotation/Genes/genes.gtf'

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
    samfile = open(sampleDestDir[i] + '/' + tempName + '_SAM_out.sam'  , 'w')
    samfile.write('')
    samfile.close()
    i += 1

#run HISAT2 for each sample
j = 0
for sample in samples:
    command = "bsub -u %s -R \"rusage[mem=6000]\" '%s/hisat2 -q -t -p %d -x %s -1 %s -2 %s -S %s'" % (email , pathToHisat2 , runThreadN , pathToHisat2 + '/' + hisatIndexNamePrefix , srcDir + '/' + sample[0] , srcDir + '/' + sample[1] , sampleDestDir[j] + '/' + sample[1][:sample[1].find('/')]  + '_SAM_out.sam')
    print command + '\n'
    coreID = subprocess.check_output(command , shell=True)
    print coreID
    j += 1
    time.sleep(3)
