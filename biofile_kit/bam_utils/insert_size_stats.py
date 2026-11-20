#!/usr/bin/env python
"""
File: insert_size_stats.py
Description: Insertion fragment size statistics.
CreateDate: 2026/1/29
Author: xuwenlin
E-mail: wenlinxu.njfu@outlook.com
"""
from typing import Tuple
from os import getcwd, makedirs
import click
from pybioinformatic import TaskManager, Displayer

displayer = Displayer(__file__.split('/')[-1], version='0.0.0')


def main(
    bam_files: Tuple[str],
    num_processing: int = 4,
    output_path: str = '.'
):
    plot_insert_size = '/'.join(__file__.split('/')[:-1]) + '/plot_insert_size.R'
    makedirs(output_path, exist_ok=True)
    cmds = []
    for bam in bam_files:
        bam_name = bam.split('/')[-1]
        cmd = fr'''samtools view -f 0x40 {bam} | perl -ane 'print abs($F[8]);print "\n";' | sort -n > {output_path}/{bam_name}.insertSize.txt; Rscript {plot_insert_size} {output_path}/{bam_name}.insertSize.txt {output_path}/{bam_name}.insertSize.png'''
        cmds.append(cmd)
    tkm = TaskManager(num_processing=num_processing, commands=cmds)
    tkm.parallel_run_cmd(show_cmd=False, pipe=False)


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('bam_files', metavar='<bam_files>', nargs=-1)
@click.option('-p', '--num-processing', 'num_processing',
              metavar='<int>', type=int, default=4, show_default=True,
              help='Number of processing.')
@click.option('-o', '--output-path', 'output_path',
              metavar='<path>', default=getcwd(), show_default=True,
              help='Output path, if the specified path does not exist, it will be automatically created.')
@click.option('-V', '--version', 'version', help='Show author and version information.',
              is_flag=True, is_eager=True, expose_value=False, callback=displayer.version_info)
def run(bam_files, num_processing, output_path):
    """Insertion fragment size statistics."""
    main(bam_files, num_processing, output_path)


if __name__ == '__main__':
    run()
