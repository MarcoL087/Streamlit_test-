import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

# uploading the dataframe
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

# setting basics configurations of the page
st.set_page_config(page_title="Cars Analyse",
                   page_icon=":bar_chart:",
                   layout="wide")

# adding a side-bar with country option
st.sidebar.header("Please Filter Here:")
country = st.sidebar.multiselect(
    "Select Country:",
    options=df_cars["continent"].unique(),
    default=df_cars["continent"].unique()
)

# Filter the DataFrame based on selected countries
filtered_df = df_cars[df_cars['continent'].isin(country)]

# uploading the image
img = Image.open('img_cars1.jpg')

st.image(img)

# setting the title
st.title('Hello Wilders, welcome to my application!')
st.markdown("##")

# setting database description
st.write("Here you will find our first analysis on the dataset cars")
st.write("The dataset has the following structure")
st.write(filtered_df)  # Display the filtered DataFrame

# KPI

fig_box = px.box(filtered_df, x='continent', y='mpg', color='continent',
                 title='Miles per Gallon by Continent',
                 labels={'mpg': 'Miles per Gallon'})

fig_bar = px.bar(filtered_df, x='continent', y='hp', color='continent',
                   title='Horsepower by Continent',
                   labels={'horsepower': 'Horsepower'})

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_box, use_container_width=True)
right_column.plotly_chart(fig_bar, use_container_width=True)

fig_violin = px.violin(filtered_df, x='continent', y='year', color='continent',
                       title='Year by Continent',
                       labels={'year': 'Year'})

fig_scatter = px.scatter(filtered_df, x='weightlbs', y='hp', color='continent',
                              title='Weight vs Horsepower by Continent',
                              labels={'weightlbs': 'Weight (lbs)', 'horsepower': 'Horsepower'})

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_violin, use_container_width=True)
right_column.plotly_chart(fig_scatter, use_container_width=True)