import os
import subprocess

#note: index files will appear in the directory in which you run this script!

email = 'russells98@gmail.com'#email for openlava output
pathToHisat2 = '/Seibold/proj/Russell_playground/hisat2/hisat2-2.1.0'#where your hisat2 dierectory is stored

threads = 12#how many threads are available to run this on?
genomeFastaFile = '/data/reference/iGenomes/Homo_sapiens/UCSC/hg38/Sequence/WholeGenomeFasta/genome.fa'#path to the fasta file
baseName = 'Homo_sapiens_index_with_dbSNP'#what do you want to name the index files?

dbSNPFile = '/data/reference/iGenomes/Homo_sapiens/UCSC/hg38/Annotation/Variation/dbSNP146_common.txt'#path to SNPs, in dbSNP format.
snpBaseFilename = 'dbSNP146_common'

dbSNPToHisatFormatCommand = "bsub -u %s -R \"rusage[mem=30000]\" 'python %s/hisat2_extract_snps_haplotypes_UCSC.py %s %s %s'" %(g)

indexBuildCommand = "bsub -u %s -R \"rusage[mem=30000]\" '%s/hisat2-build' -f -p %d --snp %s %s %s" % (email , pathToHisat2 , threads , dbSNPFile , genomeFastaFile , baseName)

coreID = subprocess.check_output(indexBuildCommand , shell = True)
print coreID
