import random

def criar_labirinto_backtracking(linhas, colunas):
    """Gera um labirinto usando o algoritmo de backtracking recursivo."""
    labirinto = [[1 for _ in range(colunas)] for _ in range(linhas)]
    movimentos = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    def dentro_limites(x, y):
        return 0 <= x < linhas and 0 <= y < colunas

    def gerar_caminho(x, y):
        labirinto[x][y] = 0
        random.shuffle(movimentos)

        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            if dentro_limites(nx, ny) and labirinto[nx][ny] == 1:
                labirinto[x + dx // 2][y + dy // 2] = 0
                gerar_caminho(nx, ny)

    # Escolhe um ponto inicial aleatório em uma célula ímpar
    inicio_x, inicio_y = random.randrange(0, linhas, 2), random.randrange(0, colunas, 2)
    gerar_caminho(inicio_x, inicio_y)
    return labirinto

def gerar_labirinto(dificuldade):
    """Gera o labirinto com base na dificuldade."""
    tamanhos = {"Fácil": 7, "Médio": 10, "Difícil": 13}
    tamanho = tamanhos[dificuldade]
    labirinto = criar_labirinto_backtracking(tamanho, tamanho)

    # Ponto de início e fim
    inicio = (0, 1)  # Entrada no canto superior esquerdo
    fim = (tamanho - 1, tamanho - 2)  # Saída no canto inferior direito

    # Certificar que os pontos de início e fim estão livres
    labirinto[inicio[0]][inicio[1]] = 0
    labirinto[fim[0]][fim[1]] = 0

    return labirinto, inicio, fim

def exibir_labirinto(labirinto, inicio, fim):
    """Exibe o labirinto no console."""
    for x, linha in enumerate(labirinto):
        for y, celula in enumerate(linha):
            if (x, y) == inicio:
                print("I", end=" ")  # Ponto inicial
            elif (x, y) == fim:
                print("F", end=" ")  # Ponto final
            elif celula == 1:
                print("#", end=" ")  # Paredes
            else:
                print(".", end=" ")  # Caminhos livres
        print()