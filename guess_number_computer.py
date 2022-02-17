def guess_2():
    """Gra w zgadywanie. Komputer odgaduje liczbę użytkownika w 10 próbach."""
    game_min = 0
    game_max = 1001
    print('Pomyśl liczbę od 0 do 1000, a komputer spróbuje ją zgadnąć w maksymalnie 10 próbach!')
    i=0
    cheat_detector=[]
    while i != 10:
        guess=int((game_max-game_min)/2+game_min)
        print(f'Zgaduję: {guess}')
        if guess not in cheat_detector:
            cheat_detector.append(guess)
        else:
            return "Nie oszukuj mnie! To powinna być uczciwa gra!"

        try:
            chosen_option = int(input(
                                        """
                                        wybierz jedną z opcji:
                                        'za mała liczba' - 1
                                        'za duża liczba' - 2
                                        'odgadnięta liczba' - 3
                                        """))
        except ValueError:
            print('Nie mogę tego przekształcić w liczbę całkowitą. Zacznij od nowa.')
            break
        if chosen_option == 1:
            game_min = guess
        elif chosen_option == 2:
            game_max = guess
        elif chosen_option == 3:
            return 'Wygrałem! Udało się odgadnąć!'
        else:
            print('Trzeba wpisać "1"(za mało), "2"(za dużo) lub "3" (oznaczające odgadnięcie liczby)')
            continue
        i += 1

    else:
        print(f'Próby zgadywania: {cheat_detector}')
        return 'Przegrana. Gramy jeszcze raz?'





if __name__ == '__main__':
    print(guess_2())