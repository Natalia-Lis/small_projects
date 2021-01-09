class HumanBlood:
    """ getter & setter - enable setting only specific blood types. """

    def __init__(self, blood_type='Not specified'):
        self.blood_type = blood_type

    def __str__(self):
        return f'obiekt {self.__class__.__name__}'

    @property
    def show_blood_type(self):
        return self.__blood_type

    @show_blood_type.setter
    def show_blood_type(self, blood_type):
        if blood_type in ['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-']:
            self.__blood_type = blood_type
        else:
            raise ValueError('It doesn\'t add up. There is no such blood type.')




if __name__ == '__main__':

    human1 = HumanBlood()
    print(human1)
    print(human1.blood_type)
    human1.show_blood_type = 'B-'
    print(human1.show_blood_type)
    print(human1._HumanBlood__blood_type) # name mangling

    # human2 = HumanBlood()
    # print(human2)
    # print(human2.blood_type)
    # human2.show_blood_type = 'X'
    # print(human2.show_blood_type)




