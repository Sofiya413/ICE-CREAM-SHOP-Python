f = 0
p = 0
ice_type = ""
total = 0


def cone():
    print("\nYou selected Cone Ice")
    flavor()
    price()


def cup():
    print("\nYou selected Cup Ice")
    cflavor()
    price()


def stick():
    print("\nYou selected Stick Ice")
    sflavor()
    price()


def flavor():
    global f
    print('\nAVAILABLE FLAVORS')
    print('B - Butterscotch\nC - Chocolate\nS - Strawberry\nV - Vanilla\n')
    fav = input("Please choose your flavor : ")
    if fav == 'v' or fav == 'V':
        f = 'VANILLA     '
        print("\nYou selected Vanilla flavor.")
    elif fav == 'c' or fav == 'C':
        f = 'CHOCOLATE   '
        print("\nYou selected Chocolate flavor.")
    elif fav == 's' or fav == 'S':
        f = 'STRAWBERRY  '
        print("\nYou selected Strawberry flavor.")
    elif fav == 'b' or fav == 'B':
        f = 'BUTTERSCOTCH'
        print("\nYou selected Butterscotch flavor.")
    else:
        print('\nPlease enter valid key.')
        flavor()


def cflavor():
    global f
    print('\nAVAILABLE FLAVORS')
    print('B - Butterscotch\nC - Chocolate\nP - Pista\nS - Strawberry\nV - Vanilla\n')
    fav = input("Please choose your flavor : ")
    if fav == 'v' or fav == 'V':
        print("\nYou selected Vanilla flavor.")
        f = 'VANILLA     '
    elif fav == 'c' or fav == 'C':
        print("\nYou selected Chocolate flavor.")
        f = 'CHOCOLATE   '
    elif fav == 's' or fav == 'S':
        print("\nYou selected Strawberry flavor.")
        f = 'STRAWBERRY  '
    elif fav == 'b' or fav == 'B':
        print("\nYou selected Butterscotch flavor.")
        f = 'BUTTERSCOTCH'
    elif fav == 'p' or fav == 'P':
        print("\nYou selected Pista flavor.")
        f = 'PISTA       '
    else:
        print('\nPlease enter valid key.')
        cflavor()


def sflavor():
    global f
    print('\nAVAILABLE FLAVORS')
    print('B - Butterscotch\nC - Choco Bar\nP - Pista\nS - Strawberry\nV - Vanilla\n')
    fav = input("Please choose your flavor : ")
    if fav == 'v' or fav == 'V':
        print("\nYou selected Vanilla flavor.")
        f = 'VANILLA     '
    elif fav == 'c' or fav == 'C':
        print("\nYou selected Chocolate flavor.")
        f = 'CHOCO BAR   '
    elif fav == 's' or fav == 'S':
        print("\nYou selected Strawberry flavor.")
        f = 'STRAWBERRY  '
    elif fav == 'b' or fav == 'B':
        print("\nYou selected Butterscotch flavor.")
        f = 'BUTTERSCOTCH'
    elif fav == 'p' or fav == 'P':
        print("\nYou selected Mango flavor.")
        f = 'MANGO       '
    else:
        print('Please enter valid key.')
        sflavor()


def price():
    global p
    print("\n\tPRICE LIST\n")
    print('1. RS.10 - 15 (Small)\n2. RS.15 - 30 (Medium)\n3. RS.25 - 60 (Large)\n')
    rang = int(input("\nPlease select your range : "))
    if rang == 1:
        print("\nPrice : 15")
        p = 15
    elif rang == 2:
        print("\nPrice : 25")
        p = 25
    elif rang == 3:
        print("\nPrice : 50")
        p = 50
    else:
        print('\nPlease enter valid number.')
        price()
    return p


def confirm():
    print('\nTo confirm your order please enter \nY - YES\nN - NO')
    i = input('\nEnter your option : ')
    if i == 'Y' or i == 'y':
        print('\nOrder Received.')
    elif i == 'n' or i == 'N':
        print('\nOrder Canceled.')
    else:
        print('\nEnter valid number.')
        confirm()


itype = []
fl = []
pz = []
qu = []
print('\nICE CREAM SHOP')
print('\nICE CREAM MENU\n* Cone Ice\n* Cup Ice\n* stick Ice')
order = int(input("\nHow many order would you like to make? "))
for x in range(1, order+1):
    def main():
        global ice_type
        print('\nICE CREAM MENU\n1. Cone Ice\n2. Cup Ice\n3. Stick Ice')
        ice = int(input("\nEnter your option: "))
        if ice == 1:
            cone()
            ice_type = 'CONE ICE '
        elif ice == 2:
            cup()
            ice_type = 'CUP ICE  '
        elif ice == 3:
            stick()
            ice_type = 'STICK ICE'
        else:
            print("Invalid Number...")
            main()
    main()
    quantity = int(input('\nPlease enter a quantity: '))
    print('\nOrder No:', x)
    print('TYPE\t:', ice_type)
    print('FLAVOR\t:', f)
    print('PRICE\t:', p, '(', quantity, ')\n')
    a = quantity * p
    total = total + a
    itype.append(ice_type)
    pz.append(p)
    fl.append(f)
    qu.append(quantity)

print('\t\t\t          YOUR ORDER\n')
print(' _________________________________________________')
print('| TYPE       \t| FLAVOR        | PRICE (QUANTITY)|')
print('|_________________________________________________|')

for b in range(0, order):
    print("|", itype[b], "\t|", fl[b], "\t|", pz[b], "(", qu[b], ")", "       |")

print('|_________________________________________________|')
print('|\t\tTotal Bill Amount:', total, "                   |")
print('|_________________________________________________|')
confirm()
