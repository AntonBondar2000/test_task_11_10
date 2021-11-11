import re


def validator_codon(codon):
    error = []
    if not bool(re.search(r'^[acgt]+$', codon, re.IGNORECASE)):
        error.append("Invalid data: codon must consist only 'A', 'C', 'G', 'T'")
    if len(codon) != 3:
        error.append("Invalid data: codon must be 3 long")
    return error

