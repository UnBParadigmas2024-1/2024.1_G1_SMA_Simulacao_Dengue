import mesa
from model.dengue_model import DengueContaminationModel
from visualization.portrayal import *

server = mesa.visualization.ModularServer(DengueContaminationModel,
                       [legend_element, canvas_element, situation_chart],
                       "Dengue Propagation Model",
                       model_kwargs)

server.port = 8521
server.launch()
