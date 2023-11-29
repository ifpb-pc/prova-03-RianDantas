def q1(cidades):

    list1 = []
  
    for i,j in cidades.items():
        if j > 100:
            list1.append(i)

    return list1

def q2(lista1, lista2):

    maior_soma = 0
    lista_maior = []


    for x in lista1:
        if x > 0:
            maior_soma += x
            lista_maior.append(x)

    for x in lista2:
        if x > 0:
            maior_soma += x
            lista_maior.append(x)
        lista_maior.sort()
    return maior_soma,lista_maior

def q3():
    return[]
  

def ler_valores():
    lista = []
    while True:
        num = int(input("Digite um numero: "))

        if num == 0:
            break

        lista.append(num)
    return lista

def processa_lista():
    list = ler_valores()

    lista_pares = []
    lista_impares = []

    for x in list:
        if x % 2 == 0:
            lista_pares.append(x)

        else:
            lista_impares.append(x)

    print(lista_pares, lista_impares)

def q4(valores):
    return []
def ler_03_alturas():

    alturas = []
    while len(alturas) < 3:
        alt = float(input("Digite uma altura: "))
    
    
        alturas.append(f'{alt:.2f}')

    return alturas



def organizar_alturas():
    lista = ler_03_alturas()
    lista1= []
# 10,20,30            10         20        30
    lista.sort()
    lista1.append(lista[1])
    lista1.append(lista[2])
    lista1.append(lista[0])
    print(lista1)

organizar_alturas()
def main():
    # Teste as questões que você desenvolveu manualmente:
    # idades = {
    #     "João Pessoa": 432,
    #     "Campina Grande": 325,
    #     "Santa Rita": 68,
    #     "Patos": 289,
    #     "Bayeux": 54,
    #     "Sousa": 178,
    #     "Cajazeiras": 201,
    #     "Cabedelo": 45,
    #     "Guarabira": 122,
    #     "Areia": 177,
    # }
    # resultado = q1(idades)
    # print("q1:", resultado)


    # lista1 = [3, -5, 12, 0, -8, 7]
    # lista2 = [-2, 10, -1, 6, -4, 9]
    # resultado = q2(lista1, lista2)
    # print("q2:", resultado)
    
    organizar_alturas()



if __name__ == "__main__":
    main()


