import random
from mesa import Agent

import uuid
from agents.water_object import WaterObject
from agents.person_agent import PersonAgent

INFECTED = "Infectado"
NOT_INFECTED = "Não infectado"
DEAD = "Morto"

class MosquitoAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        states = [INFECTED, NOT_INFECTED]
        random_state = self.random.randint(0, 1)

        self.state = states[random_state]
        self.life_time = 10

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
    
    def check_life_time(self):
        self.life_time -= 1

        if self.life_time <= 0:
            self.state = DEAD
            self.model.grid.remove_agent(self)
            
    
    def sting_person(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        persons = [agent for agent in neighbors if isinstance(agent, PersonAgent)]

        if len(persons) > 0:
            person = random.choice(persons)
            if self.state == "Infectado":
                person.infect()
    
    def create_mosquitos(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        water_objects = [agent for agent in neighbors if isinstance(agent, WaterObject)]

        for water in water_objects:
            water.state = "Contaminada"
            print("Água contaminada.")

    def step(self):
        if self.state != DEAD:
            self.move()
            self.sting_person()
            self.create_mosquitos()
            self.check_life_time()