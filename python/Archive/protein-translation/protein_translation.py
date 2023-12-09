from textwrap import wrap

def proteins(strand):
    
    # textwrap.wrap(s, i) creates a list of elements from s with a max width of i
    codons = wrap(strand, 3)
    codons_to_protein = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP',
        'UAG': 'STOP',
        'UGA': 'STOP'
    }

    RNA = []

    for i in codons:
        if codons_to_protein[i] == 'STOP':
            break
        else:
            RNA.append(codons_to_protein[i])

    return RNA
