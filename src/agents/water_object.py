from mesa import Agent

from agents.mosquito_agent import MosquitoAgent

class WaterObject(Agent):
    def __init__(self, unique_id, model, pos, infected=False):
        super().__init__(unique_id, model)
        self.pos = pos
        self.infected = infected
    
    def step(self):
        pass

    def interect_person(self, person):
        if person.state == "Saudável" and not self.contaminada:
            self.remove_standing_water()
    
    def interect_mosquito(self, mosquito):
        if self.infected:
            self.create_mosquitos()

    def remove_standing_water(self):
        self.model.grid.remove_agente(self)
        print("Agua parada removida.")

    def create_mosquitos(self):
        for _ in range(self.random.randint(1, 3)):
            new_mosquito = MosquitoAgent(self.model.next_id(), self.model)
            self.model.grid.place_agent(new_mosquito, self.pos)
            self.model.schedule.add(new_mosquito)
        print("Novos mosquitos criados.")