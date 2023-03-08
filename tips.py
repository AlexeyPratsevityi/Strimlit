import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import statsmodels # для линии тренда

st.sidebar.header('Размер датасета')

def input_data_size():
    path = 'tips.csv'
    tips = pd.read_csv(path, index_col=0)
    data_size = st.sidebar.slider("Размер датасета %", 0, 100, 80)
    rand_option = st.sidebar.checkbox("Случайная выборка")
    len_data = len(tips) * data_size // 100
    if rand_option:
        return tips.sample(len_data)
    return tips.iloc[:len_data]
tips = input_data_size()
st.write("""
# Гистограмма total_bill
""")
plotly_fig = px.histogram(data_frame=tips,x='total_bill')
st.plotly_chart(plotly_fig)

st.write("""
# Scatterplot, показывающий связь между total_bill and tip""")
plotly_fig = px.scatter(data_frame=tips, x="total_bill", y="tip", trendline="ols")
st.plotly_chart(plotly_fig)

st.write("""
# График, связывающий total_bill, tip, и size
""")
plotly_fig = px.scatter(data_frame=tips, x="total_bill", y="tip", trendline="ols", color='size',color_continuous_scale=px.colors.qualitative.Bold)
st.plotly_chart(plotly_fig)

st.write("""
# Cвязь между днем недели и размером счета""")
ax = sns.relplot(data=tips, x='day', y= 'total_bill', kind='line')
st.pyplot(ax)

st.write("""
Scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу
""")
plotly_fig = px.scatter(data_frame=tips, y='day', x='tip', color='sex')
st.plotly_chart(plotly_fig)

st.write("""
Box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)
""")
plotly_fig = px.box(data_frame=tips, x='time', y='total_bill')
st.plotly_chart(plotly_fig)

st.write("""
2 гистограммы чаевых на обед и ланч. Расположите их рядом по горизонтали.""")
plotly_fig = px.histogram(data_frame=tips, x='tip', facet_col='time')
st.plotly_chart(plotly_fig)

st.write("""
2 scatterplots (для мужчин и женщин), показав связь размера счета и чаевых,
 дополнительно разбив по курящим/некурящим. Расположите их по горизонтали.""")

plotly_fig = px.scatter(data_frame=tips, x='total_bill', y='tip', color='sex', facet_col='smoker',
                        color_discrete_sequence=px.colors.sequential.Rainbow, trendline='ols', trendline_scope='overall', trendline_color_override='palegreen')
st.plotly_chart(plotly_fig)