#!/usr/bin/env python

import argparse
import sys
from Bio.Seq import reverse_complement
from Bio import SeqIO
<<<<<<< HEAD
#from StringIO import StringIO
=======
>>>>>>> 16e5ece7e8c06b86512c0424c7533b781bbc8a7e
from io import StringIO
from Bio.SeqRecord import SeqRecord
#from Bio.Alphabet import IUPAC
from Bio.Seq import Seq


parser = argparse.ArgumentParser(description='get reverse complement of a sequence or file of seqs')
parser.add_argument('-i', '--sequence_file', dest='seqfile',
    type=str,
    help="name of input sequence file")
parser.add_argument('-o', '--output', dest='output', 
    type=str, help="output file name for reverse complemented sequences (optional)")

args = parser.parse_args()
infile = args.seqfile
outseq = args.output

if args.seqfile:
	if args.output:
		output_name = outseq
	else:
		output_name = 'reverse_comp_'+infile
	outfile = open(output_name, 'w')
	seqfile = open(infile, 'r')
	for seq in SeqIO.parse(seqfile, 'fasta'):
	    rec_id = str(seq.id)
	    rec_seq = seq.seq
	    rev = str(reverse_complement(rec_seq))
	    new = SeqRecord(Seq(rev), id=rec_id, description='')
	    
	    SeqIO.write(new, outfile, 'fasta')
	    
else:
	DNAseq = input("enter sequence to reverse complement: ")
	from Bio.Seq import reverse_complement
	RCseq = reverse_complement(DNAseq)
	print('reverse complement is: ',RCseq)

