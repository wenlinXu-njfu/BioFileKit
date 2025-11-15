# Introduction
**BioFileKit: A Python command-line toolkit dedicated to simplifying the reading, writing, conversion, 
parsing and basic operations of various biological data file formats.**

# Install
```
pip install biofile-kit --upgrade
```

# Change log
## v0.1.0
- New
  - Fasta file tools ([fasta_tools](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/fasta_tools.py)):
    - [change hard masked to soft masked](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/fasta_utils/hardmasked_to_softmasked.py)
    - [telomere finder](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/fasta_utils/telomere_finder.py)
  - Gff file tools ([gff_tools](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/gff_tools.py)):
    - [Statistical analysis of GFF file](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/gff_utils/stats.py)
  - Genotype file tools ([gt_kit](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/gt_kit.py)):
    - [genotype consistency analysis](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/gt_utils/genotype_consistency_analysis.py)
    - [genotype file merging](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/gt_utils/merge.py)
    - [statistical analysis of SNP loci](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/gt_utils/stat_gt.py)
  - VCF file tools ([vcf_tools](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/vcf_tools.py)):
    - [convert the file format from VCF to Genotype (GT)](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/vcf_utils/vcf2gt.py)
- Modified
  - Null
- Deleted
  - Null

# Usage example
**All commands in the biofile_kit directory can type `-h` to see subcommands.**<br />
```shell
gff_tools -h
```
```
Usage: gff_tools [OPTIONS] COMMAND [ARGS]...

  Gff file tools.

Options:
  -V, --version  Show author and version information.
  -h, --help     Show this message and exit.

Commands:
  extract_seq          Extract sequences from GFF file.
  get_feature_density  Get feature density from GFF file.
  rename               This script provides a standardized feature ID...
  sort                 Sort naturally in sequence according to...
  stats                Summarize the information of various features in...
  to_bed               Convert the file format from GFF to BED.
  to_gtf               Convert the file format from GFF to GTF.
```
**All subcommands can also use `-h` to view the help documentation.**
```shell
gff_tools rename -h
```
```
Usage: gff_tools rename [OPTIONS] <gff file|stdin>

  This script provides a standardized feature ID renaming scheme for genome
  annotation files in GFF format. It creates species-specific, chromosome-
  locating, and structured unique identifiers for different types of genomic
  features in accordance with best practices in bioinformatics, ensuring
  consistency and traceability of IDs throughout the annotation file.

  1.genes：<species_name>.<chr_name>Gxxxxxx.<annotation_version>

  2.mRNAs: <species_name>.<chr_name>Gxxxxxx.x.<annotation_version>

  3.other features:
  <species_name>.<chr_name>Gxxxxxx.x.<feature_type>.x.<annotation_version>

Options:
  -s, --species-name <str>        Species name.  [required]
  -v, --anno-version <str>        Annotation version.  [default: v1.0]
  -n, --npartitions <int>         The number of partitions to distribute the
                                  data into for dask processing.  [default: 4]
  -o, --output-file <file|stdout>
                                  Output file, stdout by default.
  -V, --version                   Show author and version information.
  -h, --help                      Show this message and exit.
```

