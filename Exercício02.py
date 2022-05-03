login = "email@gmail.com"
senha = "123456"
cond = 0
vali = 0

cond = int(input("Olá!\nO que deseja fazer?\n (1) Login\n (2) Cadastrar\n (0) Finalizar operação\n"))

while cond != 0:
    while cond == 1 and vali <= 3:
        verif_login = input("Digite o Login: ")
        verif_senha = input("Digite a senha: ")
        if login == verif_login and senha == verif_senha:
            print("\nLogin efetuado com sucesso")
            cond = 0
            break
        else:
            print("\nLogin ou senha inválidos!")
            vali += 1
            if vali == 3:
                print("\nVocê terminou o numero de tentativas. Redefina o login e senha.\n")
                cond = 2
    if cond == 2:
        login = input("Digite o novo Login: ")
        senha = input("Digite a nova senha: ")
        cond = int(input("Olá!\nO que deseja fazer?\n (1) Login\n (2) Cadastrar\n (0) Finalizar operação\n"))
        vali = 0
if cond == 0:
    print("Operação finalizada...")