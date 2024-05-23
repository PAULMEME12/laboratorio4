from pokemon import Pokemon
from trainer import Trainer

def classes_manual_tests():
    ### Creación de tus entrenadores
    ash = Trainer(id=1, first_name="Ash", last_name="Ketchum", age=10, level=5)
    misty = Trainer(id=2, first_name="Misty", last_name="", age=10, level=5)
    brock = Trainer(id=2, first_name="Brock", last_name="", age=10, level=5)

    

    ### Despliegue en pantalla de entrenadores
    print (ash)

    ### Creación de los pokemon con sus respectivos tipos
    charmander = Pokemon(id=1, name="Charmander", weight=6.0, height=0.4, trainer=ash)
    squirtle = Pokemon(id=3, name="Squirtle", weight=9.0, height=0.5, trainer=ash)
    pikachu = Pokemon(id=1, name="Pikachu", weight=6.0, height=0.4, trainer=ash) 

    
    ### Despliegue en pantalla de los Pokemones
    print (charmander )

    ### Despliegue del ataque de los pokemones

    print (charmander.attack() )
    print(isinstance(pikachu, Pokemon)) 
    
    ### Agrega pokemones al pokedex de 'ash'
    ash.add_to_pokedex(charmander)
    ash.add_to_pokedex(pikachu)
    ash.add_to_pokedex(squirtle)
    
    ### Imprime el pokedex de ash
    print("#######  Pokemons de Ash ##########")
    for pokemon in ash.get_pokedex():
        print(pokemon)

    
    
    
if __name__ == '__main__':
    classes_manual_tests()