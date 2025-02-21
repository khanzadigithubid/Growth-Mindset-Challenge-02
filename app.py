import streamlit as st
import plotly.express as px

st.title("Streamlit and Plotly Express")

data = px.data.gapminder()

selected_year = st.sidebar.slider("Select Year", 
                                  min_value=1952, 
                                  max_value=2007, 
                                  value=2007)

selected_continent = st.sidebar.selectbox("Select Continent", 
                                          data["continent"].unique())

selected_population = st.sidebar.slider("Select Population",
                                        min_value=int(data["pop"].min()),
                                        max_value=int(data["pop"].max()),
                                        value=(int(data["pop"].min()), 
                                               int(data["pop"].max())))

st.write("selected_population", 
         selected_population)

filtered_data = data[(data["year"] == selected_year) & (
    data["continent"] == selected_continent) & 
    (data["pop"] >= selected_population[0]) & 
    (data["pop"] <= selected_population[1])]

st.table(filtered_data)

fig = px.scatter(filtered_data, 
                 x="gdpPercap", y="lifeExp", 
                 color="country",
                 size="pop",
                 size_max=60, 
                 log_x=True,
                 title=f"Life Expecancy vs GDP per capital for {selected_year}")

st.plotly_chart(fig)
