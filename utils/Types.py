from discord import Intents
from discord.ext import commands

class Inventory():
    def __init__(self):
        self.head = "Bronze"
        self.armor = "Bronze"
        self.legs = "Bronze"

class Enemy():
    def __init__(self):
        self.type = 1
        self.hp = 100
        self.attack = 7
        self.xp = 167

class User():
    def __init__(self, name, gender, id, owner):
        self.name = name
        self.gender = gender
        self.level = 1
        self.id = id
        self.owner = owner
        self.hp = 100
        self.money = 100
        self.attack = 10
        self.inv = Inventory()
        self.enemy = Enemy()