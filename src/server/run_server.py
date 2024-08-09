from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from model.dengue_model import DengueContaminationModel
from visualization.portrayal import agent_portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
chart = ChartModule([{"Label": "Dengue",
                      "Color": "Yellow"},
                     {"Label": "Dengue Hemorrágica",
                      "Color": "Red"},
                     {"Label": "Morto",
                      "Color": "Black"}],
                    data_collector_name='datacollector')

server = ModularServer(DengueContaminationModel,
                       [grid, chart],
                       "Dengue Propagation Model",
                       {"width": 10, "height": 10, "initial_people": 50, "initial_mosquitoes": 10, "initial_water": 5})

server.port = 8521
server.launch()
