from mosquito_agent import MosquitoAgent
from mesa import Agent

from agents.water_object import WaterObject
from agents.mosquito_agent import MosquitoAgent

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
        

        # water = [obj for obj in cell_contents if isinstance(obj, WaterObject)]
        # if water:
        #     self.model.grid.remove_agent(water[0])
    
    def interact_with_water(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        water_objects = [agent for agent in neighbors if isinstance(agent, WaterObject)]
        for water in water_objects:
            water.remove_standing_water()
            break
    
    def interact_with_mosquitoes(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        mosquitoes_objects = [agent for agent in neighbors if isinstance(agent, MosquitoAgent)]
        for mosquitoes in mosquitoes_objects:
            if mosquitoes.state == "Infectado":
                self.infect()
    

    def step(self):
        if self.state != DEAD:
            self.move()
            self.interact_with_water()
            self.interact_with_mosquitoes()
            cell_contents = self.model.grid.get_cell_list_contents([self.pos])

        mosquitoes = [obj for obj in cell_contents if isinstance(obj, MosquitoAgent)]
        for mosquito in mosquitoes:
            if (
                self.state in ["Dengue", "Dengue Hemorrágica"]
                and mosquito.state == "Não infectado"
            ):
                mosquito.state = "Infectado"

    def infect(self):
        if self.state == HEALTHY:
            self.state = DENGUE
            self.infections += 1
        elif self.state == DENGUE:
            self.state = SEVERE_DENGUE
        elif self.state == SEVERE_DENGUE:
            self.state = DEAD