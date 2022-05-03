print("EXERCICIO 03 CHECKPOINT\n")

contador = 1
conta = 0

numero = int(input("Digite o numero que deseja ver a tabuada:"))

while(contador <= 10):
    conta = contador * numero
    print(f"{numero} X {contador} = {conta}")
    contador += 1
    