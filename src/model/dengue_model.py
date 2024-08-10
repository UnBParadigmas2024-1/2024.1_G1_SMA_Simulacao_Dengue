from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from agents.person_agent import PersonAgent
from agents.mosquito_agent import MosquitoAgent
from agents.water_object import WaterObject

class DengueContaminationModel(Model):
    def __init__(self, width, height, initial_people, initial_mosquitoes, initial_water):
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
            agent_reporters={"State": lambda a: a.state, "Infections": lambda a: getattr(a, "infections", 0)}
        )
        
        for i in range(initial_people):
            person = PersonAgent(i, self)
            self.grid.place_agent(person, (self.random.randrange(self.grid.width), self.random.randrange(self.grid.height)))
            self.schedule.add(person)
        
        for i in range(initial_mosquitoes):
            mosquito = MosquitoAgent(i + initial_people, self)
            self.grid.place_agent(mosquito, (self.random.randrange(self.grid.width), self.random.randrange(self.grid.height)))
            self.schedule.add(mosquito)
        
        for i in range(initial_water):
            pos = (self.random.randrange(self.grid.width), self.random.randrange(self.grid.height))
            water = WaterObject(i + initial_people + initial_mosquitoes, self, pos)
            self.grid.place_agent(water, pos)
        
        self.running = True

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
