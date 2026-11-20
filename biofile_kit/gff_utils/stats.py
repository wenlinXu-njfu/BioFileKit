#!/usr/bin/env python
"""
File: stats.py
Description: Based on the attribute in the 9th column (eg. Class), calculate the proportion of each Class on the genome.
CreateDate: 2025/11/25
Author: xuwenlin
E-mail: wenlinxu.njfu@outlook.com
"""
from io import TextIOWrapper
import click
from pybioinformatic import Gff, dataframe_to_str, Displayer

displayer = Displayer(__file__.split('/')[-1], version='0.1.0')


def main(
    gff_file: TextIOWrapper,
    genome_fai: TextIOWrapper,
    attr_name: str,
    output_file: TextIOWrapper = None
):
    genome_size = sum(int(line.strip().split('\t')[1]) for line in genome_fai)
    with Gff(gff_file) as gff:
        df = gff.to_dataframe()
        result = df.groupby(attr_name).apply(lambda x: (x['End'] - x['Start'] + 1).sum()).to_frame('Length')
        result['GenomeSize'] = genome_size
        result['Percent'] = result['Length'] / result['GenomeSize'] * 100
        result.loc['total', 'Length'] = result['Length'].sum()
        result.loc['total', 'GenomeSize'] = genome_size
        result.loc['total', 'Percent'] = result['Percent'].sum()
        result[['Length', 'GenomeSize']] = result[['Length', 'GenomeSize']].astype('Int32')
        result = dataframe_to_str(df=result, index=True, header=True)
        click.echo(result, output_file)


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-g', '--gff', 'gff_file',
              metavar='<file|stdin>', type=click.File('r'), required=True,
              help='Genome gff file.')
@click.option('-f', '--genome-index', 'genome_fai',
              metavar='<file|stdin>', type=click.File('r'), required=True,
              help='Genome fasta index file.')
@click.option('-n', '--attr-name', 'attr_name',
              metavar='<str>', default='Class', show_default=True,
              help='Attribute name in the 9th column of gff file that calculate the proportion.')
@click.option('-o', '--output-file', 'output_file',
              metavar='<file|stdout>', type=click.File('w'),
              help='Output file, stdout by default.')
@click.option('-V', '--version', 'version', help='Show author and version information.',
              is_flag=True, is_eager=True, expose_value=False, callback=displayer.version_info)
def run(gff_file, genome_fai, attr_name, output_file):
    """Based on the attribute in the 9th column (eg. Class), calculate the proportion of each Class on the genome."""
    main(
        gff_file=gff_file,
        genome_fai=genome_fai,
        attr_name=attr_name,
        output_file=output_file
    )


if __name__ == '__main__':
    run()
