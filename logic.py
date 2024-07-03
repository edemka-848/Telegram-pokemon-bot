from random import randint
import requests

class Pokemon:
    pokemons = {}
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        Pokemon.pokemons[pokemon_trainer] = self
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "Pikachu"
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    def info(self):
        return f"{self.pokemon_trainer} {self.pokemon_number} {self.img} {self.name}"  
    

class Wizard(Pokemon): 
    def attack(self, enemy):
        self.hp  = randint(1,1000)
        self.power = randint(1,1000)
        if isinstance(enemy, Wizard): 
            chance = randint(1,5)
        if chance == 1:
            return "Покемон-волшебник применил щит в сражении"
        
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    def attack(self, enemy):
        return super().attack(enemy)


class Fighter(Pokemon): 
    def attack(self, enemy):
        return super().attack(enemy)
    def attack(self, enemy,):
        self.power = randint(1,1000)
        super_power = randint(5,15)
        self.power += super_power
        resultat = super().attack(enemy)
        self.power -= super_power
        return resultat + f"\
        Боец применил супер-атаку силой:{super_power} "
        
    
    

def show_img(self):
    return self.img