from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp  = randint(1,1000)
        self.power = randint(1,1000)
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "Pikachu"
        
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"
        return f"Здоровье твоего покеомона: {self.hp}"
        return f"Сила твоего покеомона: {self.power}"


def attack(self, enemy):
    if enemy.hp > self.power:
        enemy.hp -= self.power
        return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
    else:
        enemy.hp = 0
        return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    

def show_img(self):
    return self.img