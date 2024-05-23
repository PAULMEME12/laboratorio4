from trainer import Trainer

class Pokemon:
    def __init__(self, id, name, weight, height, trainer):
        self.__id = id
        self.name = name
        self.weight = weight
        self.height = height
        if isinstance(trainer, Trainer):
            self.trainer = trainer
        else:
            raise ValueError("trainer debe ser una instancia de la clase Trainer")

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if not isinstance(id, int):
            raise TypeError("El ID debe ser un entero.")
        self.__id = id

    def __str__(self):
        return self.name

    def attack(self):
        return f"{self.name} está atacando!"
    

class ElectricPokemon(Pokemon):
    def __init__(self, id, name, weight, height, trainer):
        super().__init__(id, name, weight, height, trainer)
        self.type = "Electric"

    def attack(self):
        return f"{self.name} lanzó un ataque eléctrico!"

class WaterPokemon(Pokemon):
    def __init__(self, id, name, weight, height, trainer):
        super().__init__(id, name, weight, height, trainer)
        self.type = "Water"

    def attack(self):
        return f"{self.name} lanzó un ataque acuático!"

class FirePokemon(Pokemon):
    def __init__(self, id, name, weight, height, trainer):
        super().__init__(id, name, weight, height, trainer)
        self.type = "Fire"

    def attack(self):
        return f"{self.name} lanzó un ataque de fuego!"