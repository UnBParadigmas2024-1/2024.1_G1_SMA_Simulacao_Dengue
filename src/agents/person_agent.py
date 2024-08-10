from mesa import Agent

# Definindo os estados de saúde
HEALTHY = "Saudável"
DENGUE = "Dengue"
SEVERE_DENGUE = "Dengue Hemorrágica"
DEAD = "Morto"

class PersonAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = "Saudável"
        self.infections = 0


    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def interact_with_water(self):
        cell_contents = self.model.grid.get_cell_list_contents([self.pos])
        for content in cellmates:
            if isinstance(content,  self.model.AguaParadaAgent):
                self.model.grid.remove_agent(content)
                print(f"Água parada eliminada por agente {self.unique_id}")

    def step(self):
        if self.state != DEAD:
            self.move()
            self.interact_with_water()
        cell_contents = self.model.grid.get_cell_list_contents([self.pos])
        # water = [obj for obj in cell_contents if isinstance(obj, WaterObject)]
        # if water:
        #     self.model.grid.remove_agent(water[0])
        
        # mosquitoes = [obj for obj in cell_contents if isinstance(obj, MosquitoAgent)]
        # for mosquito in mosquitoes:
        #     if mosquito.state == "Infectado":
        #         self.infect()
    

