from random import randint


def throw_the_dice(quantity=1, dice_type=6, result_modification=0):
    """Symulator rzutu kostką.
       Można wybrać ilość rzutów, typ kostki, dodać modyfikację wyniku.
       Bez argumentów funkcja symuluje normalny rzut sześciościenną kostką"""
    if type(quantity) != int or type(dice_type) != int or type(result_modification) != int:
        raise ValueError("Podane wartości muszą być całkowitą liczbą naturalną.")
    dice_throwings = 0
    list_of_throwings = []
    for el in range(quantity):
        throw = randint(1, dice_type)
        list_of_throwings.append(throw)
        dice_throwings += throw
    print('Twoje rzuty: {}'.format(list_of_throwings))
    if result_modification != 0:
        dice_throwings += result_modification
        print('Zmodyfikowano wylosowany wynik o {}'.format(result_modification))
    return dice_throwings





if __name__ == '__main__':
    print(throw_the_dice())
    print()
    print(throw_the_dice(2,8,-100))
    print()
    print(throw_the_dice(4,20,0))
