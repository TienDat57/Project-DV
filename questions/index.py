from questions.House_Type import House_Type_Question
from questions.Price_Correlation import Price_Correlation_Question
from questions.More_Houses_Higher_Price import More_Houses_Higher_Price_Question
from questions.Regression import Regression
from utils.index import get_hash

def get_questions():
    questions = [
                {
            "component": House_Type_Question,
            "name": "🏚 House Type",
            "icon": "front"
        },
        {
            "component": Price_Correlation_Question,
            "name": "💰 Price correlation",
            "icon": "cash-coin"
        },
        {
            "component": More_Houses_Higher_Price_Question,
            "name": "🏚 More Houses Higher Price Question",
            "icon": "front"
        },
        {    
            "component": Regression,
            "name": "📈 Regression",
            "icon": "line-chart"
        },
    ]

    return get_hash(questions)