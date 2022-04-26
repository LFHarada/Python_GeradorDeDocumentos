from random import randint

def gerador_cnpj():

    print("Matriz ou filial?")
    print("1 - Matriz")
    print("2 - Filial")

    try:
        origem = int(input("Número da escolha: "))

        dig1 = randint(0, 9)
        dig2 = randint(0, 9)
        dig3 = randint(0, 9)
        dig4 = randint(0, 9)
        dig5 = randint(0, 9)
        dig6 = randint(0, 9)
        dig7 = randint(0, 9)
        dig8 = randint(0, 9)
        dig9, dig10 = 0, 0

        if origem == 1:
            dig11 = 0
            dig12 = 1
        if origem == 2:
            dig11 = randint(0, 9)
            dig12 = randint(2, 9)

        multdig13 = ((0*6)+(dig1*5)+(dig2*4)+
                     (dig3*3)+(dig4*2)+(dig5*9)+
                     (dig6*8)+(dig7*7)+(dig8*6)+
                     (dig9*5)+(dig10*4)+(dig11*3)+(dig12*2))

        divdig13 = multdig13 % 11

        dig13 = divdig13

        multdig14 = ((dig1*6)+(dig2*5)+(dig3*4)+
                     (dig4*3)+(dig5*2)+(dig6*9)+
                     (dig7*8)+(dig8*7)+(dig9*6)+
                     (dig10*5)+(dig11*4)+(dig12*3)+(dig13*2))


        cpfcompleto = "{}{}.{}{}{}.{}{}{}/{}{}{}{}-{}{}\n".format(
            dig1, dig2, dig3, dig4, dig5, dig6, dig7, dig8, dig9, dig10, dig11, dig12, dig13, dig14
        )
        print(cpfcompleto)
        return cpfcompleto

    except:
        print("Por favor, escolha um número válido.\n")