# %load dnatorna.py
"""
Convert DNA sequences to RNA.
"""

def rna(seq):
    """
    Convert a DNA sequence to RNA.
    """

    # Determine if original sequence was upper or lower case
    seq_upper = seq.isupper()

    # Covert to lower case
    seq = seq.lower()

    #swap out 't' for 'u'
    seq = seq.replace('t','u')

    #return upper ot lower case RNA sequence
    if seq_upper:
        return seq.upper()
    else:
        return seq

def reverse_rna_complement(seq):
    """
    Convert a DNA sequence into its reverse complement as RNA
    """

    # Determine if original was upper case
    seq_upper = seq.isupper()

    #Reverse sequence
    seq = seq[::-1]

    # Convert to upper
    seq = seq.upper()

    # Compute replacement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    # Return result
    if seq_upper:
        return seq.upper()
    else:
        return seq
