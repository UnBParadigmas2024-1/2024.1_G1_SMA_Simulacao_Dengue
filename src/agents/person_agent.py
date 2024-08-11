from mosquito_agent import MosquitoAgent
from mesa import Agent


class PersonAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = "Saudável"
        self.infections = 0

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False  # Considera todas as 8 direções
        )

        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()
        cell_contents = self.model.grid.get_cell_list_contents([self.pos])

        mosquitoes = [obj for obj in cell_contents if isinstance(obj, MosquitoAgent)]
        for mosquito in mosquitoes:
            if (
                self.state in ["Dengue", "Dengue Hemorrágica"]
                and mosquito.state == "Não infectado"
            ):
                mosquito.state = "Infectado"

        # water = [obj for obj in cell_contents if isinstance(obj, WaterObject)]
        # if water:
        #     self.model.grid.remove_agent(water[0])

    def infect(self):
        if self.state == "Saudável":
            self.state = "Dengue"
            self.infections += 1
        elif self.state == "Dengue":
            self.state = "Dengue Hemorrágica"
        elif self.state == "Dengue Hemorrágica":
            self.state = "Morto"
