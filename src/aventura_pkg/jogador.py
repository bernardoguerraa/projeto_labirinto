import keyboard

def mover_jogador(labirinto, inicio, fim):
    """permite que o jogador se mova pelo labirinto usando o teclado.
    
    essa função exibe o labirinto no console e permite que o jogador use as teclas w, a, s e d para
    se mover pelo labirinto. o jogador começa no ponto de início e deve tentar chegar no ponto final.
    se o jogador tentar se mover para uma parede, o movimento não será permitido.
    
    args:
        labirinto (list): a matriz 2d representando o labirinto, onde 1 é parede e 0 é caminho livre.
        inicio (tuple): as coordenadas (x, y) do ponto de entrada do labirinto.
        fim (tuple): as coordenadas (x, y) do ponto de saída do labirinto.
    """
    posicao_atual = list(inicio)  # converte para lista para modificar as coordenadas
    linhas = len(labirinto)
    colunas = len(labirinto[0])

    def exibir_labirinto_com_jogador():
        """exibe o labirinto com o jogador no console.
        
        essa função imprime o labirinto no console, substituindo a posição do jogador pela letra 'P'
        e exibindo o ponto final como 'F'.
        """
        for x, linha in enumerate(labirinto):
            for y, celula in enumerate(linha):
                if (x, y) == tuple(posicao_atual):
                    print("P", end=" ")  # representa o jogador
                elif (x, y) == fim:
                    print("F", end=" ")  # representa o fim
                elif celula == 1:
                    print("#", end=" ")  # representa as paredes
                else:
                    print(".", end=" ")  # representa os caminhos livres
            print()  # nova linha após cada linha do labirinto

    print("use as teclas w (cima), a (esquerda), s (baixo), d (direita) para se mover. pressione q para sair.")
    while True:
        exibir_labirinto_com_jogador()  # exibe o labirinto com a posição do jogador
        print(f"posição atual: {tuple(posicao_atual)}\n")
        key = keyboard.read_event(suppress=True).name  # captura o evento do teclado

        if key == "q":  # sair do jogo
            print("jogo encerrado.")
            break

        # movimentos: w (cima), a (esquerda), s (baixo), d (direita)
        nova_posicao = posicao_atual[:]
        if key == "w" and posicao_atual[0] > 0:  # cima
            nova_posicao[0] -= 1
        elif key == "s" and posicao_atual[0] < linhas - 1:  # baixo
            nova_posicao[0] += 1
        elif key == "a" and posicao_atual[1] > 0:  # esquerda
            nova_posicao[1] -= 1
        elif key == "d" and posicao_atual[1] < colunas - 1:  # direita
            nova_posicao[1] += 1

        # verifica se o movimento é válido (não pode atravessar paredes)
        if labirinto[nova_posicao[0]][nova_posicao[1]] == 0:
            posicao_atual = nova_posicao  # só faz o movimento se a célula for livre

        # verifica se o jogador alcançou o final
        if tuple(posicao_atual) == fim:
            print("parabéns! você encontrou a saída!")
            break