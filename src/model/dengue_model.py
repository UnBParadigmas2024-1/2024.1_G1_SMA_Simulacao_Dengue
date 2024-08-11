import random
import uuid
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from agents.person_agent import PersonAgent
from agents.mosquito_agent import MosquitoAgent
from agents.water_object import WaterObject

class DengueContaminationModel(Model):
    def __init__(self, width, height, initial_people, initial_mosquitoes, initial_water):
        self.initial_people = initial_people
        self.initial_mosquitoes = initial_mosquitoes
        self.initial_water = initial_water

        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        self.datacollector = DataCollector(
            agent_reporters={"State": lambda a: a.state, "Infections": lambda a: getattr(a, "infections", 0)},
            model_reporters={"Mosquito Count": self.get_mosquito_count}
        )

        # Create persons
        for _ in range(self.initial_people):
            pessoa = PersonAgent(uuid.uuid1(), self)
            self.place_agent_randomly(pessoa)

        # Create mosquito
        for _ in range(self.initial_mosquitoes):
            mosquito = MosquitoAgent(uuid.uuid1(), self)
            self.place_agent_randomly(mosquito)
        
        # Create agua
        for _ in range(self.initial_water):
            water = WaterObject(uuid.uuid1(), self)
            self.place_agent_randomly(water)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
    
    def place_agent_randomly(self, agent):
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        if self.grid.is_cell_empty((x, y)):
            self.grid.place_agent(agent, (x, y))
            self.schedule.add(agent)

    def get_mosquito_count(self):
        # Conta o número de mosquitos no modelo
        return len([a for a in self.schedule.agents if isinstance(a, MosquitoAgent)])
