# ESTACIONAMENTO

# Códigos ANSI para cores.
from cores import VERDE, VERMELHO, AMARELO, RESET

from Entrada.entrada import entrada
from Saida.saida import saida

while True:
    print("=================================")
    print(f" --- {AMARELO}Estacionamento - Entrada --- {RESET}")
    print("=================================\n")

    opcao_inicial = int(input("""[1] - Entrar
[2] - Sair
Selecinar opção: """))

    if opcao_inicial == 1:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(" --- Selecionar vaga --- ")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-")
        entrada()
        continue #Para continuar o loop.
    elif opcao_inicial == 2:
        saida()
        continue  # Volta ao menu principal