import mesa
from agents.mosquito_agent import MosquitoAgent
from agents.person_agent import PersonAgent
from agents.water_object import WaterObject

def getColorPerson(agent):
    if agent.state == "Saudável":
        return "green"
    elif agent.state == "Dengue":
        return "yellow"
    elif agent.state == "Dengue Hemorrágica":
        return "red"
    else:
        return "black"

def getPortrayalPerson(agent):
    return {
        "Shape": "circle",
        "Filled": "true",
        "Layer": 0,
        "Color": getColorPerson(agent),
        "r": 0.5,
        "id": f"Pessoa {agent.unique_id}"
    }

def circle_portrayal_example(agent):
    if agent is None:
        return

    if isinstance(agent, MosquitoAgent):
        portrayal = {
            "Shape": "circle",
            "Filled": "true",
            "Layer": 0,
            "Color": "#964b00",
            "r": 0.5,
            "id": f"Mosquito {agent.unique_id} {agent.state}"
        }
    elif isinstance(agent, WaterObject):
        portrayal = {
            "Shape": "circle",
            "Filled": "true",
            "Layer": 0,
            "Color": "#0ABCB0",
            "r": 0.5,
            "id": f"Agua parada {agent.unique_id}"
        }
    else:
        portrayal = getPortrayalPerson(agent)

    return portrayal

canvas_element = mesa.visualization.CanvasGrid(
    circle_portrayal_example, 10, 10, 700, 700
)

model_kwargs = {
    "initial_people": mesa.visualization.Slider(name="Quantidade de pessoas", min_value=0, max_value=20, step=1, value=10),
    "initial_mosquitoes": mesa.visualization.Slider(name="Quantidade de mosquitos", min_value=0, max_value=20, step=1, value=5),
    "initial_water": mesa.visualization.Slider(name="Quantidade de águas paradas", min_value=0, max_value=20, step=1, value=5),
    "width": 10,
    "height": 10
}

# Gráfico para a contagem de mosquitos
situation_chart = mesa.visualization.ChartModule(
    [{"Label": "Mosquito Count", "Color": "Green"}],
    data_collector_name="datacollector"
)

# situation_chart = mesa.visualization.ChartModule(
#    [{"Label": "Dengue", "Color": "Yellow"},
#     {"Label": "Dengue Hemorrágica", "Color": "Red"},
#     {"Label": "Morto", "Color": "Black"}],
#     data_collector_name="datacollector")