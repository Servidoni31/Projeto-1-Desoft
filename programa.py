from funcoes import define_posicoes, preenche_frota, posicao_valida

navios = {
    "porta-aviões": [4, 1],
    "navio-tanque": [3, 2],
    "contratorpedeiro": [2, 3],
    "submarino": [1, 4],
}

frota = {}

for nome in navios:
    tamanho = navios[nome][0]
    quantidade = navios[nome][1]
    i = 0
    while i < quantidade:
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        if tamanho == 1:
            orientacao = "vertical"
        else:
            opcao = int(input("[1] Vertical [2] Horizontal >"))
            if opcao == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            i += 1
        else:
            print("Esta posição não está válida!")

print(frota)