class Band:


    list_of_bands = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.__class__.list_of_bands.append(self)


    def __str__(self):
        return f'{self.name} is a band'


    def __repr__(self):
        return f'{self.name} is a band'


    def add_to_list(self):
        print(self)
        return self.list_of_bands


class Musician():


    list_of_musicians = []


    def __init__(self, name, instrument):
        self.name = name 
        self.instrument = instrument 
        self.__class__.list_of_musicians.append(self)


    def get_instrument(self):
        return f'{self.instrument} they play'


    def play_solo(self):
        return f'{self.name} plays solo'


    def __str__(self):
        return f'{self.name} {self.instrument}'

    
    def __repr__(self):
        return f'{self.__class__.__name__} {self.name}'


class Guitarist(Musician):


    def __str__(self):
        return f'{self.name} {self.instrument}'

    
    def __repr__(self):
        return f'{self.__class__.__name__} {self.name}'
    # def __init__(self, name):
    #     super().__init__(name)
    #     self.instrument = 'Guitar' 


class Bassist(Musician):


    def __str__(self):
        return f'{self.name} {self.instrument}'

    
    def __repr__(self):
        return f'{self.__class__.__name__} {self.name}'


class Drummer(Musician):


    def __str__(self):
        return f'{self.name} {self.instrument}'

    
    def __repr__(self):
        return f'{self.__class__.__name__} {self.name}'


band1 = Band('Linkin Park', 'Chester')
print(band1)
# player1 = Musician('bob', 'drummer')
# print(player1) 
it = Guitarist('bob', 'guitar')
print(it)

