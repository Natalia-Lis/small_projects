from random import choice


def rock_scissors_paper():
    """Standardowa gra w kamień, papier, nożyce. Komputer gra przeciwko użytkownikowi."""
    POSSIBLE_CHOICES = ('N', 'P', 'K')
    print('* * * Gra w kamień, papier, nożyce * * *')
    user_choice = input('Wpisz "K" jeśli wybierasz kamień, "P" jeśli papier albo "N" jeśli chcesz wybrać nożyce. ').upper()
    if user_choice not in ('N','P','K'):
        return 'Wprowadzono wartość spoza zakresu. Jeśli chcesz grać wybierz \'N\', \'K\' lub \'P\'!'
    computer_choice = choice(POSSIBLE_CHOICES)
    print(f'Twój wybór: {user_choice}, a wybór komputera: {computer_choice}.')
    if computer_choice == user_choice:
        return f'REMIS! Komputer też wybrał "{user_choice}".'
    elif user_choice == 'P':
        if computer_choice == 'K':
            return 'Brawo! Wygrana!'
        elif computer_choice == 'N':
            return 'Niestety przegrałeś.'
    elif user_choice == 'N':
        if computer_choice == 'P':
            return 'Brawo! Wygrana!'
        elif computer_choice == 'K':
            return 'Niestety przegrałeś.'
    elif user_choice == 'K':
        if computer_choice == 'N':
            return 'Brawo! Wygrana!'
        elif computer_choice == 'P':
            return 'Niestety przegrałeś.'




if __name__ == '__main__':
    print(rock_scissors_paper())