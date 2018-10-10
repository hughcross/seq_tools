# Sequence Tools
Some basic tools in python for sequence manipulation

Following are a few simple tools that I have found to be useful for my bioinformatics work


## seq_extractor.py

**Extract a subset of DNA sequences from a file**

Software prerequisite:

* Biopython https://biopython.org/

**Description**

For this tool, the user inputs a file of a list of sequence ids, a sequence file, and optionally the name of a new file, and the script will extract those sequences to a new file. 

If you do not provide a new file name, the new sequence file will be named as "extracted_" + the name of the master sequence file. 

I have used this script to extract sequences from very massive files (up to 15 Gb) with over 12 million sequences, and it finished in under five minutes (will depend on your computer, but I have run this on my laptop without problem). The example files included in this repo are from the Norway Spruce genome (*Picea abies*), which is available on http://congenie.org/ 

Here is an example usage, using the included files:

`seq_extractor.py -l example_sequence_list.txt -s example_sequences.fa`

or, to add a name for the new file:

`seq_extractor.py -l example_sequence_list.txt -s example_sequences.fa -o new_subset.fa`

If you run either of these, you should get a new file with nine sequences. 


**Note on sequence ids**

Each sequence id should include everything after the ">" but *before* the space. 

For example, to obtain a sequence that reads like this:

\>MA_1 len=89935

you list it as:

MA_1

  
  
## revcomp.py

**Get the reverse complement of a fasta file or a single sequence**

Software prerequisite:

* Biopython https://github.com/biopython/biopython.github.io/

**Description**

This script will return the reverse complement of the file or sequence that you input. For a file, use the '-i' sequence input argument, and optionally the '-o' for the name of the new reverse-complemented file. If you want to just reverse complement a single sequence (such as a primer or other short sequence), do not use any input arguments, and you will be prompted to paste in a sequence. 

Like so:

`revcomp.py -i example_sequences.fa -o testout.fa`

Or

`revcomp.py -i example_sequences.fa`
  
**for a single sequence**

`revcomp.py`

*you are prompted to enter sequence:*

`enter sequence to reverse complement:`

*you enter, for example*

`AAATTTGGCGT`

*you get the reverese complement response:*

`reverse complement is: ACGCCAAATTT`

## seq_name_changer.py

**Rename sequences in fasta or fastq file**

**Description**

This script has various options for renaming sequences, including adding a new tag to beginning or end of file, as well as formatting paired end sequences for many programs where specific naming is recommended or required. The program will detect whether it is fasta or fastq.

For typical usage, if you want to add a prefix to each sequence:

`seq_name_changer.py -i example_sequences.fa -o example_out.fa -p spruce-scaffold:`

original sequence:

\>MA_1 len=89935

will be converted to

\>spruce-scaffold:MA_1 len=89935


For applications where you need to rename paired end RNAseq sequences to conform to specific applications, where each sequence name requires a '/1' for left or forward reads, and '/2' for right or reverse reads:

`seq_name_changer.py -i example_sequences.fa -o example_pe_1.fa -f fwd`

all sequences will be renamed as such:

\>MA_1/1

You can add both prefixes and suffixes:

`seq_name_changer.py -i example_sequences.fa -o example_pe_1.fa -p spruce-scaffold: -s :paired-end -f fwd`

Will give you:

\>spruce-scaffold:MA_1:paired-end/1

*Remember that apart from the /1 and /2 each pair should have the same name!*


