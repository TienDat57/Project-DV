from screens.dataCollection import Collection_Screen
from screens.dataExploration import Exploration_Screen
from screens.dataAnalysis import Analysis_Screen
# from screens.reflection import Reflection_Screen
from utils.index import get_hash

def get_routes():
    screens = [  
        {
            "component": Collection_Screen,
            "name": "Collection",
            "icon": "cloud-download"
        },
        {
            "component": Exploration_Screen,
            "name": "Exploration",
            "icon": "folder2"
        },
        {
            "component": Analysis_Screen,
            "name": "Analysis",
            "icon": "bar-chart-line"
        },
        # {
        #     "component": Reflection_Screen,
        #     "name": "Reflection",
        #     "icon": "award"
        # }
    ]
    
    return get_hash(screens)