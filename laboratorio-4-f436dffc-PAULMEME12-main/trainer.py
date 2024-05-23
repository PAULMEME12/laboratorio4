class Trainer:
    def __init__(self, id, first_name, last_name, age, level):
        self.__id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.level = level
        self.__pokedex = []

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if not isinstance(id, int):
            raise TypeError("El ID debe ser un entero.")
        self.__id = id

    def add_to_pokedex(self, pokemon):
        from pokemon import Pokemon
        if isinstance(pokemon, Pokemon):
            print(f"Se ha agregado a {pokemon} al pokedex de {self.first_name}")
            self.__pokedex.append(pokemon)
        else:
            raise TypeError("El objeto debe ser una instancia de la clase Pokemon")

    def get_pokedex(self):
        return self.__pokedex
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    