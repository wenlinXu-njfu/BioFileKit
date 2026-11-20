#!/usr/bin/env python
"""
File: gtf2gff.py
Description: Convert the file format from GTF to GFF.
CreateDate: 2026/3/22
Author: xuwenlin
E-mail: wenlinxu.njfu@outlook.com
"""
from io import TextIOWrapper
import click
from pybioinformatic import Gtf, Displayer

displayer = Displayer(__file__.split('/')[-1], version='0.1.0')


def main(
    gtf_file: TextIOWrapper,
    feature_type: str = 'mRNA',
    output_file: click.utils.LazyFile = None
):
    with Gtf(gtf_file) as gtf:
        click.echo(gtf.to_gff(feature_type=feature_type), output_file)


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('gtf_file', metavar='<gtf>', type=click.File('r'))
@click.option('-t', '--feature-type', 'feature_type',
              default='mRNA', show_default=True,
              help='Feature type.')
@click.option('-o', '--output-file', 'output_file',
              metavar='<file|stdout>', type=click.File('w'),
              help='Output file, stdout by default.')
@click.option('-V', '--version', 'version', help='Show author and version information.',
              is_flag=True, is_eager=True, expose_value=False, callback=displayer.version_info)
def run(gtf_file, feature_type, output_file):
    """Convert the file format from GTF to GFF."""
    main(gtf_file, feature_type, output_file)


if __name__ == '__main__':
    run()
