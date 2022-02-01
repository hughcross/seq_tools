#!/usr/bin/env python


from Bio import SeqIO

def make_list(file_list):
    """convert lines in file to elements of list. for make_list"""
    file=open(file_list, 'r')
    new_list = []
    for line in file:
        line = line.strip('\n')
        new_list.append(line)
    return new_list

def extract_seqs(seq_set, seq_file_name, filetype='fasta', new_filename='extracted'):
    """allows iteration over many take input list of sequence ids and extract them from input filename to new fasta file"""
    if new_filename == 'extracted':
        new_name = 'extracted_'+seq_file_name
    else:
        new_name = new_filename

    new_file = open(new_name, 'w')
    #if filetype == 'fasta':
    for seq in SeqIO.parse(seq_file_name, filetype):
        rec_id = seq.id
        if rec_id in seq_set:
            SeqIO.write(seq, new_file, filetype)
    
    new_file.close()

