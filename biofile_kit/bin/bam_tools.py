#!/usr/bin/env python
"""
File: bam_tools.py
Description: Bam file tools.
CreateDate: 2026/1/29
Author: xuwenlin
E-mail: wenlinxu.njfu@outlook.com
"""
import click
from biofile_kit.bam_utils import filtration, insert_size_stats, __version__
from pybioinformatic import Displayer

displayer = Displayer(__file__.split('/')[-1], version=__version__)


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-V', '--version', 'version', help='Show author and version information.',
              is_flag=True, is_eager=True, expose_value=False, callback=displayer.version_info)
def bam_tools():
    """Bam file tools."""
    pass


bam_tools.add_command(filtration, 'filtration')
bam_tools.add_command(insert_size_stats, 'insert_size_stats')

if __name__ == '__main__':
    bam_tools()
