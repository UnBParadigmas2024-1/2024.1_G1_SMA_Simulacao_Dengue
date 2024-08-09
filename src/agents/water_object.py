from mesa import Agent

class WaterObject(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = "Contaminada"
    
    def step(self):
        pass
