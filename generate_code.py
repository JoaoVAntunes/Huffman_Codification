def generate_codes(node, prefix='', codebook=None):
    if codebook is None:
        codebook = {}

    content = node[2]

    if isinstance(content, str):  # nó folha
        codebook[content] = prefix
    else:
        # content é [esquerda, direita], cada um no mesmo formato [freq, count, conteúdo]
        generate_codes(content[0], prefix + '0', codebook) #esquerda
        generate_codes(content[1], prefix + '1', codebook) #direita

    return codebook