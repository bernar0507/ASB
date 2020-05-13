import difflib
def fileparser(fasta_file):
    """
    In the for loop, it will go though all the names of the sequences.
    If it has ">" will be considered has a sequence. Will go though all the fasta file and will remove the >.
    The strip() method is use to remove the enters (\n)
    The dictionary will start with the name and the sequence will be empty.
    If the for loop does not find the ">", the line will be added as part of the sequence.
    """
    dict1 = {}
    for i in fasta_file:
        if i.startswith(">"):
            name = i.replace(">", "").strip()
            dict1[name] = ""
        else:
            dict1[name] += i.strip()
    for i in dict1.keys():
        if len(i) > 99:
            i = i[:99]
    #[name_key[:99] for name_key in iter(dict1.keys()) if len(name_key) > 99] 
    
    return dict1
    #taxas = [dict1.keys()]
    #results = resultados(difflib.Differ.compare(taxas,