from agents.person_agent import PersonAgent
from agents.mosquito_agent import MosquitoAgent
from agents.water_object import WaterObject

def agent_portrayal(agent):
    if isinstance(agent, PersonAgent):
        portrayal = {
            "Shape": "circle",
            "Filled": "true",
            "r": 0.8,
            "Layer": 1  
        }
        if agent.state == "Saudável":
            portrayal["Color"] = "green"
        elif agent.state == "Dengue":
            portrayal["Color"] = "yellow"
        elif agent.state == "Dengue Hemorrágica":
            portrayal["Color"] = "red"
        else:
            portrayal["Color"] = "black"
            portrayal["r"] = 0.5
    
    elif isinstance(agent, MosquitoAgent):
        portrayal = {
            "Shape": "rect",
            "Filled": "true",
            "w": 0.5, "h": 0.5,
            "Color": "gray" if agent.state == "Não infectado" else "orange",
            "Layer": 2  
        }
    
    elif isinstance(agent, WaterObject):
        portrayal = {
            "Shape": "circle",
            "Filled": "true",
            "Color": "blue" if agent.state == "Contaminada" else "cyan",
            "r": 0.3,
            "Layer": 0
        }

    return portrayal
