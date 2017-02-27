#!/usr/bin/env python

import sys
import argparse
from Bio import SeqIO
# changed calling the function to work better with symbolic links
from seq_functions.seq_funcs import *

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



seqlist = make_list(listfile)

seq_set = set(seqlist)

if args.output:

    extract_seqs(seq_set, infile, outseq)

else:
    extract_seqs(seq_set, infile)

print("all done")


