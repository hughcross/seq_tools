# Sequence Tools
Some basic tools in python for sequence manipulation

Following are a few simple tools that I have found to be useful for my bioinformatics work


## seq_extractor.py

**Extract a subset of DNA sequences from a file**

Software prerequisite:

* Biopython https://github.com/biopython/biopython.github.io/

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

**For use with iPython**

I often use this tool within iPython or Jupyter Notebook. You could import the function 'extract_seqs' from this file to use interactively. 

  
  
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

*you enter*
`AAATTTGGCGT`

*you can copy the response*

`reverse complement is: ACGCCAAATTT`

