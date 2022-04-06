import pandas as pd
import numpy as np
import PIL as pil
import streamlit as st
import datetime
import plotly.express as px
import plotly.graph_objects as go
from streamlit.elements import layouts
import dropbox
import hydralit as hy


dbx = dropbox.Dropbox("sl.BFOTX_ommkzLrEfwU_x8t-Hvu2hVkAjMUz9v4-JE9_qZxfBPyVCPtlt29wkyok3zcQlf3FdKYkFlUv5SJ3MPDIStWEBZlqcsZ0I0g50BnaP00RiLhzMNS6tJyP72AdYOj4xcxHg1YzOS")



st.set_page_config(page_title="TROPOMI NO2", layout= "wide")

img1 = pil.Image.open('img1.png')
img2 = pil.Image.open('img2.png')


##########################################################################################################################
col01, col02, col03 = st.columns([6,2,0.90])
col01.markdown("<h6 style='text-align: center; font-weight: bold; font-size:35pt; color: #033c5a; padding-top: 35px; '>TROPOMI NO2</h1>", unsafe_allow_html=True)
col02.image(img1,use_column_width= True)
col03.image(img2,use_column_width= True)

st.text("")
st.text("")
st.text("")
over_theme = {'txc_inactive': '#000000'}
app = hy.HydraApp(title='TROPOMINO2',
        hide_streamlit_markers=False,
        #add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below.
        use_navbar=True, 
        navbar_sticky=False,
        navbar_theme=over_theme
    )
@app.addapp(is_home=True)
def home():
    my_expander1 = st.expander('Description', expanded=True)  
    col1, col2, col3 = my_expander1.columns([1,7,1])
    #col2.markdown("<h3 style='text-align: left; font-weight: bold '>Description:</h1>", unsafe_allow_html=True)
    col2.markdown("<p style='text-align: justify;'>This website provides estimates of fine particulate matter (PM<sub>2.5</sub>) and nitrogen dioxide (NO<sub>2</sub>) concentrations and associated disease burdens in >13,000 urban areas globally from 2000-2019. Methods are consistent with the Global Burden of Disease 2019 study, to the extent possible. Please visit our <b>More Information</b> and <b>Acknowledgements</b> sections by navigating to the 'About' page.</p>", unsafe_allow_html=True)

            


##########################################################################################################################

@app.addapp(title='Daily TROPOMI NO2')
def DailyTROPOMINO2():
    my_expander2 = st.expander('Daily TROPOMI NO2', expanded=True)
    daily_input = my_expander2.selectbox('Select Location:', ['U.S.A.','California','Mid Atl', 'Mid West', 'North East', 'South East', 'Texas'], key='daily_input')
    if (daily_input=='U.S.A.'):
        col11, col12, col13 = my_expander2.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        meta, img = dbx.files_download(path=f"/TROPOMI NO2 Images/daily_conus/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_QA75.png")
        col12.image(img.content, use_column_width= True, caption = f"TROPOMI NO2 {date}")
    elif (daily_input=='California'):
        col11, col12, col13 = my_expander2.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        meta, img = dbx.files_download(path=f"/TROPOMI NO2 Images/daily_california/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_CA_QA75.png")
        col12.image(img.content, use_column_width= True, caption = f"TROPOMI NO2 California {date}")
    elif (daily_input=='Mid Atl'):
        col11, col12, col13 = my_expander2.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        meta, img = dbx.files_download(path=f"/TROPOMI NO2 Images/daily_midAtl/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_midAtl_QA75.png")
        col12.image(img.content, use_column_width= True, caption = f"TROPOMI NO2 Mid Atl {date}")
    elif (daily_input=='Mid West'):
        col11, col12, col13 = my_expander2.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        meta, img = dbx.files_download(path=f"/TROPOMI NO2 Images/daily_midwest/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_MW_QA75.png")
        col12.image(img.content, use_column_width= True, caption = f"TROPOMI NO2 Mid West {date}")
    elif (daily_input=='North East'):
        col11, col12, col13 = my_expander2.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        meta, img = dbx.files_download(path=f"/TROPOMI NO2 Images/daily_northeast/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_EUS_QA75.png")
        col12.image(img.content, use_column_width= True, caption = f"TROPOMI NO2 North East {date}")
    elif (daily_input=='South East'):
        col11, col12, col13 = my_expander2.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        meta, img = dbx.files_download(path=f"/TROPOMI NO2 Images/daily_southeast/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_SE_QA75.png")
        col12.image(img.content, use_column_width= True, caption = f"TROPOMI NO2 South East {date}")
    elif (daily_input=='Texas'):
        col11, col12, col13 = my_expander2.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        meta, img = dbx.files_download(path=f"/TROPOMI NO2 Images/daily_texas/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_TX_QA75.png")
        col12.image(img.content, use_column_width= True, caption = f"TROPOMI NO2 Texas {date}")

    



##########################################################################################################################


    



##########################################################################################################################
@app.addapp(title='About')
def About():
    my_expander4 = st.expander('About', expanded=True)  
    col21, col22, col23 = my_expander4.columns([1,7,1])


app.run()





