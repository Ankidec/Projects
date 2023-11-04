import streamlit as st
import numpy as np # linear algebra....
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)....
from matplotlib import pyplot as plt #Visualization of the data....
import warnings
warnings.filterwarnings("ignore")
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
import plotly.graph_objs as go
import matplotlib as mpl
import matplotlib.patches as mpatches
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from plotly import tools
from plotly.subplots import make_subplots
from plotly.offline import iplot
import missingno as mn

df=pd.read_csv(r"C:\Users\PS3\Documents\Projects\Dataset\collegePlace (1).csv")
#plotting all the graphs
st.title("Ages Vs Placed or NOT")

fig = px.histogram(df, x="Age", color ="PlacedOrNot", pattern_shape="PlacedOrNot",
                   template='plotly_white', barmode='group',color_discrete_sequence=['greenyellow'])

fig.update_layout(bargap=0.2)
st.plotly_chart(fig)

fig1= px.histogram(df, x="Student_Age", color ="PlacedOrNot", pattern_shape="PlacedOrNot",
                   template='plotly_white', barmode='group',color_discrete_sequence=['greenyellow'])

fig1.update_layout(bargap=0.2)
st.plotly_chart(fig1)
st.write("OBSERVATIONS")
st.write("1-Students whose age is 21 & 22 have more chances of getting placed through campus placements. 2-Students whose age is between 28-30 have fewer chances of getting placed in the organization.")



st.title("Gender Vs Placed or NOT")
fig2 = px.histogram(df, x="Gender", color ="PlacedOrNot", pattern_shape="PlacedOrNot",
                   template='plotly_white', barmode='group',color_discrete_sequence=['greenyellow'])

fig2.update_layout(bargap=0.2)
st.plotly_chart(fig2)
st.write("OBSERVATIONS")
st.write("1. As per the data, we can say that most of the students who got placed are Male than female.")


st.title("Interships Vs Placed or NOT")
fig3 = px.histogram(df, x="Internships", color ="PlacedOrNot", pattern_shape="PlacedOrNot",color_discrete_sequence=['greenyellow'],
                   template='plotly_white', barmode='group')

fig3.update_layout(bargap=0.2)
st.plotly_chart(fig3)
st.write("OBSERVATIONS")
st.write("1- Most of the students who got placed have done either 0 or 1 internships. 2- Very few students have done 3 internships and got placed successfully.")

st.title("CGPA Vs Placed or NOT")
fig4 = px.histogram(df, x="CGPA", color ="PlacedOrNot", pattern_shape="PlacedOrNot",color_discrete_sequence=['greenyellow'],
                   template='plotly_white', barmode='group')

fig4.update_layout(bargap=0.2)
st.plotly_chart(fig4)
st.write("OBSERVATIONS")
st.write("1- Most of the students who got placed have scored 8 in CGPA.2- Very few students have scored 5 and got placed successfully")


st.title("Hostels Vs PlacedorNOT")
fig5 = px.histogram(df, x="Hostel", color ="PlacedOrNot", pattern_shape="PlacedOrNot",
                   template='plotly_white', barmode='group',color_discrete_sequence=['greenyellow'])

fig5.update_layout(bargap=0.2)
st.plotly_chart(fig5)
st.write("OBSERVATIONS")
st.write("1-Most of the students who got placed are from local residency.2-Very few students stays in the hostel and got placed successfully")


st.title("Stream Vs PlacedorNOT")
fig6 = px.histogram(df, x="Stream", color ="PlacedOrNot", pattern_shape="PlacedOrNot",
                   template='plotly_white', barmode='group',color_discrete_sequence=['greenyellow'])

fig6.update_layout(bargap=0.2)
st.plotly_chart(fig6)
st.write("OBSERVATIONS")
st.write("1-Most of the students who got placed are from Computer Science and Information Technology Stream.2-Very few students from the Civil and Electrical stream and got placed successfully. ")



st.title("HistoryOfBacklogs Vs PlacedorNOT")
fig7 = px.histogram(df, x="HistoryOfBacklogs", color ="PlacedOrNot", pattern_shape="PlacedOrNot",
                   template='plotly_white', barmode='group',color_discrete_sequence=['greenyellow'])

fig7.update_layout(bargap=0.2)
st.plotly_chart(fig7)
st.write("OBSERVATIONS")
st.write("1-Most of the students who got placed have no backlogs. 2-Very few students have a backlog ,got placed successfully.")










