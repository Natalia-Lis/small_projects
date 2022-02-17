class HumanBlood:
    """ getter & setter - enables setting only specific blood types. """

    def __init__(self, blood_type='Not specified'):
        self.__blood_type = blood_type

    def __str__(self):
        return f'Obiekt {self.__class__.__name__} o grupie krwi "{self.__blood_type}".'

    @property
    def blood(self):
        return self.__blood_type

    @blood.setter
    def blood(self, blood_type):
        if blood_type in ['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-']:
            self.__blood_type = blood_type
        else:
            raise ValueError('It doesn\'t add up. There is no such blood type.')



if __name__ == '__main__':
    human1 = HumanBlood()
    human2 = HumanBlood()
    print(human1)
    human1.blood='B-'
    print(human1)
    print(human1.blood)
    print(human1._HumanBlood__blood_type) # name mangling
    human2.blood='A+'
    print(human2)


    # PROGRAM NIE POZWOLI NA ZAPIS BŁĘDNEJ GRUPY KRWI
    # human3 = HumanBlood()
    # human3.blood='X-'
    # print(human3)





