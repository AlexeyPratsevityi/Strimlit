import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
path = '/home/alexeyprats/ds_bootcamp/ds-phase-0/learning/datasets/tips.csv'
tips = pd.read_csv(path, index_col=0)
#fig = sns.displot(data = tips, x='total_bill', kind = 'hist')
print(tips)
plotly_fig = px.histogram(data_frame=tips,x='total_bill')
st.plotly_chart(plotly_fig)