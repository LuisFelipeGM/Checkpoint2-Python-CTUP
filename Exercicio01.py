print("EXERCICIO 01 CHECKPOINT\n")

tipo = input("Digite a operação que deseja realizar!\n(a) Adição\n(b) Subtração\n(c) Multiplicação\n(d) Divisão\n")

continuar = 1
x = 0
y = 0


while(continuar == 1):
    # ADIÇÃO
    if (tipo == "a"):

        num1 = int(input("Digite o valor do primeiro numero: "))
        num2 = int(input("Digite o valor do segundo numero: "))

        #MAIOR E MENOR
        
        if(num1 >= num2):
            x = num1
            y = num2
        if(num1 <= num2):
            x = num2
            y = num1

        total = num1 + num2
        print(f"O valor da Soma foi de {total}")
        continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
        if (continuar == 2):
            print("Programa Encerrado!")
            break
        while(continuar == 1):
            cond = input("Digite a operação que deseja realizar com a soma anterior!\n(a) Adição\n(b) Subtração\n(c) Multiplicação\n(d) Divisão\n")

            if(cond == "a"):
                num1 = int(input("\nDigite o valor do numero: "))                
                total += num1
                print(f"O valor da Soma foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            if(cond == "b"):
                num1 = int(input("\nDigite o valor do numero: "))
                total -= num1
                print(f"O valor da Subtração foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            if(cond == "c"):
                num1 = int(input("\nDigite o valor do numero: "))
                total *= num1
                print(f"O valor da Multiplicação foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            if(cond == "d"):
                num1 = int(input("\nDigite o valor do numero: "))
                total /= num1
                print(f"O valor da Divisão foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break

            if(num1 > x):
                x = num1
            else:
                y = num1

    # SUBTRAÇÃO
    if (tipo == "b"):
    
        num1 = int(input("Digite o valor do primeiro numero: "))
        num2 = int(input("Digite o valor do segundo numero: "))
        total = num1 - num2
        print(f"O valor da Subtração foi de {total}")
        continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
        if (continuar == 2):
            print("Programa Encerrado!")
            break
        while(continuar == 1):
            cond = input("Digite a operação que deseja realizar com a soma anterior!\n(a) Adição\n(b) Subtração\n(c) Multiplicação\n(d) Divisão\n")

            if(cond == "a"):
                num1 = int(input("\nDigite o valor do numero: "))
                total += num1
                print(f"O valor da Soma foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            if(cond == "b"):
                num1 = int(input("\nDigite o valor do numero: "))
                total -= num1
                print(f"O valor da Subtração foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            if(cond == "c"):
                num1 = int(input("\nDigite o valor do numero: "))
                total *= num1
                print(f"O valor da Multiplicação foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            if(cond == "d"):
                num1 = int(input("\nDigite o valor do numero: "))
                total /= num1
                print(f"O valor da Divisão foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break

            if(num1 > x):
                x = num1
            else:
                y = num1

    # MULTIPLICAÇÃO
    if (tipo == "c"):
    
        num1 = int(input("Digite o valor do primeiro numero: "))
        num2 = int(input("Digite o valor do segundo numero: "))
        total = num1 * num2
        print(f"O valor da Multiplicação foi de {total}")
        continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
        
        if (continuar == 2):
            print("Programa Encerrado!")
            break
        while(continuar == 1):
            cond = input("Digite a operação que deseja realizar com a soma anterior!\n(a) Adição\n(b) Subtração\n(c) Multiplicação\n(d) Divisão\n")

            if(cond == "a"):
                num1 = int(input("\nDigite o valor do numero: "))
                total += num1
                print(f"O valor da Soma foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            if(cond == "b"):
                num1 = int(input("\nDigite o valor do numero: "))
                total -= num1
                print(f"O valor da Subtração foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            if(cond == "c"):
                num1 = int(input("\nDigite o valor do numero: "))
                total *= num1
                print(f"O valor da Multiplicação foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            if(cond == "d"):
                num1 = int(input("\nDigite o valor do numero: "))
                total /= num1
                print(f"O valor da Divisão foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            
            if(num1 > x):
                x = num1
            else:
                y = num1

    # DIVISÃO
    if (tipo == "d"):
    
        num1 = int(input("Digite o valor do primeiro numero: "))
        num2 = int(input("Digite o valor do segundo numero: "))
        total = num1 / num2
        print(f"O valor da Divisão foi de {total}")
        continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
        if (continuar == 2):
            print("Programa Encerrado!")
            break
        while(continuar == 1):
            cond = input("Digite a operação que deseja realizar com a soma anterior!\n(a) Adição\n(b) Subtração\n(c) Multiplicação\n(d) Divisão\n")

            if(cond == "a"):
                num1 = int(input("\nDigite o valor do numero: "))
                total += num1
                print(f"O valor da Soma foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            if(cond == "b"):
                num1 = int(input("\nDigite o valor do numero: "))
                total -= num1
                print(f"O valor da Subtração foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            if(cond == "c"):
                num1 = int(input("\nDigite o valor do numero: "))
                total *= num1
                print(f"O valor da Multiplicação foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            if(cond == "d"):
                num1 = int(input("\nDigite o valor do numero: "))
                total /= num1
                print(f"O valor da Divisão foi de {total}")
                continuar = int(input("Deseja continuar? (1) Sim e (2) Não\n"))
                if (continuar == 2):
                    print("Programa Encerrado!")
                    break
            
            if(num1 > x):
                x = num1
            else:
                y = num1

print(f"O Total foi de {total}\nO maior numero digitado foi {x}\nO menor numero digitado foi {y}")

                

