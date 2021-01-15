from random import randint


def lotto():
    """Symulator LOTTO (zasady dużego lotka)"""
    chosen_numbers = []
    winning_numbers = []
    for element in range(6):
        try:
            num = int(input('Wprowadź POJEDYNCZO sześć liczb całkowitych z zakresu od 1 do 49: '))
            if 1 <= num <= 49:
                chosen_numbers.append(num)
            else:
                print('Nie wprowadzono liczby z zakresu 1-49, zatem nie może wziąć udziału w losowaniu')
        except ValueError:
            return 'Nie tak! Podaj LICZBĘ z zakresu 1-49. Lepiej zacznij od nowa...'

    chosen_numbers_set = set(chosen_numbers)
    if len(chosen_numbers_set) < len(chosen_numbers):
        print('Wpisując powtarzające się liczby zmniejsza się szansę na wygraną...')
    chosen_numbers.sort()
    print(f'Oto wybrane przez Ciebie liczby: {chosen_numbers}')
    while len(winning_numbers) != 6:
        lotto_number = randint(1, 49)
        if lotto_number not in winning_numbers:
            winning_numbers.append(lotto_number)
    winning_numbers.sort()
    print(f'A wyniki losowania w dniu dzisiejszym to... {winning_numbers}')
    print()
    print('*** Sprawdzanie wybranych liczb względem liczb wygrywających... ***')
    guessed_numbers = chosen_numbers_set.intersection(set(winning_numbers))
    if len(guessed_numbers) > 0:
        print(f'Wylosowano {len(guessed_numbers)} z twoich liczb, a konkretnie: {guessed_numbers}')

    if chosen_numbers == winning_numbers:
        return 'PEŁNA WYGRANA! - 6 liczb, które wybrano zgadza się z liczbami wygrywającymi!'
    elif len(guessed_numbers) == 5:
        return 'Brawo! Udało Ci się wybrać 5 wygrywających liczby'
    elif len(guessed_numbers) == 4:
        return 'Brawo! Udało Ci się wybrać 4 wygrywające liczby'
    elif len(guessed_numbers) == 3:
        return 'Brawo! Udało Ci się wybrać 3 wygrywające liczby'
    else:
        return """
Niestety! Przegrana! Wygrywają tylko trafienia trzech, czterech, pięciu i sześciu liczb. 
Spróbuj zagrać jeszcze raz...
               """




if __name__ == '__main__':
    print(lotto())