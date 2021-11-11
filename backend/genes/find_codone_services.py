def straight_search(codon, gene):
    find = False
    i = 0
    while i <= len(gene) - len(codon):
        j = 0
        while j < len(codon):
            if codon[j] != gene[j + i]:
                find = False
                break
            find = True
            j += 1
        if find:
            return find
        i += 1
    return find


def prefix(codon):
    """
        Help function for kmp method
    """
    v = [0] * len(codon)
    for i in range(1, len(codon)):
        k = v[i - 1]
        while k > 0 and codon[k] != codon[i]:
            k = v[k - 1]
        if codon[k] == codon[i]:
            k = k + 1
        v[i] = k
    return v


def kmp_search(codon, gene):
    index = False
    f = prefix(codon)
    k = 0
    for i in range(len(gene)):
        while k > 0 and codon[k] != gene[i]:
            k = f[k - 1]
        if codon[k] == gene[i]:
            k = k + 1
        if k == len(codon):
            index = True
            break
    return index


def method_in(codon, gene):
    return True if codon in gene else False


def method_find(codon, gene):
    return True if gene.find(codon) != -1 else False


def method_straight(codon, gene):
    return straight_search(codon, gene)


def method_kmp(codon, gene):
    return kmp_search(codon, gene)
