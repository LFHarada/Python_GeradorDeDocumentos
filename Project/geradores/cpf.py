from random import randint


def gerador_cpf():
    print("Qual o estado de origem do CPF?\n")
    print("0 – RS")
    print("1 – DF, GO, MS, MT e TO")
    print("2 – AC, AM, AP, PA, RO e RR")
    print("3 – CE, MA e PI")
    print("4 – AL, PB, PE, RN")
    print("5 – BA e SE")
    print("6 – MG")
    print("7 – ES e RJ")
    print("8 – SP")
    print("9 – PR e SC")
    print("10 - ALEATORIO")
    print("11 - SAIR\n")

    try:
        escolha = int(input("Número da escolha: "))

        dig1 = randint(0, 9)
        dig2 = randint(0, 9)
        dig3 = randint(0, 9)
        dig4 = randint(0, 9)
        dig5 = randint(0, 9)
        dig6 = randint(0, 9)
        dig7 = randint(0, 9)
        dig8 = randint(0, 9)

        # Escolha estado específico ou aleatório
        if escolha:
            if escolha in range(0, 9):
                dig9 = escolha
            if escolha == 10:
                dig9 = randint(0, 9)
        else:
            pass

        # Primeiro dígito verificador
        multdig10 = ((dig1*10)+(dig2*9)+(dig3*8)+
                     (dig4*7)+(dig5*6)+(dig6*5)+
                     (dig7*4)+(dig8*3)+(dig9*2))

        divdig10 = multdig10 % 11

        if divdig10 == 0 | divdig10 == 1:
            dig10 = 0
        if 3 <= divdig10 <= 10:
            dig10 = 11 - divdig10

        # Segundo dígito verificador
        multdig11 = ((dig2*10)+(dig3*9)+(dig4*8)+
                     (dig5*7)+(dig6*6)+(dig7*5)+
                     (dig8*4)+(dig9*3)+(dig10*2))

        divdig11 = multdig11 % 11

        if divdig11 == 0 | divdig11 == 1:
            dig11 = 0
        if 3 <= divdig11 <= 10:
            dig11 = 11 - divdig11

        cpfcompleto = "{}{}{}.{}{}{}.{}{}{}-{}{}\n".format(
            dig1, dig2, dig3, dig4, dig5, dig6, dig7, dig8, dig9, dig10, dig11
        )
        print(cpfcompleto)
        return cpfcompleto

    except:
        print("Por favor, escolha um número válido.\n")


gerador_cpf()
