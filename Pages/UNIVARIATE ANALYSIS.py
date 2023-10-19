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
st.title("Distribution of Ages")
fig = make_subplots(rows=1,cols=1)
fig.add_trace(go.Bar(y = df['Age'].value_counts().values.tolist(), 
                      x = df['Age'].value_counts().index, 
                      text=df['Age'].value_counts().values.tolist(),
              textfont=dict(size=15),
                      textposition = 'outside',
                      showlegend=False,
              marker = dict(color = '#c6ff1a',
                            line_color = 'black',
                            line_width=3)),row = 1,col = 1)

fig.update_layout(title={'y':0.9,
                         'x':0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'},
                  template='plotly_white')
fig.update_yaxes(range=[0,1300])

st.plotly_chart(fig)
st.write("OBSERVATIONS")
st.write("1.The highest number of students age is 21. 2.The second highest age of the students is 22. Usually, engineering students age will be between 19-25.But here some students age is 26+.Quite strange🤔🤔")

st.title("Distribution of Intenships")


fig1 = make_subplots(rows=1,cols=1)
fig1.add_trace(go.Bar(y = df['Internships'].value_counts().values.tolist(), 
                      x = df['Internships'].value_counts().index, 
                      text=df['Internships'].value_counts().values.tolist(),
              textfont=dict(size=15),
                      textposition = 'outside',
                      showlegend=False,
              marker = dict(color = '#c6ff1a',
                            line_color = 'black',
                            line_width=3)),row = 1,col = 1)

fig1.update_layout(title={'y':0.9,
                         'x':0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'},
                  template='plotly_white')
fig1.update_yaxes(range=[0,1500])
st.plotly_chart(fig1)
st.text("OBSERVATIONS")
st.text("1.The highest number of students haven't done any internships.2.2.The second highest internships worked by the students is 1.3.Very few students worked in 3 internships")
st.text("The student who worked in more internships automatically might be having a good experience working. It is a plus point for any placement and has a  higher chance of getting placed")

st.header("Distribution of CGPA")
fig2 = make_subplots(rows=1,cols=1)
fig2.add_trace(go.Bar(y = df['CGPA'].value_counts().values.tolist(), 
                      x = df['CGPA'].value_counts().index, 
                      text=df['CGPA'].value_counts().values.tolist(),
              textfont=dict(size=15),
                      textposition = 'outside',
                      showlegend=False,
              marker = dict(color = '#c6ff1a',
                            line_color = 'black',
                            line_width=3)),row = 1,col = 1)

fig2.update_layout(title={'y':0.9,
                         'x':0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'},
                  template='plotly_white')
fig2.update_yaxes(range=[0,1200])
st.plotly_chart(fig2)

st.text("OBSERVATIONS")
st.text("1-The Highest number of students' CGPA is7.2-The second-highest number of students' CGPA is 8.3-Very few students' CGPA is 9./nCGPA places a very important role in getting the job.")



st.header("Distribution of Hostel")
fig3 = make_subplots(rows=1,cols=1)
fig3.add_trace(go.Bar(y = df['Hostel'].value_counts().values.tolist(), 
                      x = df['Hostel'].value_counts().index, 
                      text=df['Hostel'].value_counts().values.tolist(),
              textfont=dict(size=15),
                      textposition = 'outside',
                      showlegend=False,
              marker = dict(color = '#c6ff1a',
                            line_color = 'black',
                            line_width=3)),row = 1,col = 1)

fig3.update_layout(title={'y':0.9,
                         'x':0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'},
                  template='plotly_white')
fig3.update_yaxes(range=[0,2200])
st.plotly_chart(fig3)
st.text("OBSERVATIONS")
st.text("1-Very few students stay in the hostel.2-Most of the students are local residence.")



st.title("Distribution of HistoryOfBacklogs")
fig4= make_subplots(rows=1,cols=1)
fig4.add_trace(go.Bar(y = df['HistoryOfBacklogs'].value_counts().values.tolist(), 
                      x = df['HistoryOfBacklogs'].value_counts().index, 
                      text=df['HistoryOfBacklogs'].value_counts().values.tolist(),
              textfont=dict(size=15),
                      textposition = 'outside',
                      showlegend=False,
              marker = dict(color = '#c6ff1a',
                            line_color = 'black',
                            line_width=3)),row = 1,col = 1)

fig4.update_layout(title={'y':0.9,
                         'x':0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'},
                  template='plotly_white')
fig4.update_yaxes(range=[0,3000])
st.plotly_chart(fig4)
st.text("OBSERVATIONS")
st.text("1- Very few students have a backlog.2-Most of the students don't have a backlog.3-The student who has a backlog has fewer chances of getting the job.")



st.title("Distribution of Placed or Not")
fig5 = make_subplots(rows=1,cols=1)
fig5.add_trace(go.Bar(y = df['PlacedOrNot'].value_counts().values.tolist(), 
                      x = df['PlacedOrNot'].value_counts().index, 
                      text=df['PlacedOrNot'].value_counts().values.tolist(),
              textfont=dict(size=15),
                      textposition = 'outside',
                      showlegend=False,
              marker = dict(color = '#c6ff1a',
                            line_color = 'black',
                            line_width=3)),row = 1,col = 1)

fig5.update_layout(title={'y':0.9,
                         'x':0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'},
                  template='plotly_white')
fig5.update_yaxes(range=[0,2000])
st.plotly_chart(fig5)
st.text("OBSERVATIONS")
st.text("1- Very few students didn't get the job.2-Most of the students got their job.")




st.title("Distribution of Gender")
fig6 = make_subplots(rows=1,cols=1)
fig6.add_trace(go.Bar(y = df['Gender'].value_counts().values.tolist(), 
                      x = df['Gender'].value_counts().index, 
                      text=df['Gender'].value_counts().values.tolist(),
              textfont=dict(size=15),
                      textposition = 'outside',
                      showlegend=False,
              marker = dict(color = '#c6ff1a',
                            line_color = 'black',
                            line_width=3)),row = 1,col = 1)

fig6.update_layout(title={'y':0.9,
                         'x':0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'},
                  template='plotly_white')
fig6.update_yaxes(range=[0,3000])
st.plotly_chart(fig6)
st.text("OBSERVATIONS")
st.text("1-Most of the students are Male.2-Very few students are Female.")

st.title("Distribution of Stream")
fig7 = make_subplots(rows=1,cols=1)
fig7.add_trace(go.Bar(y = df['Stream'].value_counts().values.tolist(), 
                      x = df['Stream'].value_counts().index, 
                      text=df['Stream'].value_counts().values.tolist(),
              textfont=dict(size=15),
                      textposition = 'outside',
                      showlegend=False,
              marker = dict(color = '#c6ff1a',
                            line_color = 'black',
                            line_width=3)),row = 1,col = 1)

fig7.update_layout(title={'y':0.9,
                         'x':0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'},
                  template='plotly_white')
fig7.update_yaxes(range=[0,1000])
st.plotly_chart(fig7)
st.text("OBSERVATIONS")
st.text("1- The highest no. of the students' stream is Computer Science.2-2. The second highest students stream is Information Technology.3-3. Very few students' streams are Civil")







