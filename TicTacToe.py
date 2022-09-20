import random
from os import X_OK, system, name


def limpaTela():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def defe(tabuleiro, simboloComputador, x, y, z):
    """
    Verifica se o parâmetro "x" e "y" são diferentes de vazio e do símbolo do Computador, bem como verifica se o parâmetro "z" é vazio:
    Se sim, retorna True, senão, retorna False.
    """
    if (
        tabuleiro[x] != simboloComputador
        and tabuleiro[x] != " "
        and tabuleiro[y] != simboloComputador
        and tabuleiro[y] != " "
        and tabuleiro[z] == " "
    ):
        return True
    return False


def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas,
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia:
    # Explique aqui, de forma resumida, a sua estratégia usada para o computador vencer o jogador

    O computador verificará se há alguma possível combinação que o faça vencer,
    caso não vença, ele irá bloquear, da maneira possível, a vitória do usuário (se houver a chance de o usuário vencer).
    Se não houver chance de vitória ou jogadas de defesa a serem feitas, então ele simplesmente irá selecionar uma espaço vazio com a ordem de prioridade:
    [1], [2], [5], [7], [9], [3], [4], [6], [8].
    """
    # Combinações para vencer
    if (
        tabuleiro[1] == simboloComputador
        and tabuleiro[2] == simboloComputador
        and tabuleiro[3] == " "
    ):
        j = 3
    elif (
        tabuleiro[1] == simboloComputador
        and tabuleiro[3] == simboloComputador
        and tabuleiro[2] == " "
    ):
        j = 2
    elif (
        tabuleiro[2] == simboloComputador
        and tabuleiro[3] == simboloComputador
        and tabuleiro[1] == " "
    ):
        j = 1
    elif (
        tabuleiro[4] == simboloComputador
        and tabuleiro[5] == simboloComputador
        and tabuleiro[6] == " "
    ):
        j = 6
    elif (
        tabuleiro[4] == simboloComputador
        and tabuleiro[6] == simboloComputador
        and tabuleiro[5] == " "
    ):
        j = 5
    elif (
        tabuleiro[5] == simboloComputador
        and tabuleiro[6] == simboloComputador
        and tabuleiro[4] == " "
    ):
        j = 4
    elif (
        tabuleiro[7] == simboloComputador
        and tabuleiro[8] == simboloComputador
        and tabuleiro[9] == " "
    ):
        j = 9
    elif (
        tabuleiro[7] == simboloComputador
        and tabuleiro[9] == simboloComputador
        and tabuleiro[8] == " "
    ):
        j = 8
    elif (
        tabuleiro[2] == simboloComputador
        and tabuleiro[5] == simboloComputador
        and tabuleiro[8] == " "
    ):
        j = 8
    elif (
        tabuleiro[9] == simboloComputador
        and tabuleiro[8] == simboloComputador
        and tabuleiro[7] == " "
    ):
        j = 7
    elif (
        tabuleiro[3] == simboloComputador
        and tabuleiro[5] == simboloComputador
        and tabuleiro[7] == " "
    ):
        j = 7
    elif (
        tabuleiro[1] == simboloComputador
        and tabuleiro[4] == simboloComputador
        and tabuleiro[7] == " "
    ):
        j = 7
    elif (
        tabuleiro[1] == simboloComputador
        and tabuleiro[5] == simboloComputador
        and tabuleiro[9] == " "
    ):
        j = 9
    elif (
        tabuleiro[1] == simboloComputador
        and tabuleiro[9] == simboloComputador
        and tabuleiro[5] == " "
    ):
        j = 5
    elif (
        tabuleiro[5] == simboloComputador
        and tabuleiro[9] == simboloComputador
        and tabuleiro[1] == " "
    ):
        j = 1
    elif (
        tabuleiro[7] == simboloComputador
        and tabuleiro[1] == simboloComputador
        and tabuleiro[4] == " "
    ):
        j = 4
    elif (
        tabuleiro[8] == simboloComputador
        and tabuleiro[5] == simboloComputador
        and tabuleiro[2] == " "
    ):
        j = 2
    elif (
        tabuleiro[9] == simboloComputador
        and tabuleiro[3] == simboloComputador
        and tabuleiro[6] == " "
    ):
        j = 6
    elif (
        tabuleiro[7] == simboloComputador
        and tabuleiro[5] == simboloComputador
        and tabuleiro[3] == " "
    ):
        j = 3
    elif (
        tabuleiro[3] == simboloComputador
        and tabuleiro[6] == simboloComputador
        and tabuleiro[9] == " "
    ):
        j = 9
    elif (
        tabuleiro[9] == simboloComputador
        and tabuleiro[6] == simboloComputador
        and tabuleiro[3] == " "
    ):
        j = 3

    # Combinações para se defender
    elif defe(tabuleiro, simboloComputador, 1, 2, 3):
        return 3
    elif defe(tabuleiro, simboloComputador, 1, 3, 2):
        return 2
    elif defe(tabuleiro, simboloComputador, 8, 5, 2):
        return 2
    elif defe(tabuleiro, simboloComputador, 2, 3, 1):
        return 1
    elif defe(tabuleiro, simboloComputador, 4, 5, 6):
        return 6
    elif defe(tabuleiro, simboloComputador, 4, 6, 5):
        return 5
    elif defe(tabuleiro, simboloComputador, 5, 6, 4):
        return 4
    elif defe(tabuleiro, simboloComputador, 7, 1, 4):
        return 4
    elif defe(tabuleiro, simboloComputador, 7, 8, 9):
        return 9
    elif defe(tabuleiro, simboloComputador, 7, 9, 8):
        return 8
    elif defe(tabuleiro, simboloComputador, 9, 8, 7):
        return 7
    elif defe(tabuleiro, simboloComputador, 1, 4, 7):
        return 7
    elif defe(tabuleiro, simboloComputador, 1, 5, 9):
        return 9
    elif defe(tabuleiro, simboloComputador, 1, 9, 5):
        return 5
    elif defe(tabuleiro, simboloComputador, 5, 9, 1):
        return 1
    elif defe(tabuleiro, simboloComputador, 3, 5, 7):
        return 7
    elif defe(tabuleiro, simboloComputador, 2, 5, 8):
        return 8
    elif defe(tabuleiro, simboloComputador, 9, 3, 6):
        return 6
    elif defe(tabuleiro, simboloComputador, 9, 6, 3):
        return 3
    elif defe(tabuleiro, simboloComputador, 3, 6, 9):
        return 9
    elif defe(tabuleiro, simboloComputador, 7, 2, 5):
        return 5
    elif defe(tabuleiro, simboloComputador, 2, 8, 5):
        return 5
    elif defe(tabuleiro, simboloComputador, 7, 3, 8) or defe(
        tabuleiro, simboloComputador, 9, 1, 8
    ):
        return 8
    elif defe(tabuleiro, simboloComputador, 7, 5, 3):
        return 3
    elif defe(tabuleiro, simboloComputador, 7, 4, 1):
        return 1
    elif (
        tabuleiro[1] == simboloComputador
        and tabuleiro[8] == simboloComputador
        and tabuleiro[9] == " "
    ):
        j = 9
    elif (
        tabuleiro[3] == simboloComputador
        and tabuleiro[8] == simboloComputador
        and tabuleiro[7] == " "
    ):
        j = 7
    elif (
        tabuleiro[9] == simboloComputador
        and tabuleiro[2] == simboloComputador
        and tabuleiro[1] == " "
    ):
        j = 1
    elif (
        tabuleiro[7] == simboloComputador
        and tabuleiro[2] == simboloComputador
        and tabuleiro[3] == " "
    ):
        j = 3
    elif (
        tabuleiro[6] != simboloComputador
        and tabuleiro[6] != " "
        and defe(tabuleiro, simboloComputador, 8, 2, 9)
    ):
        return 9

    elif (
        tabuleiro[8] != simboloComputador
        and tabuleiro[7] == simboloComputador
        and tabuleiro[4] != simboloComputador
        and tabuleiro[3] == " "
    ):
        j = 5

    elif (
        tabuleiro[1] == simboloComputador
        and tabuleiro[3] == simboloComputador
        and tabuleiro[4] != simboloComputador
        and tabuleiro[5] == " "
    ):
        j = 5

    elif (
        tabuleiro[1] == simboloComputador
        and tabuleiro[2] != simboloComputador
        and tabuleiro[3] == simboloComputador
        and tabuleiro[7] == " "
    ):
        j = 7
    elif (
        tabuleiro[1] == simboloComputador
        and tabuleiro[3] == simboloComputador
        and tabuleiro[5] == " "
    ):
        j = 5
    elif (
        tabuleiro[1] == simboloComputador
        and tabuleiro[2] != simboloComputador
        and tabuleiro[2] != " "
        and tabuleiro[4] == " "
    ):
        j = 4
    elif (
        tabuleiro[1] == simboloComputador
        and tabuleiro[5] != simboloComputador
        and tabuleiro[5] != " "
        and tabuleiro[9] == " "
    ):
        j = 9
    elif (
        tabuleiro[1] == simboloComputador
        and tabuleiro[7] != simboloComputador
        and tabuleiro[7] != " "
        and tabuleiro[9] == " "
    ):
        j = 9
    elif (
        tabuleiro[8] != simboloComputador
        and tabuleiro[8] != " "
        and tabuleiro[3] != simboloComputador
        and tabuleiro[3] != " "
        and tabuleiro[9] == " "
    ):
        j = 9

    elif (
        tabuleiro[2] != simboloComputador
        and tabuleiro[2] != " "
        and tabuleiro[4] != simboloComputador
        and tabuleiro[4] != " "
        and tabuleiro[5] == " "
    ):
        j = 5
    elif (
        tabuleiro[6] != simboloComputador
        and tabuleiro[6] != " "
        and tabuleiro[2] != simboloComputador
        and tabuleiro[2] != " "
        and tabuleiro[3] == simboloComputador
        and tabuleiro[5] == " "
    ):
        j = 5
    elif (
        tabuleiro[8] != simboloComputador
        and tabuleiro[8] != " "
        and tabuleiro[6] != simboloComputador
        and tabuleiro[6] != " "
        and tabuleiro[3] == " "
    ):
        j = 3
    elif (
        tabuleiro[8] != simboloComputador
        and tabuleiro[8] != " "
        and tabuleiro[6] != simboloComputador
        and tabuleiro[6] != " "
        and tabuleiro[1] == " "
    ):
        j = 1
    elif (
        tabuleiro[8] != simboloComputador
        and tabuleiro[8] != " "
        and tabuleiro[4] != simboloComputador
        and tabuleiro[4] != " "
        and tabuleiro[1] == " "
    ):
        j = 7
    elif (
        tabuleiro[2] != simboloComputador
        and tabuleiro[2] != " "
        and tabuleiro[6] != simboloComputador
        and tabuleiro[6] != " "
        and tabuleiro[3] == " "
    ):
        j = 3
    elif (
        tabuleiro[2] != simboloComputador
        and tabuleiro[2] != " "
        and tabuleiro[4] != simboloComputador
        and tabuleiro[4] != " "
        and tabuleiro[1] == " "
    ):
        j = 1
    elif (
        tabuleiro[1] != simboloComputador
        and tabuleiro[1] != " "
        and tabuleiro[8] != simboloComputador
        and tabuleiro[8] != " "
        and tabuleiro[7] == " "
    ):
        j = 7

    elif (
        tabuleiro[1] == simboloComputador
        and tabuleiro[9] != simboloComputador
        and tabuleiro[3] == " "
    ):
        j = 3
    elif (
        tabuleiro[1] != simboloComputador
        and tabuleiro[1] != " "
        and tabuleiro[5] == " "
    ):
        j = 5
    elif (
        tabuleiro[3] != simboloComputador
        and tabuleiro[3] != " "
        and tabuleiro[5] == " "
    ):
        j = 5
    elif (
        tabuleiro[7] != simboloComputador
        and tabuleiro[7] != " "
        and tabuleiro[5] == " "
    ):
        j = 5
    elif (
        tabuleiro[9] != simboloComputador
        and tabuleiro[9] != " "
        and tabuleiro[5] == " "
    ):
        j = 5
    elif (
        tabuleiro[6] != simboloComputador
        and tabuleiro[6] != " "
        and tabuleiro[3] == " "
    ):
        j = 3

    elif (
        tabuleiro[8] != simboloComputador
        and tabuleiro[8] != " "
        and tabuleiro[7] == " "
    ):
        j = 7
    elif (
        tabuleiro[5] != simboloComputador
        and tabuleiro[5] != " "
        and tabuleiro[9] != simboloComputador
        and tabuleiro[9] != " "
        and tabuleiro[3] == " "
    ):
        j = 3

    elif (
        tabuleiro[5] != simboloComputador
        and tabuleiro[5] != " "
        and tabuleiro[6] != simboloComputador
        and tabuleiro[6] != " "
        and tabuleiro[4] != simboloComputador
        and tabuleiro[4] != " "
        and tabuleiro[2] == " "
    ):
        j = 2

    # Escolha dos espaços vazios
    elif tabuleiro[1] == " ":
        j = 1
    elif tabuleiro[2] == " ":
        j = 2
    elif tabuleiro[5] == " ":
        j = 5
    elif tabuleiro[9] == " ":
        j = 9
    elif tabuleiro[7] == " ":
        j = 7
    elif tabuleiro[3] == " ":
        j = 3
    elif tabuleiro[4] == " ":
        j = 4
    elif tabuleiro[6] == " ":
        j = 6
    elif tabuleiro[8] == " ":
        j = 8
    return j


def verificaVencedor(x, o, c, d, e):
    """
    Recebe os parâmetros "x" e "o", as posições do tabuleiro e verifica se houve uma combinação
    de três posições com o mesmo parâmetro. Por fim, retorna o vencedor (se houver), caso contrário retorna
    None.
    """
    if x == c and x == d and x == e:
        return x
    elif o == c and o == d and o == e:
        return o
    else:
        return None


def verificaJogada(tabuleiro, simbolo, simboloComputador):
    """
    Recebe o tabuleiro e
    imprime se um jogador ('x' ou 'o') venceu a jogada e solicita se o usuário deseja jogar novamente.
    """
    if (
        verificaVencedor(
            simbolo, simboloComputador, tabuleiro[3], tabuleiro[5], tabuleiro[7]
        )
        == simbolo
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[1], tabuleiro[5], tabuleiro[9]
        )
        == simbolo
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[1], tabuleiro[2], tabuleiro[3]
        )
        == simbolo
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[4], tabuleiro[5], tabuleiro[6]
        )
        == simbolo
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[7], tabuleiro[8], tabuleiro[9]
        )
        == simbolo
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[1], tabuleiro[4], tabuleiro[7]
        )
        == simbolo
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[2], tabuleiro[5], tabuleiro[8]
        )
        == simbolo
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[3], tabuleiro[6], tabuleiro[9]
        )
        == simbolo
    ):
        limpaTela()
        imprimetabuleiro(tabuleiro)
        print("Parabéns! Você venceu a partida!")
        escolha = input(
            "Que ótima jogada, meu caro!! Gostaria de jogar novamente? (Digite 'S' para continuar ou qualquer outra tecla para finalizar): "
        )
        if escolha == "S" or escolha == "s":
            programa()
        else:
            quit()
    elif (
        verificaVencedor(
            simbolo, simboloComputador, tabuleiro[3], tabuleiro[5], tabuleiro[7]
        )
        == simboloComputador
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[1], tabuleiro[5], tabuleiro[9]
        )
        == simboloComputador
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[1], tabuleiro[2], tabuleiro[3]
        )
        == simboloComputador
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[4], tabuleiro[5], tabuleiro[6]
        )
        == simboloComputador
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[7], tabuleiro[8], tabuleiro[9]
        )
        == simboloComputador
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[1], tabuleiro[4], tabuleiro[7]
        )
        == simboloComputador
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[2], tabuleiro[5], tabuleiro[8]
        )
        == simboloComputador
        or verificaVencedor(
            simbolo, simboloComputador, tabuleiro[3], tabuleiro[6], tabuleiro[9]
        )
        == simboloComputador
    ):
        limpaTela()
        imprimetabuleiro(tabuleiro)
        print("Que pena! O computador venceu a partida!")
        escolha = input(
            "Às vezes a vida é deveras complexa, meu bom. Gostaria de uma revanche? (Digite 'S' para continuar ou qualquer outra tecla para finalizar): "
        )
        if escolha == "S" or escolha == "s":
            programa()
        else:
            quit()
    elif (
        tabuleiro[1] != " "
        and tabuleiro[2] != " "
        and tabuleiro[3] != " "
        and tabuleiro[4] != " "
        and tabuleiro[5] != " "
        and tabuleiro[6] != " "
        and tabuleiro[7] != " "
        and tabuleiro[8] != " "
        and tabuleiro[9] != " "
    ):
        limpaTela()
        imprimetabuleiro(tabuleiro)
        print("Empate!")
        escolha = input(
            "Gostaria de desempatar esse negócio e deixar clara a sua superioridade? (Digite 'S' para continuar ou qualquer outra tecla para finalizar): "
        )
        if escolha == "S" or escolha == "s":
            programa()
        else:
            quit()


def tabu():
    """
    Gera a lista inicial para construção do tabuleiro.
    """
    l = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    return l


def imprimetabuleiro(l):
    """
    Recebe o tabuleiro e o imprime.
    """
    print(f" {l[7]} | {l[8]} | {l[9]} ")
    print("---+---+---")
    print(f" {l[4]} | {l[5]} | {l[6]} ")
    print("---+---+---")
    print(f" {l[1]} | {l[2]} | {l[3]} ")


def xo():
    """
    Verifica qual símbolo (X ou O) o usuário deseja ser: se escolher "X" então o computador será "O" e vice-versa.
    Retorna o símbolo do usuário e do computador.
    (O programa aceitará X e O minúsculos também)
    """
    simbolo = input("Olá! Qual letra (X ou O) você gostria de ser? ")
    if simbolo != "X" and simbolo != "O" and simbolo != "x" and simbolo != "o":
        print("ERRO! Simbolo inválido!")
        return xo()
    if simbolo == "X":
        simmboloComputador = "O"
    if simbolo == "O":
        simmboloComputador = "X"
    # Minúsculo
    if simbolo == "x":
        simmboloComputador = "o"
    if simbolo == "o":
        simmboloComputador = "x"
    return simbolo, simmboloComputador


def primeiro():
    """
    Escolhe aleatóriamente quem começará jogando e retorna essa escolha.
    """
    escolha = random.choice(["jogador", "computador"])
    return escolha


def lista(posiçao, tabuleiro, simbolo):
    """
    Gera a atualização do tabuleiro conforme o jogo decorre.
    """
    tabuleiro[posiçao] = simbolo
    return tabuleiro


def ocupaçao(tabuleiro, posiçaoo):
    """
    Verifica se a posição que o usuário escolheu já está ocupada.
    Caso esteja, gera uma mensagem de erro e retorna pra escolha da posição novamente.
    """
    if tabuleiro[posiçaoo] != " ":
        print("Posição já ocupada!")
        return posiçao(tabuleiro)
    return posiçaoo


def posiçao(tabuleiro):
    """
    Solicita a escolha da posição do usuário e verifica se ela é válida.
    Se não for válida, exibe uma mensagem de erro e solicita a esolha novamente.
    Por fim, retorna a escolha válida do usuário.
    """
    posiçaoo = input("Escolha qual posição deseja marcar: ")
    if (
        posiçaoo != "1"
        and posiçaoo != "2"
        and posiçaoo != "3"
        and posiçaoo != "4"
        and posiçaoo != "5"
        and posiçaoo != "6"
        and posiçaoo != "7"
        and posiçaoo != "8"
        and posiçaoo != "9"
    ):
        print("ERRO: você deve digitar um número de 1-9!")
        return posiçao(tabuleiro)
    p = int(posiçaoo)
    position = ocupaçao(tabuleiro, p)
    return position


def jogada(tabuleiro, simbolo, simboloComputador):
    """
    Promove o fluxo do jogo quando o usuário é quem começa.
    """
    imprimetabuleiro(tabuleiro)
    posiçaoo = posiçao(tabuleiro)
    t = lista(posiçaoo, tabuleiro, simbolo)
    verificaJogada(tabuleiro, simbolo, simboloComputador)
    compjogada = jogadaComputador(t, simboloComputador)
    t = lista(compjogada, t, simboloComputador)
    verificaJogada(tabuleiro, simbolo, simboloComputador)
    limpaTela()
    return jogada(t, simbolo, simboloComputador)


def jogada2(tabuleiro, simbolo, simboloComputador):
    """
    Promove o fluxo do jogo quando o computador é quem começa.
    """
    compjogada = jogadaComputador(tabuleiro, simboloComputador)
    t = lista(compjogada, tabuleiro, simboloComputador)
    verificaJogada(tabuleiro, simbolo, simboloComputador)
    imprimetabuleiro(t)
    posiçaoo = posiçao(t)
    t = lista(posiçaoo, t, simbolo)
    verificaJogada(tabuleiro, simbolo, simboloComputador)
    limpaTela()
    return jogada2(t, simbolo, simboloComputador)


def jogo(escolha, simbolo, simboloComputador):
    """
    Recebe a escolha de quem começa e os símbolos dos participantes, então direciona o jogo para
    o fluxo 1 ou 2 (jogada e jogada2).
    """
    l = tabu()  # Tabuleiro inicial.
    if escolha == "jogador":
        print("Você começa.")
        jogada(l, simbolo, simboloComputador)
    elif escolha == "computador":
        print("O computador começa.")
        jogada2(l, simbolo, simboloComputador)


def programa():
    """
    Gera os parâmetros básicos para o resto das funções e direciona para o resto do programa.
    """
    limpaTela()
    print("Bem-vindo ao jogo da Velha!")
    simbolo, simboloComputador = xo()
    escolha = primeiro()
    jogo(escolha, simbolo, simboloComputador)


def main():
    limpaTela()
    _ = input("Pressione qualquer tecla para continuar -->")
    programa()


## NÃO ALTERE O CÓDIGO ABAIXO ##
if __name__ == "__main__":
    main()
