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

st.title("Welcome to my dashboard")
# Load the image
st.image("image.jpg", use_column_width=True)
 
st.write("Engineering placement, also known as campus recruitment, is when companies come to your colleges campus, conduct interviews, and hire candidates to work in their company. These campus placements are arranged for by your college who invite all the best possible companies to recruit from their students. The campus placements are held before the final examination. These placements not only benefit the students, but they also benefit the companies and colleges") 
st.write("However, as a student, you need to prepare well for the campus placements. Getting the best companies for the placement drive is the main job of your college.The main objective of the campus placement activity is to get students a job right after they have finished their education. Since the campus placement is conducted before the final exam, students have an added incentive to do well in their final exam. Students are also under less pressure. Good placements also allow colleges to claim 100% placement which is an excellent form of advertising for them. Companies get to snatch up talented people who will do some great work for their business.")


