import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7,
         8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

table = []
player = []


def draw():
    choice = random.choice(cards)
    return choice


def start(table, player):
    table = []
    player = []
    table.append(draw())
    table.append(draw())
    player.append(draw())
    player.append(draw())
    return table, player


def total(card):
    suma = sum(card)
    while 11 in card and suma > 21:
        card.remove(11)
        card.append(1)
        suma = sum(card)
    return suma


def nice_print(name, card, hide=False):
    if hide:
        temp = card.copy()
        temp[0] = "X"
        print(f"Cards of {name}: {temp}")
    else:
        print(f"Cards of {name}: {card}, total: {total(card)}")


def black_jack(table, player):
    if total(player) == 21 and total(table) != 21:
        print("You win BLACKJACK!")
    elif total(player) != 21 and total(table) == 21:
        print("Table wins BLACKJACK!")
    elif total(player) > 21 and total(table) <= 21:
        print("Table wins!")
    elif total(table) > 21 and total(player) <= 21:
        print("You win!")
    elif total(table) > total(player) and total(table) < 21 and total(player) < 21:
        print("Table wins!")
    elif total(table) < total(player) and total(table) < 21 and total(player) < 21:
        print("You win!")
    elif total(table) == total(player):
        print("Draw!")
    else:
        print("You lose both!")


while True:
    print(logo)
    table, player = start(table, player)
    nice_print("table", table, True)
    nice_print("player", player)
    end = False
    while not end:
        if total(player) >= 21:
            break
        next_card = input("Do you need next card: Y/N? ")
        if next_card == "Y":
            player.append(draw())
            nice_print("player", player)
        elif next_card == "N":
            end = True
        else:
            print("You chose anapopriate option!")

    end = False
    while not end:
        next_card = total(table) <= 17
        if next_card == True:
            table.append(draw())
            nice_print("table", table)
        else:
            end = True
    print("Final results:")
    nice_print("table", table)
    nice_print("player", player)
    black_jack(table, player)
    game = input("Press Y to play again or press any other buttom to exit")
    if game != "Y":
        print("The end")
        break
