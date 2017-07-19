#! /bin/sh
#star_generate_genome_indexes.sh
#Russell Stewart
#7/14/2017
#Generates the genome indexes files needed to use STARAligner, a package of
#genome mapping software.
#STARAlinger can be found at:
#https://github.com/alexdobin/STAR

#how many cores are on your server node?
NUMBER_OF_THREADS="12"
#where can STAR store 100 gigabytes of genome indexes? actually make this directory.
GENOME_DIR="/Seibold/proj/Russell_playground/starAligner/genomeDir"
#the filepath to the reference genome you want to use
GENOME_FASTA_FILE="/data/reference/iGenomes/Homo_sapiens/UCSC/hg38/Sequence/WholeGenomeFasta/genome.fa"
#the filepath to the annotations you want to use
GTF_FILE="/data/reference/iGenomes/Homo_sapients/UCSC/hg38/Annotation/Genes/genes.gtf"
# should equal (read length) - 1
SJDB_OVERHANG="99"

bsub /Seibold/proj/Russell_playground/starAligner/STAR/source/STAR --runThreadN $NUMBER_OF_THREADS --runMode genomeGenerate --genomeDir $GENOME_DIR --genomeFastaFiles $GENOME_FASTA_FILE --sjdbGTFfile $GTF_FILE --sjdbOverhang $SJDB_OVERHANG
