# Sequence Conversion Tool
An online system that is able to read sequence(s) from rich format and convert it into sequence(s) in simple format.

# What information we provide?
 - Rich format
 
 File supported format: Genbank, EMBL
 
 GenBank format: It consists of an annotation section and a &nbsp;sequence section.
 
 EMBL format: One sequence entry starts with an identifier &nbsp;line ("ID "), followed by further annotation lines.
 
 - Simple format
 
 Converted file format: Fasta, GCG
 
 Fasta format: The line before the nucleotide sequence, called &nbsp;the FASTA definition line, must begin with a carat (">"), &nbsp;followed by a unique SeqID (sequence identifier). 
 
 GCG format: It contains exactly one sequence, begins with &nbsp;annotation lines and the start of the sequence is marked by a &nbsp;line ending with two dot ("..") characters.
