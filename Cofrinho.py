from os import system, name


def limpaTela():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def space():
    """
    Prints a message on the screen and "inputs" any symbol
    to continue the program.
    """
    _ = input("--> press enter to continue")


def deposito(valdep=0, n100=0, n50=0, n20=0, n10=0, n5=0, n2=0, n1=0, i=0):
    """
    Calculates the amount that will be deposited in the piggy bank, as well as performs a verification
    and counting the bills used.
    """
    CYAN = "\033[36m"
    RST = "\033[00m"
    if i == 0:
        print(f"{CYAN}ENTER '0' TO FINISH THE DEPOSIT{RST}")
    val = int(input("Enter the bill to be deposited: "))
    if val == 0:
        return valdep, n100, n50, n20, n10, n5, n2, n1
    elif (
        val != 100
        and val != 50
        and val != 20
        and val != 10
        and val != 5
        and val != 2
        and val != 1
    ):
        print("ERROR: Invalid bill!")
        return deposito(valdep, n100, n50, n20, n10, n5, n2, n1, i=1)
    else:
        if val == 100:
            n100 += 1
        elif val == 50:
            n50 += 1
        elif val == 20:
            n20 += 1
        elif val == 10:
            n10 += 1
        elif val == 5:
            n5 += 1
        elif val == 2:
            n2 += 1
        elif val == 1:
            n1 += 1
        return deposito(valdep + val, n100, n50, n20, n10, n5, n2, n1, i=1)


def countt(x, valor):
    """
    It counts the amount of bills and prints them on the screen.
    """
    if x > 0:
        print(f"{valor:.2f}")
        x -= 1
        countt(x, valor)


def venotas(val, n, p, sac, conta=0):
    """
    Checks if the amount to be withdrawn is greater than or equal to the value of the respective bills in sequence.
    It also checks the amount of bills used. So, it returns the value the user already has at hand and
    the amount of bills being analyzed.
    """
    if val >= p and n > 0 and sac + p <= val:
        n -= 1
        sac = p + sac
        conta += 1
        return venotas(val, n, p, sac, conta)
    else:
        return sac, n, conta


def saque(val, qtd100, qtd50, qtd20, qtd10, qtd5, qtd2, qtd1):
    """
    Checks if the amount the user has in hand already satisfies the amount he wants to withdraw.
    If not possible then displays an error message. Also calls the "countt" function.
    """
    sac = 0
    conta100 = 0
    conta50 = 0
    conta20 = 0
    conta10 = 0
    conta5 = 0
    conta2 = 0
    conta1 = 0
    if sac < val and sac + 100 <= val:
        sac, qtd100, conta100 = venotas(val, qtd100, 100, sac)
    if sac < val and sac + 50 <= val:
        sac, qtd50, conta50 = venotas(val, qtd50, 50, sac)
    if sac < val and sac + 20 <= val:
        sac, qtd20, conta20 = venotas(val, qtd20, 20, sac)
    if sac < val and sac + 10 <= val:
        sac, qtd10, conta10 = venotas(val, qtd10, 10, sac)
    if sac < val and sac + 5 <= val:
        sac, qtd5, conta5 = venotas(val, qtd5, 5, sac)
    if sac < val and sac + 2 <= val:
        sac, qtd2, conta2 = venotas(val, qtd2, 2, sac)
    if sac < val and sac + 1 <= val:
        sac, qtd1, conta1 = venotas(val, qtd1, 1, sac)
    if sac < val:
        print("ERROR: Insufficient bills!")
        sac = 0
        return sac, qtd100, qtd50, qtd20, qtd10, qtd5, qtd2, qtd1
    else:
        countt(conta100, 100)
        countt(conta50, 50)
        countt(conta20, 20)
        countt(conta10, 10)
        countt(conta5, 5)
        countt(conta2, 2)
        countt(conta1, 1)
        return val, qtd100, qtd50, qtd20, qtd10, qtd5, qtd2, qtd1


