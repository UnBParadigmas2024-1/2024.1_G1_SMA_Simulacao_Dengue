from mesa import Agent
import random
import uuid


from agents.water_object import WaterObject

HEALTHY = "Saudável"
DENGUE = "Dengue"
SEVERE_DENGUE = "Dengue Hemorrágica"
DEAD = "Morto"
RECOVERED = "Curado"

class PersonAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = HEALTHY
        self.infections = 0
        self.infectedDays = 0

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False  
        )

        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()
        self.interact_with_water()
    
    def interact_with_water(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        water_objects = [agent for agent in neighbors if isinstance(agent, WaterObject)]
        if water_objects:
            for water in water_objects:
                if random.random() < 0.6:
                    water.remove_standing_water()
                    print("Agua parada removida.")
                    break
        else:
            if random.random() < 0.1:
                new_water = WaterObject(uuid.uuid1(), self.model)
                self.model.grid.place_agent(new_water, self.pos)
                print("Agua parada adicionada.")

    def statusUpdate(self):
        if self.state== DENGUE:
            self.infectedDays += 1
            if random.random()<0.2:
                self.state=SEVERE_DENGUE
            elif random.random()<0.01:
                self.state=DEAD
            elif self.infectedDays>7 and random.random()<0.5:
                self.state=RECOVERED
        elif self.state== SEVERE_DENGUE:
            if random.random()<0.2:
                self.state=DEAD
            elif self.infectedDays>14 and random.random()<0.4:
                self.state=RECOVERED



    def step(self):
        if self.state != DEAD:
            self.move()
            self.statusUpdate()
            self.interact_with_water()

    
    def infect(self):
        if self.state == HEALTHY and random.random()<0.5:
            self.state = DENGUE
            self.infections += 1
            self.infectedDays += 1