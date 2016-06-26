#!/usr/bin/env python

import sys
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description='extract sequences from a list of IDs')

parser.add_argument('-s', '--sequence_file', dest='seqfile',
    type=str,
    help="name of sequence file to source")
parser.add_argument('-o', '--output', dest='output', 
    type=str, help="file name for extracted sequences (optional)")
parser.add_argument('-l', '--listfile', dest='listing', 
    type=str, help="file listing seq IDs to extract (one per line)")

args = parser.parse_args()
infile = args.seqfile
outseq = args.output
listfile = args.listing


def make_list(file_list):
    """convert lines in file to elements of list. for make_list"""
    file=open(file_list, 'r')
    new_list = []
    for line in file:
        line = line.strip('\n')
        new_list.append(line)
    return new_list

def extract_seqs(seq_set, seq_file_name, new_filename='extracted'):
    """allows iteration over many take input list of sequence ids and extract them from input filename to new fasta file"""
    if new_filename == 'extracted':
        new_name = 'extracted_'+seq_file_name
    else:
        new_name = new_filename

    new_file = open(new_name, 'w')
    for seq in SeqIO.parse(seq_file_name, 'fasta'):
        rec_id = seq.id
        if rec_id in seq_set:
            SeqIO.write(seq, new_file, 'fasta')
    new_file.close()

seqlist = make_list(listfile)

seq_set = set(seqlist)

if args.output:

    extract_seqs(seq_set, infile, outseq)

else:
    extract_seqs(seq_set, infile)

print("all done")


