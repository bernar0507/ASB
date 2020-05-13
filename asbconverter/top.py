# Nesta função, criamos o cabecário.


def top(dict1):

    """
    This function doesn't receive any argument.
    It returns a variable (top) that is the text that is suppose to be at the top of the nexus file.
    That string also contains 2 variables: num_names and num_char. The num_names is the number of names
    of the sequences and the variable num_char is the length of the sequence.
    """

    num_names = len(dict1.keys())
    num_char = []
    [num_char.append(len(v)) for v in dict1.values() if len(v) not in num_char]

    top = '#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX={} NCHAR={};\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n'.format(
        num_names, num_char[0])

    return top