def operaçao(saldo=188, c100=1, c50=1, c20=1, c10=1, c5=1, c2=1, c1=1):
    """
    Prints a simple menu on the screen so the user can choose the option
    of action you want. So, after accepting the chosen option, it continues the processes
    corresponding to the option chosen by the user.
    """
    limpaTela()
    RED = "\033[31m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RST = "\033[00m"
    print(YELLOW)
    print("+" + "-" * 19 + "+")
    print("|" + " " * 19 + "|")
    print("| 1 - Deposit       |")
    print("| 2 - Withdraw      |")
    print("| 3 - Balance       |")
    print("| 4 - Report        |")
    print("| 5 - Quit          |")
    print("|" + " " * 19 + "|")
    print("+" + "-" * 19 + "+")
    print(RST)
    opçao = input("Select an option ")
    if opçao == "1":
        print(f"{YELLOW}|Deposit|{RST}")
        val, n100, n50, n20, n10, n5, n2, n1 = deposito()
        print(f"Amount deposited = {GREEN}R${val:.2f}{RST}")
        space()
        operaçao(
            saldo + val,
            c100 + n100,
            c50 + n50,
            c20 + n20,
            c10 + n10,
            c5 + n5,
            c2 + n2,
            c1 + n1,
        )
    elif opçao == "2":
        print(f"{YELLOW}|Withdraw|{RST}")
        print()
        print("BILLS AVAILABLE ON THE MACHINE")
        print("." + "-" * 13 + ".")
        if c100 > 0:
            print(f"|{c100} x R$100,00 |")
        if c50 > 0:
            print(f"|{c50} x R$50,00  |")
        if c20 > 0:
            print(f"|{c20} x R$20,00  |")
        if c10 > 0:
            print(f"|{c10} x R$10,00  |")
        if c5 > 0:
            print(f"|{c5} x R$5,00   |")
        if c2 > 0:
            print(f"|{c2} x R$2,00   |")
        if c1 > 0:
            print(f"|{c1} x R$1,00   |")
        print("." + "-" * 13 + ".")
        val = int(input("Enter an amount to be withdrawn: R$"))
        if val < 0:
            print("ERROR: You cannot withdraw a negative value!")
            space()
            operaçao(saldo, c100, c50, c20, c10, c5, c2, c1)
        if val > saldo:
            all = input(
                "ERROR: Insufficient balance! Would you like to withdraw the entire amount contained in the piggy bank? (N/S):"
            )
            if all == "s" or all == "S":
                countt(c100, 100)
                countt(c50, 50)
                countt(c20, 20)
                countt(c10, 10)
                countt(c5, 5)
                countt(c2, 2)
                countt(c1, 1)
                print(f"Amount withdrawn = {RED}R${saldo:.2f}{RST}")
                space()
                operaçao(saldo=0, c100=0, c50=0, c20=0, c10=0, c5=0, c2=0, c1=0)
            else:
                space()
                operaçao(saldo, c100, c50, c20, c10, c5, c2, c1)
        valsac, n100, n50, n20, n10, n5, n2, n1 = saque(
            val, c100, c50, c20, c10, c5, c2, c1
        )
        print(f"Amount withdrawn = {RED}R${valsac:.2f}{RST}")
        space()
        operaçao(saldo - valsac, n100, n50, n20, n10, n5, n2, n1)
    elif opçao == "3":
        print(f"{YELLOW}|Balance|{RST}")
        print(f"Balance: {GREEN}R${saldo:.2f}{RST}")
        space()
        operaçao(saldo, c100, c50, c20, c10, c5, c2, c1)
    elif opçao == "4":
        print(f"{YELLOW}|Report|{RST}")
        print(f"{CYAN}Bills of R$100,00:{RST} {c100}")
        print(f"{CYAN}Bills of  R$50,00:{RST} {c50}")
        print(f"{CYAN}Bills of  R$20,00:{RST} {c20}")
        print(f"{CYAN}Bills of  R$10,00:{RST} {c10}")
        print(f"{CYAN}Bills of   R$5,00:{RST} {c5}")
        print(f"{CYAN}Bills of   R$2,00:{RST} {c2}")
        print(f"{CYAN}Bills of   R$1,00:{RST} {c1}")
        print(f"\nTotal balance = {GREEN}R${saldo:.2f}{RST}")
        space()
        operaçao(saldo, c100, c50, c20, c10, c5, c2, c1)
    elif opçao == "5":
        if saldo > 0:
            escolha = input(
                "Would you like to withdraw all the money from the piggy bank? (N/S): "
            )
            if escolha == "s" or escolha == "S":
                print(f"Amount withdrawn = {RED}R${saldo:.2f}{RST}")
                limpaTela()
                exit()
            else:
                limpaTela()
                exit()
        else:
            print(
                "You have no balance to withdraw for the time being. Check back often!"
            )
            limpaTela()
            exit()
    else:  # Redirect the program to the beginning of the case the user chooses an option that does not exist.
        print("ERROR: Invalid option!")
        space()
        operaçao(saldo, c100, c50, c20, c10, c5, c2, c1)


def main():
    operaçao()


main()
