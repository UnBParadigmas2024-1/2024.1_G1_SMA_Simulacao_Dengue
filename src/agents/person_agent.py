from mesa import Agent

from agents.water_object import WaterObject

HEALTHY = "Saudável"
DENGUE = "Dengue"
SEVERE_DENGUE = "Dengue Hemorrágica"
DEAD = "Morto"

class PersonAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = HEALTHY
        self.infections = 0

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False  # Considera todas as 8 direções
        )

        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()
        self.interact_with_water()
    
    def interact_with_water(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        water_objects = [agent for agent in neighbors if isinstance(agent, WaterObject)]
        for water in water_objects:
            water.remove_standing_water()
            break
    
    def step(self):
        if self.state != DEAD:
            self.move()
            self.interact_with_water()
    
    def infect(self):
        if self.state == "Saudável":
            self.state = "Dengue"
            self.infections += 1
        elif self.state == "Dengue":
            self.state = "Dengue Hemorrágica"
        elif self.state == "Dengue Hemorrágica":
            self.state = "Morto"