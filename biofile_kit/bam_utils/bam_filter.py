#!/usr/bin/env python
"""
File: bam_filter.py
Description: Bam file filtration.
CreateDate: 2025/12/22
Author: xuwenlin
E-mail: wenlinxu.njfu@outlook.com
"""
from io import TextIOWrapper
from pysam import AlignmentFile
import click
from pybioinformatic import Displayer

displayer = Displayer(__file__.split('/')[-1], version='0.0.0')


def calculate_alignment_length(read, operations: tuple = None) -> int:
    """
    Calculate the valid alignment length of reads on the reference genome based on the CIGAR string.
    CIGAR中，'M', '=', 'X' 代表匹配/错配，'I' 代表插入（在参考中无对应），
    'D' 和 'N' 代表删除和跳过（在参考中占据长度）。
    通常，比对长度 = 匹配(M/=X) + 删除(D) + 跳过(N) 的碱基数。
    """
    aligned_length = 0
    if operations is None:
        operations = (0, 2, 3, 7, 8)
    if read.cigar:
        for operation, length in read.cigar:
            # 操作码含义: M/=/X (0/7/8): 对齐; D (2): 参考缺失; N (3): 参考跳过（内含子）
            if operation in operations:
                aligned_length += length
    return aligned_length


def main(
    input_bam: TextIOWrapper,
    min_q: int = 20,
    min_alignment_len: int = 10000,
    min_alignment_cov: float = 0.9,
    supplementary_alignment: bool = True,
    not_primary_alignment: bool = True,
    output_bam: str = 'filtered.bam'
):
    with AlignmentFile(input_bam) as inbam, \
            AlignmentFile(output_bam, 'wb', template=inbam) as outbam:
        for read in inbam:
            if not read.is_unmapped and read.query_length != 0:  # read mapped reference
                alignment_len = calculate_alignment_length(read, operations=(0,))
                conditions1 = [
                    not not_primary_alignment and not supplementary_alignment,
                    # not secondary alignment and not supplementary alignment
                    not_primary_alignment and not (read.flag & 0x100) and supplementary_alignment and not (read.flag & 0x800),
                    # not secondary alignment
                    not_primary_alignment and not (read.flag & 0x100) and not supplementary_alignment,
                    # not supplementary alignment
                    supplementary_alignment and not (read.flag & 0x800) and not not_primary_alignment
                ]
                conditions2 = [
                    # mapping Q value filtration
                    read.mapping_quality >= min_q,
                    # alignment length filtration
                    alignment_len >= min_alignment_len,
                    # alignment coverage filtration
                    alignment_len / read.query_length >= min_alignment_cov
                ]
                if any(conditions1) and all(conditions2):
                    outbam.write(read)


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('bam', metavar='<bam|stdin>', type=click.File('rb'))
@click.option('-q', '--min-map-q-value', 'min_q',
              metavar='<int>', type=int, default=20, show_default=True,
              help='Minimum mapping Q value.')
@click.option('-l', '--min-alignment-len', 'min_alignment_len',
              metavar='<int>', type=int, default=10000, show_default=True,
              help='Minimum alignment length.')
@click.option('-c', '--min-alignment-cov', 'min_alignment_cov',
              metavar='<int>', type=float, default=0.9, show_default=True,
              help='Minimum alignment coverage.')
@click.option('-s', '--filter-supplementary-alignment', 'supplementary_alignment',
              is_flag=True, flag_value=True,
              help='Filter supplementary alignment reads.')
@click.option('-p', '--filter-non-primary-alignment', 'not_primary_alignment',
              is_flag=True, flag_value=True,
              help='Filter not primary alignment reads.')
@click.option('-o', '--output-bam', 'output_bam',
              metavar='<file>', help='Output bam file.')
@click.option('-V', '--version', 'version', help='Show author and version information.',
              is_flag=True, is_eager=True, expose_value=False, callback=displayer.version_info)
def run(bam, min_q, min_alignment_len, min_alignment_cov, supplementary_alignment, not_primary_alignment, output_bam):
    """Bam file filtration."""
    main(
        input_bam=bam,
        min_q=min_q,
        min_alignment_len=min_alignment_len,
        min_alignment_cov=min_alignment_cov,
        supplementary_alignment=supplementary_alignment,
        not_primary_alignment=not_primary_alignment,
        output_bam=output_bam
    )


if __name__ == '__main__':
    run()
