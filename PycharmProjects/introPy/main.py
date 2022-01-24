

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
    print_hi('Amanda')

    resultado = calcular_area_do_retangulo(3,4)
    print(f'a área do retângulo é de {resultado} metros')

    resultado = calcular_area_do_quadrado(5)
    print(f'a área do quadrado é de {resultado} metros')

    resultado = calcular_area_do_triangulo(6,7)
    print (f'a área do triângulo é de {resultado} metros')

    contagem_progressiva(11)

    apoiar_candidato('Faker',10)

    brincar_de_plim(100)


