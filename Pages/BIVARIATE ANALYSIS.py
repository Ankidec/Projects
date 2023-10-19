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

