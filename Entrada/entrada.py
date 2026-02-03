from cores import RESET, VERDE, VERMELHO

vagas_ocupadas = [] #Lista para maracar vagas já ocupadas.

def entrada():
    while True: #Laço infinito.

      # ----- MOSTRAR O MAPA DE VAGAS -----
        for letras in "ABCDEFGHIJ": #Escreve as letras de A-J.
            for i in range (1,11): #Escreve os números de 1-10.
                vaga_atual = (f"{letras}{i}") #Formato de impressão das vagas (Letra - Número).

                #Verifica se alguma vaga impressa está na lista 'vagas_ocupadas' e define a cor .
                if vaga_atual in vagas_ocupadas:
                    cor = VERMELHO
                else:
                    cor = VERDE
                #Imprime a cor das vagas baseado nas cores da estrutura de repetição anterior.
                print(f"{cor}{vaga_atual}{RESET}", end=' ')
            print() #A cada número final imprimido (10) é esaltado uma linha para o a próxima linha do loop.

        #Variável para guaradar vaga selecioanada pelo usuário deixando todos os caracteres maiúsculos (.upper()) e retirando qualquer espaço digitado (.strip()).
        vaga_escolhida = input("Selecione a vaga desejada: ").upper().strip()

        # Verifica se o tamanho é válido (Se a vaga digitada tem tamanho de dois ou três caracteres).
        if len(vaga_escolhida) not in (2, 3):
            print(f"{VERMELHO}Formato inválido. Use algo como A1, B10...{RESET}")
            continue

        # Primeiro caractere deve ser a letra da vaga.
        letra = vaga_escolhida[0]
        # O restante deve ser o número (pode ter 1 ou 2 dígitos).
        numero_str = vaga_escolhida[1:]

        # Confere se a letra está entre A-J.
        if letra not in "ABCDEFGHIJ":
            print(f"{VERMELHO}Letra inválida. Use de A-J.{RESET}")
            continue

        # Confere se a parte numérica é realmente número.
        if not numero_str.isdigit():
            print(f"{VERMELHO}Número inválido. Use de 1-10.{RESET}")
            continue

        # Confere se o número está no intervalo permitido.
        if int(numero_str) < 1 or int(numero_str) > 10:
            print(f"{VERMELHO}Número fora do intervalo (1 a 10).{RESET}")
            continue

        # Verifica se a vaga já está ocupada.
        if vaga_escolhida in vagas_ocupadas:
            print(f"{VERMELHO}Vaga ocupada, por favor escolha outra.{RESET}")
            continue

        #Variável para guardar caracteres da placa digitadas pelo usuário deixando todos os caracteres maiúsculos (.upper()) e retirando qualquer espaço digitado (.strip()).
        placa_carro = input("Digite a placa do carro: ").upper().strip()
        
        # Valida se a placa foi digitada.
        if placa_carro == "":
            print(f"{VERMELHO}É necessário informar a placa do carro para proseguir.{RESET}")
            continue

        #A lista "vagas_ocupadas" começa com tamanho '0' e com o ".append" ela aumenta de tamanho baseado nos caracteres guardados pela variável (vaga_escolhida), aumentando a cada loop.
        vagas_ocupadas.append(vaga_escolhida)
        
        print(f"Vaga {VERMELHO}{vaga_escolhida}{RESET} ocupada para o carro {placa_carro}!\nPode prosseguir para a vaga!\n")
        break  # Sai do while True e retorna ao menu principal.
