from mesa import Agent

class WaterObject(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = "Contaminada"
    
    def step(self):
        pass

    # Se a pessoa encontrar agua parada ele remove a agua
    def remove_standing_water(self):
        self.model.grid.remove_agent(self)
        print("Agua parada removida.")
