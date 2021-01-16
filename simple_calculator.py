from math import sqrt


def calculator(*args):
    """Bardzo prosty kalkulator, który przyjmuje dowolną ilośc argumentów.
       Użytkownik każdorazowo ma możliwość wybrania wykonywanego działania."""
    for el in args:
        if type(el) not in [int, float]:
            raise ValueError
    print('Jakie chcesz wykonać działanie?')
    print("""
Wpisz 1 dla dodawania, 2 dla odejmowania, 3 dla mnożenia,
4 dla dzielenia, 5 dla potęgowania, 6 dla pierwiastka kwadratowego
    """)
    x=input('Wpisz jaki jest Twój wybór?')

    if x=='1' or x=='+':
        print('Dodawanie liczb')
        wynik = 0
        print(sum(args))
    elif x=='2' or x=='-':
        print(f'Odejmowanie liczb od {args[0]}.')
        wynik = args[0]
        for elem in args[1:]:
            wynik -= elem
        print(wynik)
    elif x=='3' or x=='*':
        print('Mnożenie liczb')
        wynik = args[0]
        for elem in args[1:]:
            wynik *= elem
        print(wynik)
    elif x=='4' or x=='/':
        print(f'Dzielenie - {args[0]} przez {args[1:]}.')
        wynik = args[0]
        for elem in args[1:]:
            wynik /= elem
        print(wynik)
    elif x=='5' or x=='**':
        print(f'Potęgowanie - {args[0]} do potęgi {args[1:]}.')
        wynik = args[0]
        for elem in args[1:]:
            wynik **= elem
        print(wynik)
    elif x=='6':
        print('Pierwiastek kwadratowy')
        for el in args:
            wynik = sqrt(el)
            print(wynik)
    else:
        print('Wybór spoza listy możliwości...')




if __name__ == '__main__':
    calculator(1,2,3,4)
    calculator(10.5,2,3)
    calculator(64, 9)


