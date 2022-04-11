import pandas as pd
import numpy as np
import PIL as pil
import streamlit as st
import datetime
import plotly.express as px
import plotly.graph_objects as go
from streamlit.elements import layouts
import hydralit as hy
import boto3

s3 = boto3.resource(
    's3',
    aws_access_key_id = st.secrets["aws_access_key_id"],
    aws_secret_access_key = st.secrets["aws_secret_access_key"],
    region_name = 'us-east-1'
)
bucket = s3.Bucket('tropomino2')


st.set_page_config(page_title="TROPOMI NO2", layout= "wide")
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 1rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

##########################################################################################################################
img1 = pil.Image.open('img1.png')
#col01, col02, col03 = st.columns([2,4,2])
#col02.image(img1, use_column_width=True)


over_theme = {'txc_inactive': '#000000'}
app = hy.HydraApp(title='TROPOMINO2',
        hide_streamlit_markers=False,
        #add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below.
        use_navbar=True, 
        navbar_sticky=False,
        navbar_theme=over_theme
    )


##########################################################################################################################

@app.addapp(title='Daily TROPOMI NO2')
def DailyTROPOMINO2():
    my_expander1 = st.expander('Daily TROPOMI NO2', expanded=True)
    col01, col02, col03 = my_expander1.columns([3,3,3])
    col03.image(img1, use_column_width=True)
    daily_input = col01.selectbox('Select Location:', ['U.S.A.','California','Mid Atl', 'Mid West', 'North East', 'South East', 'Texas'], key='daily_input')
    if (daily_input=='U.S.A.'):
        col11, col12, col13 = my_expander1.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_conus/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")
    elif (daily_input=='California'):
        col11, col12, col13 = my_expander1.columns([3,3,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_california/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_CA_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")

    elif (daily_input=='Mid Atl'):
        col11, col12, col13 = my_expander1.columns([3,7,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_midAtl/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_midAtl_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")

    elif (daily_input=='Mid West'):
        col11, col12, col13 = my_expander1.columns([3,8,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_midwest/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_MW_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")
    elif (daily_input=='North East'):
        col11, col12, col13 = my_expander1.columns([3,8,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_northeast/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_EUS_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")
    elif (daily_input=='South East'):
        col11, col12, col13 = my_expander1.columns([3,8,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_southeast/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_SE_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")
    elif (daily_input=='Texas'):
        col11, col12, col13 = my_expander1.columns([3,7,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_texas/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_TX_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")

    



##########################################################################################################################

@app.addapp(title='Monthly TROPOMI NO2')
def MonthlyTROPOMINO2():
    my_expander2 = st.expander('Monthly TROPOMI NO2', expanded=True)  
    col01, col02, col03 = my_expander2.columns([3,3,3])
    col03.image(img1, use_column_width=True)
    #daily_input = col01.selectbox('Select Location:', ['U.S.A.','California','Mid Atl', 'Mid West', 'North East', 'South East', 'Texas'], key='daily_input')


app.run()





