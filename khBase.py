from kahoot import client as account
from os import system

bots = []

def add_bots(pin, name, n):
    print(f"\n Enviando {n} bots para {pin}...")
    n = int(n)
    index = 0
    while(index != n):
        bot = account()
        bot.join(pin, f"{name}{index + 1}")
        bots.append(bot)
        index += 1
    print(" Bots enviados!")

def leave_room():
    print("\n Removendo bots...")
    auth = True
    for bot in bots:
        try:
            bot.leave()
        except:
            print("ERRO: OS BOTS NÃO ESTÃO EM UMA SALA EXISTENTE")
            auth = False
            break  
    bots.clear()
    if(auth == True):
        print(" Bots removidos!")

def main():
    system("cls")
    auth = False

    print("#=----------------------------=#\n       Killhoot (Portable) V1\n          by madmattp\n ")
    pin = input(" Insira o Pin da sala >")
    name = input(" Insira o nome dos bots >")

    while(auth == False):
        try:
            n = int(input(" Insira o número de bots >"))
            auth = True
        except:
            print("ERRO: O VALOR DE 'NÚMERO DE BOTS' DEVE SER UM NÚMERO INTEIRO. ")
            auth = False

    add_bots(pin, name, n)
    input("(PRESSIONE ENTER PARA REMOVER OS BOTS DA SALA)")
    leave_room()
    input("(PRESSIONE ENTER PARA VOLTAR AO INÍCIO...)")
    main()

if(__name__ == "__main__"):
    main()
