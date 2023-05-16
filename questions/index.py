from questions.House_Type import House_Type_Question
from questions.Price_Correlation import Price_Correlation_Question
from questions.House_Price_Fluctuation import Price_Fluctuation_Question
from questions.District_Information import District_Information_Question
from questions.house_rooms_correlation import houseRoomsCorrelation
from utils.index import get_hash

def get_questions():
    questions = [
        {
            "component": House_Type_Question,
            "name": "🏚 Q1 House Type",
            "icon": "front"
        },
        {
            "component": Price_Correlation_Question,
            "name": "💰 Q2 Price correlation",
            "icon": "cash-coin"
        },
        {
            "component": Price_Fluctuation_Question,
            "name": "📉 Q3 Price Fluctuation",
            "icon": "line-chart"
        },
        {
            "component": District_Information_Question,
            "name": "🌆 Q4 District Information",
            "icon": "home-night"
        },
        {
            "component": houseRoomsCorrelation,
            "name": "🤖 Q5 House Rooms Correlation",
            "icon": "cash-coin"
        }
    ]

    return get_hash(questions)