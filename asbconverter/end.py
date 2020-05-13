# Esta função serve para acrescentar o texto em baixo no final do ficheiro nexus.


def end():
    """
    This function will append the text at the end of the nexus file
    """

    return '  ;\nEND;\n\nbegin mrbayes;\n  set autoclose=yes;\n  outgroup Podarcis;\n  mcmcp ngen=200000 ' \
           'printfreq=1000 samplefreq=100 diagnfreq=1000 nchains=4 savebrlens=yes filename=MyRun01;\n  mcmc;\n  ' \
           'sumt filename=MyRun01;\nend;'

