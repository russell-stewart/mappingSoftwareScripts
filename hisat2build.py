#hisat2build.py
#Russell O. Stewart
#7/27/2017
#Builds hisat2 indexes needed to run hisat2 mapping. These index files also
#incorporate haplotypes and SNPs.
#Make sure you have converted your dbSNP file into hisat's snp format using
#hisat2_extract_snps_haplotypes_UCSC.py (part of HISAT2) BEFORE running this!
#note: index files will appear in the directory in which you run this script!
#preferably, run this inside of the hisat2 directory itself
#if you plan to use SNP/haplotype files, make sure to use at least 200 Gb of
#memory! If not, 8 Gb will suffice.
#hisat2 is available from:
#https://github.com/infphilo/hisat2
import os
import subprocess

email = 'russells98@gmail.com'#email for openlava output
pathToHisat2 = '/Seibold/proj/Russell_playground/hisat2/hisat2-2.1.0'#where your hisat2 dierectory is stored

threads = 12#how many threads are available to run this on?
genomeFastaFile = '/data/reference/iGenomes/Homo_sapiens/UCSC/hg38/Sequence/WholeGenomeFasta/genome.fa'#path to the fasta file
baseName = 'Homo_sapiens_index_with_SNP'#what do you want to name the index files?

snpFile = '/Seibold/proj/Russell_playground/hisat2/hisat2SNPFiles/SNP144_common.snp'#path to SNPs, in HISAT2's format, .snp
haplotypeFile = '/Seibold/proj/Russell_playground/hisat2/hisat2SNPFiles/SNP144_common.haplotype'#same but .haplotype for haplotype

indexBuildCommand = "bsub -u %s -R \"rusage[mem=250000]\" -m f01 '%s/hisat2-build' -f -p %d --snp %s  --haplotype %s %s %s" % (email , pathToHisat2 , threads , snpFile , haplotypeFile , genomeFastaFile  , baseName)

coreID = subprocess.check_output(indexBuildCommand , shell = True)
print indexBuildCommand
print coreID
