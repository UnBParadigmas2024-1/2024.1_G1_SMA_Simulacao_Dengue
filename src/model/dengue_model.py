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

        self.num_people = initial_people
        self.num_mosquitoes = initial_mosquitoes

        self.datacollector = DataCollector(
            #agent_reporters={"State": lambda a: a.state, "Infections": lambda a: getattr(a, "infections", 0)}
            model_reporters={
                "Total People": lambda m: m.num_people,
                "Total Mosquitoes": lambda m: m.num_mosquitoes
            },
            agent_reporters={
                "State": lambda a: getattr(a, "state", None), 
                "Infections": lambda a: getattr(a, "infections", 0)
            }
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
            water = WaterObject(i + initial_people + initial_mosquitoes, self)
            self.grid.place_agent(water, (self.random.randrange(self.grid.width), self.random.randrange(self.grid.height)))
        
        self.running = True

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

        self.num_people = sum(1 for agent in self.schedule.agents if isinstance(agent, PersonAgent))
        self.num_mosquitoes = sum(1 for agent in self.schedule.agents if isinstance(agent, MosquitoAgent))
