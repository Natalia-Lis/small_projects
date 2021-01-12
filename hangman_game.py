from random import choice
import hangman_pictures_necessary as hg


def podaj():
    print("""         * GRA WISIELEC *
Spróbuj zgadnąć krótkie losowe słowo!""")

    wybrane_slowo = choice(hg.pula_slow)
    wybrane_slowo_lower = wybrane_slowo.lower()
    wybrane_slowo_do_zmiany_na_litery = '' + wybrane_slowo_lower
    haslo = list(wybrane_slowo_lower)
    for i in range(len(wybrane_slowo)):
        haslo[i] = '_'
    liczba_prob = 0
    index = 0
    licznik = 0
    liczba_liter_w_slowie = len(wybrane_slowo)
    if liczba_liter_w_slowie <= 4:
        print(f'Wylosowane słowo ma: {liczba_liter_w_slowie} litery', '(', liczba_liter_w_slowie * ' * ', ')' )
    elif liczba_liter_w_slowie >= 5:
        print(f'Wylosowane słowo ma: {liczba_liter_w_slowie} liter', '(', liczba_liter_w_slowie * ' * ', ')' )
    while liczba_prob != 7:
        if wybrane_slowo_lower == '':
            print('Zwycięstwo!')
            break
        licznik += 1
        print(hg.hangman_pictures[index])
        input_uzytkownika = input(f'Podaj literę od A do Z (próba {licznik})')
        if len(input_uzytkownika) == 1:
            if input_uzytkownika.lower() in wybrane_slowo_lower:
                for i in range(len(wybrane_slowo)):
                    if wybrane_slowo_do_zmiany_na_litery[i] == input_uzytkownika:
                        haslo[i] = input_uzytkownika
                wybrane_slowo_lower = wybrane_slowo_lower.replace(input_uzytkownika, '')
            else:
                print('Próbuj dalej')
                liczba_prob += 1
                index += 1
        else:
            print('Powinieneś podać tylko jedną literę')
        print(' '.join(haslo))
    else:
        print(hg.hangman_picture_last)
        print('Nie zgadłaś/eś słowa w odpowiedniej liczbie prób. Spróbuj ponownie.')



if __name__ == '__main__':
    podaj()
