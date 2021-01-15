from random import randint


def guessing_number():
    """Zgadywanie liczb. Zgaduje użytkownik, a komputer losuje liczbę."""
    must_guess = randint(1,100)
    guess = 0
    while guess != must_guess:
        try:
            guess = int(input('Spróbuj zgadnąć liczbę! Podaj liczbę z zakresu 1-100: '))
            if 1 <= guess <= 100:
                if guess < must_guess:
                    print('Za mało!')
                elif guess > must_guess:
                    print('Za dużo!')
                else:
                    return 'Brawo! Wygrana!'
            else:
                print('Trzeba zgadnąć liczbę całkowitą w zakresie 1-100!')
        except Exception as error:
            print(f'To nie jest liczba całkowita z zakresu 1-100! Zacznijmy od nowa. Błąd: {error}')
            return guessing_number()




if __name__ == '__main__':
    print(guessing_number())