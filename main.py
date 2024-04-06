import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Du hast überkauft. Du verlierst 😤"
    if user_score == computer_score:
        return "Unentschieden 🙃"
    elif computer_score == 0:
        return "Verloren, Gegner hat Blackjack 😱"
    elif user_score == 0:
        return "Gewonnen mit einem Blackjack 😎"
    elif user_score > 21:
        return "Du bist über 21. Du verlierst 😭"
    elif computer_score > 21:
        return "Gegner ist über 21. Du gewinnst 😁"
    elif user_score > computer_score:
        return "Du gewinnst 😃"
    else:
        return "Du verlierst 😤"

def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Deine Karten: {user_cards}, aktuelle Punktzahl: {user_score}")
        print(f"   Erste Karte des Computers: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Tippe 'y' für eine weitere Karte, tippe 'n' zum Passen: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Deine finale Hand: {user_cards}, finale Punktzahl: {user_score}")
    print(f"   Computers finale Hand: {computer_cards}, finale Punktzahl: {computer_score}")
    print(compare(user_score, computer_score))

while input("Möchtest du eine Runde Blackjack spielen? Tippe 'y' für Ja oder 'n' für Nein: ") == "y":
    play_game()
