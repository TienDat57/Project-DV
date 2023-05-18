from questions.Price_Correlation import Price_Correlation_Question
from questions.House_Price_Fluctuation import Price_Fluctuation_Question
from questions.District_Information import District_Information_Question
from questions.Regression import Regression
from utils.index import get_hash

def get_questions():
    questions = [
        {
            "component": Price_Correlation_Question,
            "name": "💰 Q1 Price correlation",
            "icon": "cash-coin"
        },
        {
            "component": Price_Fluctuation_Question,
            "name": "📉 Q2 Price Fluctuation",
            "icon": "line-chart"
        },
        {
            "component": District_Information_Question,
            "name": "🌆 Q3 District Information",
            "icon": "home-night"
        },
        {    
            "component": Regression,
            "name": "📈 Q4 Regression",
            "icon": "line-chart"
        },
    ]

    return get_hash(questions)