## Generate random nucleotide sequences
```shell
fasta_tools random_nucl -n seq1,seq2 -l 1000,1200
```
```
>seq1 length=1000
CGCCAGGCCTGCCCTGCGACGGAGGTTCCCCGTATGACTGCCCTATATCATTCCTGCTAAACTCAATCCACAAGATCAATTCACTCCGGGGAACAACTGCCACTAGAAACCGTAGGTTACCATCAATAGTTCCCCACTTGGAGGAAGAAGTCTTTGAAGCAGGTTGTCATCCAGCATTCTTTCTAAACGTCATTGGACATAGGGGTAAGCTCATATCCTCTCCCAACCATTCAGAAGTCCATGACCATGTCCGGTGCAAATTTGAAAGTCATGATGGTGAGGGAGCAAGAGAGCGCAGATCACGGATAAGTATTAAAAAGTGCTGTCGAGGCCGCAGTGGAAGTGACTAATTGGCTGATGCACGGACCTCCAGTGTACAGCTCATGTTTCAGGTGCGTCGGACTGTCAGTGACTCAATTTTCTGGGCCCAACTCCGCGTTCGGTGGATTAGTAACTATAGTGGTTGCATGAGGTACTGAGATTGAGCCGTGAAAAGCATTCAAAGTGCGGTTCCTCAACCTATTATTATTAAGACATAAGTTTGCTAGCGCTTTGTTGCAATCGTGTCGTGGAATGCGATTGATGCTTAGCAGTTTCCGGGAAGTACGGACTCATGCCGTTATGTGCGCCAACAAACAGCGCGTGTTTCATTTCGCGCCGGTCGCCTGGCGCGTGTTATGGGATCGCACTTCACCGTGCTGATATCGCTGAGGCGAGGGTTCCTCGAGATATTGGCTTGGCTCGCCAGGCAGTAGTCGTGGTCAGCCCGACTTGGCACGCTAAAGACGAGCCCACGTGCATTCGGTCGGAATCAGTTAGACGTCGAACGATTCGATCCAGCGTGAGGCCTATCCTTTGCCCATTTAACTCCGTATTCACGGTCTCCTTGATACATAGTGTACTTAGTGTTACCAGCGAACTCCGACGCGGACAGTGTCCTCGGAGTATTACCTCCAAAGAAATTCTCGGGCCGAACAGCGTAGTCTATACCGCCTGGGTG
>seq2 length=1200
ATAGGTGTAGTGTGTCTTCATCTTGATGTAAGTTCGTTCACCCAGATCTGCTAAAACGCATGGCATTTTTTTCGCATACGGTCCACTGGCACTATATGATTCCCAGTACTTCGCAGATTTGGGGGGGTAAGAGTCCGCGGAAGCGTTGTTCTGACGCGTACGCATGTTCGGTATTTTTTACGGGTGAGTTGCATCGGTTGTGTATTGGTCCATGTTAAGACGGTTATCGGGCAGGCTTCTCAATGCGGTGAGTCGGGAAGACACTAGCCAGCGAAATTATGTGATCGCTGGAATAGGATCGATGTAGCAACGACACTTTCCTGGCCTACAGACGGACTTGGACCGGATCAATCGTCTTATATAATAATACACGTCGCAGAACGGTCTGTGTATAGGACCGGTAGAATGAGTAGTTCATACTCCGGCCCGCAGGTACCCCTGTACGCATGAAAGTCCAAGCTCTCGCTGAACCGACACCTCTAGCCGAGGTACGTATGCATGACCTGGTTGTTCTCTTCGGGTCACGACAGTTGCCTATTTACGCTCGGATACCAGGAAACTTTGCCGGGAGTTCGCCCCCAGTAGTTCCCGGGTTGGGGTCGGGGTGTTCTGCCGATTACCGGATGTATCTCACCTGAGATTCAGCATCGGTGCGAACATCGTGAATCCTAAAGGTTGAACAAAGGAAGGCCTCCATGCGTTGGAAAGTCCTCGAAGTGGAGAAGTCTATCGTAGATCAACCGATAGGCAATGAAAAGAAAAAGCGCAACAGACGCCACGCTTCTAGATCGCAGTTGGCCTTTTAATGGCGAATCCATTTACCGAGCGAAGAAAAAGCCTGGCTAGCTTGTTTAAAACTGGTAACACTGAATCTCCGAAAGAGTAGCTATAGGCTCCCAGCACAGCCTGCGGCTGGCGCCAACGCCTAACGAAAATGCCAATCCACTTAGTTGTGTTAACTGTCTCCCCACTATATGCGGCTTACCAGGGAGTGTAATTTCTGGCGATGACCAGCGTTTCCTTTGGGTTCCGTCGAATTCCTTAGATCTAGGACAGCAGTTCGAATTACTTGGCGTGGTCGCATCAGGACTTCGCGTAGTGGCTATCCAGATCATAGACTGAGTCACGTATTTGACGCCAGACCTAAGACCCCACGATGGTTTCTAGTCGTAACTTGAGTGAGCTAGCTCGCCTCGTGTC
```

## ORF prediction
```shell
fasta_tools random_nucl -n seq1,seq2 -l 1000,1200 | fasta_tools ORF_finder -c -
```
```
>seq1 length=42 ORF_prediction
MRLMLSSFREVRTHAVMCANKQRVFHFAPVAWRVLWDRTSPC*
>seq2 length=87 ORF_prediction
MIWIATTRSPDATTPSNSNCCPRSKEFDGTQRKRWSSPEITLPGKPHIVGRQLTQLSGLAFSLGVGASRRLCWEPIATLSEIQCYQF*
```
