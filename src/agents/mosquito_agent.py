from person_agent import PersonAgent
from mesa import Agent


class MosquitoAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = "Não infectado"
        self.life_time = 3

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def sting_person(self, person: PersonAgent):
        if self.state == "Infectado":
            person.infect()

    def step(self):
        self.move()
        # self.life_time -= 1
        # if self.life_time <= 0:
        #     self.model.grid.remove_agent(self)
        #     return

        cell_contents = self.model.grid.get_cell_list_contents([self.pos])
        # water = [obj for obj in cell_contents if isinstance(obj, WaterObject)]
        # if water:
        #     for _ in range(self.random.randint(1, 3)):
        #         new_mosquito = MosquitoAgent(self.model.next_id(), self.model)
        #         self.model.grid.place_agent(new_mosquito, self.pos)
        #         self.model.schedule.add(new_mosquito)

        # people = [obj for obj in cell_contents if isinstance(obj, PersonAgent)]
        # for person in people:
        #     if person.state != "Morto":
        #         if self.state == "Não infectado" and person.state in ["Dengue", "Dengue Hemorrágica"]:
        #             self.state = "Infectado"
