#ESTACIONAMNETO - PAGAMENTO
from cores import VERDE, VERMELHO, AMARELO, RESET

def saida():
    F_VERMELHO = "\033[1;41m"

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" --- Pagar estacionamento --- ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    while True:
        placa_carro1 = input("Digite a placa do carro: ")
        
        print()
        print(f"""{F_VERMELHO}ATENÇÃO: O VALOR DO ESTACIONAMENTO COMEÇA A SER COBRADO A PARTIR DE 60 MINUTOS DE OCUPAÇÃO,
        APÓS ISSO, A CADA 60 MINUTOS O VALOR É RECALCULADO COM UMA BASE DE VALOR POR HORA!{RESET}""")
        
        print()
        opcao_saida = input("""[1] - Prosseguir para o pagamento
[2] - Voltar
Selecionar opção: """)

        if opcao_saida == "1":
                print("PARTE POR FAZER, SERÁ COMPLETA MUITO EM BREVE!")
                break  # Sai do loop e retorna ao menu principal
        elif opcao_saida == "2":
                continue  # Volta a perguntar a placa do carro
        else:
                print("Opção inválida. Tente novamente.")
                continue
