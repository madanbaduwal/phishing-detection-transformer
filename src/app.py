"""IN this model we create a simple web app.
We take input from user(UI) and
do prediction using src/models/predict_model.py"""
import datetime
import os
import sys
import base64
import urllib
import requests

# we up directory
print("This is from streamlit",sys.path.append(os.path.join(os.path.dirname(__file__), "..")))

pwd = os.getcwd()
print(pwd)

import numpy as np
import streamlit as st

from inference import inference

api_key = "Xa4TEDdRpvF91scwtEHxJum4bit1lqYN" # Replace with your PhishTank API key


def app():
    # """Function that create web app"""

    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # st.set_page_config(layout="wide")
    # Add text and data

    # Add a title
    # st.title('My first app')
    # Along with magic commands, st.write() is Streamlit’s “Swiss Army knife”.
    # You can pass almost anything to st.write():
    # text, data, Matplotlib figures, Altair charts, and more. Don’t worry,
    #  Streamlit will figure it out and render things the right way.
    # st.write()  # write
    # your own markdown.
    st.markdown(
        """<h1 style='text-align: center; color: black;'>
            Phishing Detection Using Transformer</h1>""",
        unsafe_allow_html=True,
    )

    # Write a data frame
    # st.dataframe()
    # st.table()

    # Use magic (streamlit call nagarikana ni dherai garna milxa)
    # """
    # # My first app
    # Here's our first attempt at using data to create a table:
    # """

    # df = pd.DataFrame({
    # 'first column': [1, 2, 3, 4],
    # 'second column': [10, 20, 30, 40]
    # })

    # df

    # Draw charts and maps
    # st.line/bar/..(dataframe)

    # Add interactivity with widgets
    # Checkbox
    # if st.checkbox('Show dataframe'):
    #  (click garyapaxi sabai dekhauxa tyati matra)
    #     chart_data = pd.DataFrame(
    #     np.random.randn(20, 3),
    #     columns=['a', 'b', 'c'])
    #     chart_data

    # option = st.selectbox(      # kunai auta select garyasi k garni vanni
    # 'Which number do you like best?',
    #  [1,2,3])
    # 'You selected: ', option
    #  you can put your logic here
    #  if option == 1:
    #      then...

    options = [
        "Demo",
        "About",
    ]

    option = st.sidebar.selectbox("What do you want?", options)

    # Prediction in dummy features
    if option == "Demo":
        st.markdown(
            """<h4 style='text-align: center; color: black;padding-top: 1rem;'>
            Enter URL</h4>""",
            unsafe_allow_html=True,
        )
        
        input_url = st.text_input('Enter URL', '')
        flag = 0
        first_c, second_c, third_c = st.columns(3)
        with second_c:
            if st.button("Predict"):
                    flag = 1
                    features,predictions_probability,prediction = inference(input_url)

                    # st.write(features,predictions_probability,prediction)

        first_c, second_c = st.columns(2)
        with first_c:
            st.markdown(
                """<h5 style='text-align: center; color: black;'>
                Your URL</h5>""",
                unsafe_allow_html=True,
            )
            if flag:
                st.write(input_url)
        # with second_c:                
        #         st.markdown(
        #             """<h5 style='text-align: center; color: black;'>
        #             Features</h5>""",
        #             unsafe_allow_html=True,
        #         )
        #         if flag:
        #             st.write(f"features:      {features}")
        #             f1 = features[0]
        #             st.write(f"Have_IP:       {f1}")
        #             f2 = features[1]
        #             st.write(f"Have_At:       {f2}")
        #             f3 = features[2]
        #             st.write(f"URL_Length:    {f3}")
        #             f4 = features[3]
        #             st.write(f"URL_Depth:     {f4}")
        #             f5 = features[4]
        #             st.write(f"Redirection:   {f5}")
        #             f6 = features[5]
        #             st.write(f"https_Domain:  {f6}")
        #             f7 = features[6]
        #             st.write(f"TinyURL:       {f7}")
        #             f8 = features[7]
        #             st.write(f"Prefix/Suffix: {f8}")
        #             f9 = features[8]
        #             st.write(f"DNS_Record:    {f9}")
        #             f10 = features[9]
        #             st.write(f"Domain_Age:    {f10}")
        #             f11 = features[10]
        #             st.write(f"Domain_End:    {f11}")
        #             f12 = features[11]
        #             st.write(f"iFrame:         {f12}")
        #             f13 = features[12]
        #             st.write(f"Mouse_Over:     {f13}")
        #             f14 = features[13]
        #             st.write(f"Right_Click:    {f14}")
        #             f15 = features[14]
        #             st.write(f"Web_Forwards:    {f5}")
            
        with second_c:
            st.markdown(
                """<h5 style=' color: black;'>
                Decision</h5>""",
                unsafe_allow_html=True,
            )
            # response = requests.get(f"https://developers.checkphish.ai/api/neo/scan")
            # # response = requests.get(f"https://ipqualityscore.com/api/json/url?key={api_key}&url={input_url}")
            # result = response.json()
            # print(result)
            # if flag:
            #         if result["unsafe"] == True or result["phishing"] == True or result["suspicious"] == True:
            #             st.write(f"Phishing")
            #         else:
            #             st.write(f"Non Phishing")
                        
            if flag:
                    if prediction[0] == 1:
                        st.write(f"Non Phishing")
                        st.image(f"./np-image.jpg")
                    else:
                        st.write(f"Phishing")
                        st.image(f"./p-image.jpg")
       
    if option == "About":
        st.markdown(
                """<h5 style='text-align: center; color: black;'>
                Madan Baduwal, Prakash Madai</h5>""",
                unsafe_allow_html=True,
            )
        

if __name__ == "__main__":
    app()