def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    i = 0
    while i < tamanho:
        if orientacao=="vertical":
            posicoes.append([linha+i,coluna])
        else:
            posicoes.append([linha,coluna+i])
        i += 1
    return posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in frota:
        frota[nome_navio] = []

    frota[nome_navio].append(posicoes)
    return frota


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro
def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0] * 10)

    for tipo in frota:
        for navio in frota[tipo]:
            for pos in navio:
                tabuleiro[pos[0]][pos[1]] = 1

    return tabuleiro

def afundados(frota, tabuleiro):
    quantidade = 0

    for tipo in frota:
        for navio in frota[tipo]:
            afundou = True

            for linha, coluna in navio:
                if tabuleiro[linha][coluna] != 'X':
                    afundou = False

            if afundou:
                quantidade += 1

    return quantidade

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in posicoes:
        l, c = posicao

        if l < 0 or l >= 10 or c < 0 or c >= 10:
            return False

        for tipo in frota:
            for navio in frota[tipo]:
                if posicao in navio:
                    return False

    return True
