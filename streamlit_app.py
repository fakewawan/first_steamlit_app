import streamlit;
import pandas;
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My parents new healthy diner!!');

streamlit.header('Breakfast Favorites:');

streamlit.text(' 🥣  Omega 3 & oatmeal');
streamlit.text(' 🥗  Kale & Bullshit');
streamlit.text(' 🐔  Hard boiled free range eggs');
streamlit.text('  🥑🍞  Avocado Toats');

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show=my_fruit_list.loc[fruit_selected]
# Display the table on the page.
streamlit.dataframe(fruit_to_show)

streamlit.text(fruityvice_response)
