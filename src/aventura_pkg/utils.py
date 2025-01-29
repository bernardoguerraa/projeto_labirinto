def exibir_menu():
    print("Bem vindo ao Jogo do Labirinto, vamos começar! Escolha um dos números das opções:")
    print("1 - Jogar")
    print("2 - Instruções")
    print("3 - Sobre o Projeto")
    print("4 - Sair do Jogo")


def capturar_resposta():
    while True:
        resposta = input("Digite sua opção: ")
        match resposta:
            case "1":
                return "Jogar"
            case "2":
                return "Instruções"
            case "3":
                return "Sobre"
            case "4":
                return "Sair"
            case _:
                print("Opção inválida, escolha um número entre 1, 2, 3 e 4.")
                
                

def exibir_instrucoes():
    """exibe as instruções detalhadas de como jogar o jogo."""
    print("Instruções de Jogo:")
    print("1. O objetivo do jogo é sair do labirinto, começando no ponto de entrada e chegando até a saída.")
    print("2. Para se mover pelo labirinto, utilize as teclas W, A, S e D:")
    print("   - W: mover para cima (cima)")
    print("   - A: mover para a esquerda")
    print("   - S: mover para baixo (baixo)")
    print("   - D: mover para a direita")
    print("3. O jogador pode se mover apenas pelas células que são caminhos livres (representadas por '.').")
    print("4. Cuidado! Não é possível atravessar as paredes do labirinto (representadas por '#').")
    print("5. O jogo termina quando o jogador alcança a saída, que está marcada com 'F'.")
    print("6. Para sair do jogo a qualquer momento, pressione a tecla 'Q'.")
    print("Boa sorte e divirta-se!")
    
    # Tecla para voltar ao menu
    input("\nPressione enter para voltar ao menu...")

def exibir_sobre():
    """exibe informações sobre o projeto."""
    print("Este jogo foi desenvolvido por Bernardo Guerra, estudante de Engenharia de Computação pela Universidade Federal de Itajubá\n"
          "e estudante de programação pelo Projeto Desenvolve - Itabira. O jogo conta com conceitos básicos, porém muito importantes para\n"
          "qualquer aplicação em Python, como: Modularização, funções recursivas, estruturas de controle, controle de fluxo e muito mais.\n"
          "Além disso, o projeto foi feito com boa escalabilidade, de maneira que, futuramente, novas funcionalidades possam ser adicionadas\n"
          "facilmente. Durante o desenvolvimento, foram seguidas boas práticas de codificação, como a escolha de nomes significativos para\n"
          "variáveis e funções, a indentação correta do código e a utilização de comentários. Divirta-se!")

    input("\nPressione enter para voltar ao menu...")
