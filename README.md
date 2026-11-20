# Introduction
**BioFileKit: A Python command-line toolkit dedicated to simplifying the reading, writing, conversion, 
parsing and basic operations of various biological data file formats.**

# Install
```
pip install biofile-kit --upgrade
```

# Change logs
## v0.1.1
- New
  - bam file tools ([gff_tools](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/bam_tools.py)):
    - [bam file filtration](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bam_utils/bam_filter.py)
    - [insertion fragment size statistics](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bam_utils/insert_size_stats.py)
  - fasta file tools ([fasta_tools](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/fasta_tools.py)):
    - [motif sequence support for degenerate bases](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/fasta_utils/motif_finder.py)
  - Gff file tools ([gff_tools](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/gff_tools.py)):
    - [add attributions in 9th column of gff file](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/gff_utils/add_attribute.py)
    - [add gene flank region](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/gff_utils/add_gene_flank_region.py)
    - [based on the attribute in the 9th column (eg. "Class"), calculate the proportion of each "Class" on the genome](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/gff_utils/stats.py)
  - Gtf file tools ([https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/gtf_tools.py])
    - [convert the file format from gtf to gff](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/gtf_utils/gtf2gff.py)
- Modified
  - Gff file tools ([gff_tools](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/gff_tools.py)):
    - [rename "stats" module to "summary"](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/gff_utils/stats.py)
  - Fasta file tools ([gff_tools](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/fasta_tools.py)):
    - [fix the bug that causes the negative strand to fail in finding telomeres](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/fasta_utils/telomere_finder.py)
- Deleted
  - Null
## v0.1.0
- New
  - Fasta file tools ([fasta_tools](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/fasta_tools.py)):
    - [change hard masked to soft masked](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/fasta_utils/hardmasked_to_softmasked.py)
    - [telomere finder](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/fasta_utils/telomere_finder.py)
  - Gff file tools ([gff_tools](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/gff_tools.py)):
    - [statistical analysis of gff file](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/gff_utils/stats.py)
  - Genotype file tools ([gt_kit](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/gt_kit.py)):
    - [genotype consistency analysis](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/gt_utils/genotype_consistency_analysis.py)
    - [genotype file merging](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/gt_utils/merge.py)
    - [statistical analysis of SNP loci](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/gt_utils/stat_gt.py)
  - VCF file tools ([vcf_tools](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/bin/vcf_tools.py)):
    - [convert the file format from vcf to genotype (gt)](https://github.com/wenlinXu-njfu/BioFileKit/blob/main/biofile_kit/vcf_utils/vcf2gt.py)
- Modified
  - Null
- Deleted
  - Null

# Usage example
**All commands in the "biofile_kit/bin" directory can type `-h` to see subcommands.**<br />
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
  add_attr             Add attribute in 9th column of GFF file.
  extract_seq          Extract sequences from GFF file.
  get_feature_density  Get feature density from GFF file.
  rename               This script provides a standardized feature ID...
  sort                 Sort naturally in sequence according to...
  stats                Based on the attribute in the 9th column (eg.
  summary              Summarize the information of various features in...
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
