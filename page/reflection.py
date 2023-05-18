import streamlit as st

def app():
   st.title("Reflection for each member")
   with st.expander("If we had more time, we would have..."):
      st.write("- We would have more time to do more feature engineering and more data exploration")
      st.write("- We would have more time to do more data visualization")
      st.write("- We would have more time to do more data analysis by asking more meaningful questions")
      
   with st.expander("What difficulties have you encountered?"):
      st.subheader("- 20127458 - Đặng Tiến Đạt")
      st.markdown('- Github: merge code with notebook files (conflict,...)')
      st.markdown('- For each step:')
      st.markdown("> - Data engineer: Data exchange protocols, choose the right API for you and the params, headers, ... required to be able to request the API. Data cleaning is not good, leading to errors when the model")
      st.markdown("> - Data analyst: Choose how to visualize to be reasonable for the question you posed, statistical methods to find that question.")

      st.subheader("- 20127627 - Nguyễn Quốc Thắng")
      st.markdown('> -  About data collection, I had difficulty in crawling data by getting API.Finding data and how to crawl using the API is also the first time, so it is quite difficult.')
      st.markdown('> - About clear and preprocess data: It is quite difficult to clear data from crawl data, data is missing, data type is wrong a lot, making it quite difficult for me to keep or delete that row. And about the examination as well as asking questions and answering, as this is the first time, it is a challenge to ask meaningful questions and answer them.')
      
      st.subheader("- 20127680 - Phạm Thị Ánh Phát")
      st.markdown("> - The data is too small to be able to extract the information. Difficulty asking and answering questions")
      st.markdown("> - Challenge in using Streamlit")
      st.markdown("> - Difficulty in choosing the right data")
      
      st.subheader("- 20127084 - Nguyễn Ngọc Bảo Trâm")
      st.markdown("> - Difficulty in choosing the right data")
      st.markdown("> - Challenge in using new tools")
      st.markdown("> - Difficulty in choosing time to meet and discuss")
      
   with st.expander("What did you learn?"):
      st.subheader("- 20127458 - Đặng Tiến Đạt")
      st.markdown("> - Proficient with numpy, pandas")
      st.markdown("> - Workflow with data")
      st.markdown("> - Know how to ask questions and answer them yourself")
      st.markdown("> - Know how to use Streamlit")
      
      st.subheader("- 20127627 - Nguyễn Quốc Thắng")
      st.markdown("> - Proficient with numpy, pandas")
      st.markdown("> - Workflow with data")
      st.markdown("> - Know how to use Streamlit")
      st.markdown("> - Know how to ask questions and answer them yourself")
      
      st.subheader("- 20127680 - Phạm Thị Ánh Phát")
      st.markdown("> - Proficient with numpy, pandas")
      st.markdown("> - Workflow with data")
      st.markdown("> - Know how to use Streamlit")
      st.markdown("> - Know how to ask questions and answer them yourself")
      
      st.subheader("- 20127084 - Nguyễn Ngọc Bảo Trâm")
      st.markdown("> - Proficient with numpy, pandas")
      st.markdown("> - Workflow with data")
      st.markdown("> - Know how to use Streamlit")
      st.markdown("> - Know how to ask questions and answer them yourself")
      
   st.markdown(
    """
      <style>
      .streamlit-expanderHeader > div > p {
         font-size: x-large;
         font-weight: 700;
      }
      </style>
   """,
    unsafe_allow_html=True,
   )