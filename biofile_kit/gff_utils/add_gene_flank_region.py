#!/usr/bin/env python
"""
File: add_gene_flank_region.py
Description: Add gene flank region.
CreateDate: 2025/12/8
Author: xuwenlin
E-mail: wenlinxu.njfu@outlook.com
"""
from io import TextIOWrapper
import click
from pybioinformatic import Gff, Displayer

displayer = Displayer(__file__.split('/')[-1], version='0.1.0')


def main(
    fai_file: TextIOWrapper,
    gff_file: TextIOWrapper,
    flank_len: int = 2000,
    output_file: click.utils.LazyFile = None
):
    with Gff(gff_file) as gff:
        for line in gff.add_flank_region(
            fai_file=fai_file,
            feature='gene',
            flank_len=flank_len
        ):
            click.echo(line, output_file)


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('fai_file', metavar='<fai|stdin>', type=click.File('r'))
@click.argument('gff_file', metavar='<gff|stdin>', type=click.File('r'))
@click.option('-l', '--flank-len', 'flank_len',
              metavar='<int>', type=int, default=2000, show_default=True,
              help='Flank region length of genes.')
@click.option('-o', '--output-file', 'output_file',
              metavar='<file|stdout>', type=click.File('w'),
              help='Output file, stdout by default.')
@click.option('-V', '--version', 'version', help='Show author and version information.',
              is_flag=True, is_eager=True, expose_value=False, callback=displayer.version_info)
def run(fai_file, gff_file, flank_len, output_file):
    """Add gene flank region."""
    main(fai_file, gff_file, flank_len, output_file)


if __name__ == '__main__':
    run()
