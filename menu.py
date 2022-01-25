

def print_hi(name):
    print(f'Hi, {name}')

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado * lado

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento/2

def contagem_progressiva(fim):
    for numero in range(fim):
        print(numero)

def apoiar_candidato(nome, vezes):
    for numero in range (vezes):

        if numero < 9:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1,'-', nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')

        else:
            print('{:0>50}'.format(numero))


if __name__ == '__main__':

    resposta = "C"

    while resposta.upper() != 'Z':
        print('##################################')
        print('#                                #')
        print('# MENU DE OPÇÕES                 #')
        print('#                                #')
        print('#   1- Olá Mundo !               #')
        print('#   2- Área do retângulo         #')
        print('#   3- Área do quadrado          #')
        print('#   4- Área do triângulo         #')
        print('#   5- Contagem progressiva      #')
        print('#   6- Apoiar candidato          #')
        print('#   7- Brincar de PLIM           #')
        print('#   Z- SAIR                      #')
        print('#                                #')
        print('##################################')

        resposta = input('Escolha sua opção')
        print(f'A sua escolha foi: {resposta}')

        if resposta.upper() != 'Z':
            if resposta == '1':
                print_hi('Amanda')
            elif resposta == '2':
                resultado = calcular_area_do_retangulo(8,7)
                print(f'A área do retângulo é de {resultado} m')
            elif resposta == '3':
                resultado = calcular_area_do_quadrado(6)
                print(f'A área do quatrado é de {resultado}m')
            elif resposta == '4':
                resultado = calcular_area_do_triangulo(5,8)
                print(f'A área do triângulo é de {resultado}m')
            elif resposta == '5':
                contagem_progressiva(11)
            elif resposta == '6':
                apoiar_candidato('Qual será?',10)
            elif resposta == '7':
                brincar_de_plim(50)
            else:
                print('Você digitou uma opção inválida. Escolha uma opção de 1 a 7')



