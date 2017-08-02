# mappingSoftwareScripts
Simple scripts for pipeline interaction with RNA-Seq mapping software

## Mapping Software Packages Supported
- HISAT: [https://github.com/infphilo/hisat.git]
- HISAT2: [https://github.com/infphilo/hisat2]
- STAR: [https://github.com/alexdobin/STAR]

##Files

### HISAT
- **hisat_map.py**: Batch runs HISAT mapping software for a set of trimmed fastq files outputted from skewer

### HISAT2
- **hisat2build.py**: Builds hisat2 indexes needed to run hisat2 mapping
- **hisat2map.py**: Batch runs HISAT2 mapping software for a set of trimmed fastq files outputted from skewer

### STAR
- **star_generate_genome_indexes.sh**: Builds hisat2 indexes needed to run STAR mapping
- **star_map.py**: Batch runs STAR mapping software for a set of trimmed fastq files outputted from skewer
