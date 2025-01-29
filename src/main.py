from aventura_pkg.utils import exibir_menu, exibir_sobre, exibir_instrucoes, capturar_resposta
from aventura_pkg.labirinto import gerar_labirinto, exibir_labirinto
from aventura_pkg.jogador import mover_jogador

def menu():
    """exibe o menu principal e gerencia a navegação entre as opções."""
    while True:
        exibir_menu()  # exibe o menu inicial
        opcao = capturar_resposta()  # captura a resposta do usuário

        match opcao:  # usa o match para verificar qual opção foi escolhida
            case "Jogar":  # opção para iniciar o jogo
                # solicita que o jogador escolha a dificuldade do jogo
                print("Escolha a dificuldade do jogo: \n"
                      "1 - Fácil \n"
                      "2 - Médio \n"
                      "3 - Difícil")
                dificuldade = input()  # recebe a entrada do jogador para a dificuldade

                # mapeia a opção escolhida para o nome da dificuldade
                dificuldades = {"1": "Fácil", "2": "Médio", "3": "Difícil"}
                dificuldade_selecionada = dificuldades.get(dificuldade)

                # se a opção de dificuldade for inválida, exibe uma mensagem e retorna ao menu
                if not dificuldade_selecionada:
                    print("Opção inválida. Tente novamente.")
                    continue  # volta para o menu

                # gera o labirinto com a dificuldade selecionada
                labirinto, inicio, fim = gerar_labirinto(dificuldade_selecionada)

                # exibe o labirinto gerado no console
                exibir_labirinto(labirinto, inicio, fim)

                # inicia a movimentação do jogador dentro do labirinto
                mover_jogador(labirinto, inicio, fim)

            case "Sobre":  # opção para exibir informações sobre o projeto
                exibir_sobre()  # exibe informações sobre o projeto

            case "Instruções":  # opção para exibir as instruções de como jogar
                exibir_instrucoes()  # exibe as instruções do jogo

            case "Sair":  # opção para sair do jogo
                print("Obrigado por jogar! Até a próxima!")  # mensagem de despedida
                break  # encerra o loop e o programa

# chama a função menu se este script for executado diretamente
if __name__ == "__main__":
    menu()