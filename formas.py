def circulo():
    raio = float(input("Informe o valor do raio "))
    resultado = (raio * raio) * 3.14
    print(f"A área do círculo é {resultado}")


def triangulo():
    base = float(input("Informe a base "))
    altura = float(input("Informe a altura "))
    resultado = (base * altura) / 2
    print(f"A área do triângulo é {resultado}")


def quadrado():
    lado = float(input("Digite o valor do lado "))
    resultado = lado * lado
    print(f"A área do quadrado é {resultado}")


def retangulo():
    base = float(input("Informe a base do retângulo "))
    altura = float(input("Informe a altura do retângulo "))
    resultado = base * altura
    print(f"A área do retângulo é {resultado}")


def paralelogramo():
    base = float(input("Informe a base do paralelogramo "))
    altura = float(input("Informe a altura do paralelogramo "))
    resultado = base * altura
    print(f"A área do paralelogramo é {resultado}")


def losango():
    diagonal_maior = float(input("Informe a diagonal maior "))
    diagonal_menor = float(input("Informe a diagonal menor "))
    resultado = (diagonal_maior * diagonal_menor) / 2
    print(f"A área do losango é {resultado}")


def trapezio():
    base_maior = float(input("Informe a base maior "))
    base_menor = float(input("Informe a base menor "))
    altura = float(input("Informe a altura "))
    resultado = ((base_maior + base_menor) * altura) / 2
    print(f"A área do trapézio é {resultado}")

     
 
while True:

    print ("Calculo de formas")
    print ("1 - Circulo")
    print ("2 - Triangulo")
    print ("3 - Quadrado")
    print ("4 - Retangulo")
    print ("5 - Paralelogramo")
    print ("6 - Losango")
    print ("7 - Trapezio")
    print ("0 - sair")


    opcao = input("Escolha uma forma: ")
    if opcao == "1":
        circulo()

    elif opcao == "2":
        triangulo()

    elif opcao == "3":
        quadrado()

    elif opcao == "4":
        retangulo()

    elif opcao == "5":
        paralelogramo()

    elif opcao == "5":
        losango()

    elif opcao == "6":
        trapezio()

    elif opcao == "0":
        print("saindo..")
        break

    else:
     print("Opção inválida. Tente novamente.")