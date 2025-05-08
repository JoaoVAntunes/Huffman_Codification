def generate_codes(node, prefix='', codebook=None):
    if codebook is None:
        codebook = {}

    if isinstance(node[1], str):  # nó folha
        codebook[node[1]] = prefix
    else:
        generate_codes(node[1][0], prefix + '0', codebook)  # esquerda
        generate_codes(node[1][1], prefix + '1', codebook)  # direita
    return codebook