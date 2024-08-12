from mesa import Agent

class WaterObject(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = "Limpa"
    
    def step(self):
        pass

    def remove_standing_water(self):
        self.model.grid.remove_agent(self)
        
    def get_all_water_objects(self):
        water_objects = []
        for agent in self.schedule.agents:
            if isinstance(agent, WaterObject):
                water_objects.append(agent)
        return water_objects