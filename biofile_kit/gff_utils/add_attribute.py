#!/usr/bin/env python
"""
File: add_attribute.py
Description: Add attribute in 9th column of GFF file.
CreateDate: 2025/11/17
Author: xuwenlin
E-mail: wenlinxu.njfu@outlook.com
"""
from typing import Union
from io import TextIOWrapper
import click
from pybioinformatic import Gff, Displayer

displayer = Displayer(__file__.split('/')[-1], version='0.1.0')


def main(
    gff_file: Union[str, TextIOWrapper],
    attr_file: Union[str, TextIOWrapper],
    output_file: TextIOWrapper = None
):
    with Gff(gff_file) as gff:
        for line in gff.add_attr(attr_file):
            click.echo(line, output_file)


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('gff_file', metavar='<gff|stdin>', type=click.File('r'))
@click.option('-a', '--attr-file', 'attr_file',
              metavar='<file|stdin>', type=click.File('r'), required=True,
              help=r'Attribute file added to 9th column (header=ID\tAttrName1\tAttrName2\tEtc). '
                   '\033[1mNote that if the attribute name in the attribute file has the same name as '
                   'the attribute name in the 9th column of the GFF file, '
                   'the value of that attribute will be updated.\033[0m')
@click.option('-o', '--output-file', 'output_file',
              metavar='<file|stdout>', type=click.File('w'),
              help='Output file, stdout by default.')
@click.option('-V', '--version', 'version', help='Show author and version information.',
              is_flag=True, is_eager=True, expose_value=False, callback=displayer.version_info)
def run(gff_file, attr_file, output_file):
    """Add attribute in 9th column of GFF file."""
    main(gff_file, attr_file, output_file)


if __name__ == '__main__':
    run()
