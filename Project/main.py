from geradores.cpf_old import *
from geradores.cnpj import *

print("Bem vindo ao gerador de documentos!")
print("-----------------------------------")
print("Por favor, escolha uma das opções abaixo.\n")

menu_options = {
    1: '1 - Gerador de CPF - CADASTRO DE PESSOAS FÍSICAS',
    2: '2 - Gerador de TE - TÍTULO ELEITORAL',
    3: '3 - Gerador de CN - CERTIDÃO DE NASCIMENTO',
    4: '4 - Gerador de CC - CERTIDÃO DE CASAMENTO',
    5: '5 - Gerador de CO - CERTIDÃO DE ÓBITO',
    6: '6 - Gerador de CNH - CARTEIRA NACIONAL DE HABILITAÇÃO',
    7: '7 - Gerador de PIS',
    8: '8 - Gerador de CNPJ - CADASTRO NACIONAL DE PESSOAS JURÍDICAS',
    9: '9 - Gerador de PLACA VEICULAR',
    10: '10 - Gerador de RENAVAM',
    11: '11 - Gerador de CARTÃO DE CRÉDITO',
    99: '99 - Exit\n',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    gerador_cpf()


def option2():
    gerador_cnpj()


def option3():
    pass


if __name__ == '__main__':

    while(True):

        print_menu()
        option = ''

        try:
            option = int(input('Enter your choice: '))

        except:
            print('Wrong input. Please enter a number ...')

        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Opção inválida, por favor, escolha corretamente.')

