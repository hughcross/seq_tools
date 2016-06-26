#!/usr/bin/env python

# script to rename fasta and fastq files

import sys
import argparse

parser = argparse.ArgumentParser(description='script to rename fq/fa files')

parser.add_argument('-i', '--input_file', dest='input',
type=str,
help='fastq input filename')

parser.add_argument('-o', '--output_file', dest='out',
type=argparse.FileType('w'),
help='fastq output filename')

parser.add_argument('-p', '--prefix', dest='prefix',
type=str,
help='new name to add to beginning of each sequence name')

parser.add_argument('-s', '--suffix', dest='suffix',
type=str,
help='new name to add to end of each sequence name')

parser.add_argument('-f', '--format', dest='format',
type=str,
help='output format, for paired end RNAseq: use fwd, rev')

parser.add_argument('-k', '--key_phrase', dest='key',
type=str,
help='key phrase to recognize ID line')

args = parser.parse_args()
infile = args.input
output = args.out
prefix = args.prefix
suffix = args.suffix
format = args.format
start = args.key

infile1 = open(infile, 'r')
firstline = infile1.readline()
infile1.close()


if firstline.startswith('>'):
    filetype = 'fa'
    start = '>'
    beginning = '>'
elif firstline.startswith('@'):
    filetype = 'fq'
    start = firstline[:3]
    beginning = '@'

if args.prefix:
    if filetype == 'fa':
        namestart = '>'+prefix
    elif filetype == 'fq':
        namestart = '@'+prefix
    else:
        print('cannot determine file type, (fasta or fastq)')
        sys.exit()
else:
    if filetype == 'fa':
        namestart = '>'
    elif filetype == 'fq':
        namestart = '@'
    else:
        print('cannot determine file type, (fasta or fastq)')
        sys.exit()

if args.suffix:
    end = suffix
else:
    end = ''


seqfile = open(infile, 'r')

if args.format:
    if format == 'fwd':
        endline = '/1\n'
    elif format == 'forward':
        endline = '/1\n'
    elif format == 'reverse':
        endline = '/2\n'
    elif format == 'rev':
        endline = '/2\n'
    else:
        print('you have to specify fwd or rev for paired end data')
        sys.exit()

    for line in seqfile: 
        if line.startswith(start):
            line = line.strip('\n')
            firstname = line.split(' ')[0]
            oldline = firstname.split(beginning)[1]
            newline = namestart+oldline+end+endline
            output.write(newline)
        else:
            output.write(line)

else:
    for line in seqfile:
        if line.startswith(start):
            line = line.strip('\n')
            oldline = line.split(beginning)[1]
            newline = namestart+oldline+end+'\n'
            output.write(newline)
        else:
            output.write(line)


output.close()





