#star_map.py
#Russell Stewart
#7/14/2017
#Calls STAR to map a set of fastq files given STAR has already generated
#genome indexes.
#If you haven't made genome indexes yet, make sure to run
#star_generate_genome_indexes.sh
#STARAlinger can be found at:
#https://github.com/alexdobin/STAR

import os
import time
import subprocess

#make sure to update these!!!
srcDir = '/Seibold/proj/Russell_playground/skewer'
destDir = '/Seibold/proj/Russell_playground/starAligner'
runThreadN = 12
genomeDir = '/Seibold/proj/Russell_playground/starAligner/genomeDir'
email = 'russells98@gmail.com'

#makes and returns a new directory with given directory path and name of dir
def mkDir(path , name):
    newDir = os.path.join(path , name)
    if not os.path.isdir(newDir):
        os.makedirs(newDir)
    return(newDir)

folders = os.listdir(srcDir)
mkDir(destDir , 'STARResults')

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
    sampleDestDir.append(destDir + '/STARResults/' + tempName)
    i += 1

#run STAR for each sample
j = 0
for sample in samples:
    command = "bsub -u %s -R \"rusage[mem=30000]\" '/Seibold/proj/Russell_playground/starAligner/STAR/source/STAR --runThreadN %d --genomeDir %s --readFilesIn %s %s --outFileNamePrefix %s --readFilesCommand zcat  --outSAMtype BAM Unsorted'" % (email , runThreadN , genomeDir , srcDir + '/' + sample[0] , srcDir + '/' + sample[1] , sampleDestDir[j])
    print command + '\n'
    coreID = subprocess.check_output(command , shell=True)
    print coreID
    j += 1
    time.sleep(3)
