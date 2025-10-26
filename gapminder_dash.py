import pandas as pd
import streamlit as st 
import plotly_express as px
st.set_page_config(layout="wide")

st.markdown("# Gapminder Dashboard")

df=pd.read_csv("7 - gapminder-data-graphs.csv")

unique_years = df["year"].unique()

selected_year = st.selectbox(label="Select Year",
                             options=unique_years)

df_plot = df[df["year"]==selected_year]


average_gdp = round(df_plot["gdp"].mean(),2)
average_life_exp = round(df_plot["life_exp"].mean(),2)
average_hdi = round(df_plot["hdi_index"].mean(),2)

col1,col2,col3=st.columns([1,1,1])
col1.metric(label = "Average GDP", value=average_gdp)
col2.metric(label = "Average_life_exceptency", value=average_life_exp)
col3.metric(label="Average_HDI",value=average_hdi)


title=f"Plot Of GDP VS Life_Exp For Year {selected_year}"
scatter_plot = px.scatter(data_frame=df_plot,
                          x="gdp", y="life_exp",
                          color="continent",title=title)
st.plotly_chart(scatter_plot)

col4,col5=st.columns([1,1])
with col4:
    title1=f"Plot Of Box for Life_exp {selected_year}"
    box_life_exp = px.box(data_frame=df_plot,
                            x="continent", y="life_exp",title=title1)
    st.plotly_chart(box_life_exp)
    
with col5:
    title2=f"Plot Of Histogram for Life_exp {selected_year}"
    hist_life_exp = px.histogram(data_frame=df_plot,
                             x="life_exp",title=title2)
    st.plotly_chart(hist_life_exp)
    
    
col6,col7=st.columns([1,1])
with col6:
    title3=f"Plot Of Box for GDP {selected_year}"
    box_gdp = px.box(data_frame=df_plot,
                            x="continent", y="gdp",title=title3)
    st.plotly_chart(box_gdp)
    
with col7:
    title4=f"Plot Of Histogram for GDP {selected_year}"
    hist_gdp = px.histogram(data_frame=df_plot,
                             x="gdp",title=title4)
    st.plotly_chart(hist_gdp)
    
    
col8,col9=st.columns([1,1])
with col8:
    title5=f"Plot Of Box for HDI {selected_year}"
    box_hdi = px.box(data_frame=df_plot,
                            x="continent", y="hdi_index",title=title5)
    st.plotly_chart(box_hdi)

with col9:
    title6=f"Plot Of Histogram for HDI {selected_year}"
    hist_hdi = px.histogram(data_frame=df_plot,
                            x="hdi_index",title=title6)
    st.plotly_chart(hist_hdi)
    

    
