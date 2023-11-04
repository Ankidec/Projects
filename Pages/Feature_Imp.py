import streamlit as st
import numpy as np # linear algebra....
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)....
from matplotlib import pyplot as plt #Visualization of the data....
import warnings
warnings.filterwarnings("ignore")
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
import plotly.graph_objs as go
import matplotlib as mp
import matplotlib.patches as mpatches
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from plotly import tools
from plotly.subplots import make_subplots
from plotly.offline import iplot
import missingno as mn


df=pd.read_csv(r"C:\Users\PS3\Documents\Projects\Dataset\collegePlace (1).csv")
st.title("Feature Importance:📊:")
plt.figure(figsize = (10,6))
sns.barplot(x = feature, y = feature.index,color = '#c6ff1a')
plt.title("Feature Importance")
plt.xlabel('Score')
plt.ylabel('Features')
plt.show()