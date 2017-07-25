import os
import subprocess

#note: index files will appear in the directory in which you run this script!

email = 'russells98@gmail.com'
pathToHisat2 = '/Seibold/proj/Russell_playground/hisat2-2.1.0/'

threads = 12
genomeFastaFile = '/data/reference/iGenomes/Homo_sapiens/UCSC/hg38/Sequence/WholeGenomeFasta/genome.fa'
baseName = 'Homo_sapiens_index'

indexBuildCommand = "bsub -u %s -R \"rusage[mem=30000]\" '%s/hisat2-build' -f -p %d %s %s" % (email , pathToHisat2 , threads , genomeFastaFile , baseName)

coreID = subprocess.check_output(indexBuildCommand , shell = True)
print coreID
