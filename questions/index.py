from questions.House_Type import House_Type_Question
from questions.Price_Correlation import Price_Correlation_Question
from questions.House_Price_Fluctuation import Price_Fluctuation_Question
from questions.District_Information import District_Information_Question
from questions.house_rooms_correlation import houseRoomsCorrelation
from questions.More_House_Less_Price import More_House_Less_Price_Question
from questions.Regression import Regression_Question
from questions.Price_followed_by_District import Price_followed_by_district_Question
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
        },
        {
            "component": More_House_Less_Price_Question,
            "name": "🏚 Q6 More House Less Price",
            "icon": "front"
        },
        {    
            "component": Regression_Question,
            "name": "📈 Q7 Regression",
            "icon": "line-chart"
        },
        {
            "component": Price_followed_by_district_Question,
            "name": "📈 Q8 Price followed by district",
            "icon": "line-chart"
        }]

    return get_hash(questions)