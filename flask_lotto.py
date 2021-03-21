from random import randint

from flask import Flask, request, render_template


app = Flask(__name__, template_folder='.')


@app.route('/', methods=['GET', 'POST'])
def index():
    """ Lotto Simulator - user choose 6 numbers and gets answer whether his numbers match winning numbers """
    if request.method == 'POST':
        n1 = int(request.form['num1'])
        n2 = int(request.form['num2'])
        n3 = int(request.form['num3'])
        n4 = int(request.form['num4'])
        n5 = int(request.form['num5'])
        n6 = int(request.form['num6'])
        chosen_numbers = [n1,n2,n3,n4,n5,n6]
        chosen_numbers.sort()

        winning_numbers = []
        while len(winning_numbers) != 6:
            lotto_number = randint(1, 49)
            if lotto_number not in winning_numbers:
                winning_numbers.append(lotto_number)
        winning_numbers.sort()

        show_chosen = ', '.join(str(i) for i in chosen_numbers)
        show_winning = ', '.join(str(i) for i in winning_numbers)

        chosen_numbers_set = set(chosen_numbers)
        if len(chosen_numbers_set) < 6:
            return 'Wpisując powtarzające się liczby zmniejsza się szansę na wygraną... \
                    Powinieneś wpisać niepowtarzające się liczby. Gramy jeszcze raz?'
        if any(number > 49 for number in chosen_numbers) or any(number < 1 for number in chosen_numbers):
            return f'Twoje wybrane liczby to: {n1}, {n2}, {n3}, {n4}, {n5}, {n6}. Wybrałeś liczbę/y spoza zakresu'

        guessed_numbers = chosen_numbers_set.intersection(set(winning_numbers))
        if 3 > len(guessed_numbers) > 0:
            message = f'Wylosowano {len(guessed_numbers)} z twoich liczb, a konkretnie: {guessed_numbers}.'
            return render_template('flask_lotto.html', message=message,
                                   show_chosen=show_chosen, show_winning=show_winning)
        elif chosen_numbers == winning_numbers:
            message = 'PEŁNA WYGRANA! - 6 liczb, które wybrano zgadza się z liczbami wygrywającymi!'
            return render_template('flask_lotto.html', message=message,
                                   show_chosen=show_chosen, show_winning=show_winning)
        elif len(guessed_numbers) == 5:
            message = 'Brawo! Udało Ci się wybrać 5 wygrywających liczby.'
            return render_template('flask_lotto.html', message=message,
                                   show_chosen=show_chosen, show_winning=show_winning)
        elif len(guessed_numbers) == 4:
            message = 'Brawo! Udało Ci się wybrać 4 wygrywające liczby.'
            return render_template('flask_lotto.html', message=message,
                                   show_chosen=show_chosen, show_winning=show_winning)
        elif len(guessed_numbers) == 3:
            message = 'Brawo! Udało Ci się wybrać 3 wygrywające liczby.'
            return render_template('flask_lotto.html', message=message,
                                   show_chosen=show_chosen, show_winning=show_winning)
        else:
            message = 'Niestety! Przegrana! Wygrywają tylko trafienia trzech, czterech, \
                       pięciu i sześciu liczb. Spróbuj zagrać jeszcze raz... .'
            return render_template('flask_lotto.html', message=message,
                                   show_chosen=show_chosen, show_winning=show_winning)

    else:
        return """
        symulator dużego lotka<br>
        <form action='/' method=POST>
            <label>
                Wpisz liczbę 1-49: <input type='number' step="1" name='num1'><br>
                Wpisz liczbę 1-49: <input type='number' step="1" name='num2'><br>
                Wpisz liczbę 1-49: <input type='number' step="1" name='num3'><br>
                Wpisz liczbę 1-49: <input type='number' step="1" name='num4'><br>
                Wpisz liczbę 1-49: <input type='number' step="1" name='num5'><br>
                Wpisz liczbę 1-49: <input type='number' step="1" name='num6'><br>
            </label>
            <button type='submit'>
                Wyślij!
            </button>
        </form>
    """


if __name__ == '__main__':
    app.run(debug=True)