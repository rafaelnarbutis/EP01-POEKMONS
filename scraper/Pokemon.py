import json


class Pokemon:

    def __init__(self):
        self.damage_taken = None
        self.evolution = None
        self.types = None
        self.height = None
        self.weight = None
        self.name = None
        self.number = None

    def setName(self, name):
        self.name = name

    def setNumber(self, number):
        self.number = number

    def setTypes(self, types):
        self.types = types

    def setHeight(self, height):
        self.height = height

    def setWeight(self, weight):
        self.weight = weight

    def setEvolution(self, evolution):
        self.evolution = evolution

    def setDamageTaken(self, damageTaken):
        self.damage_taken = damageTaken

    def toJson(self): return json.dumps(self, default = lambda o: o.__dict__, indent = 4)
