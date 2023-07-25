import streamlit;
import pandas;
import requests;
import snowflake.connector;
from urllib.error import URLError;

def get_fruitvice_data(fruit_choice):
  streamlit.write('The user entered ', fruit_choice)
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  streamlit.text(fruityvice_response.json())
  # write your own comment -what does the next line do? 
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  # write your own comment - what does this do?
  return fruityvice_normalized

def get_fruit_load_list():
  my_cur.execute("SELECT * from fruit_load_list")
  my_data_rows = my_cur.fetchall()
  return my_data_rows

def insert_row_fruit_snowflake(add_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "Thanks for Adding "+ add_fruit

#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
#my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My parents new healthy diner!!');

streamlit.header('Breakfast Favorites:');

streamlit.text(' 🥣  Omega 3 & oatmeal');
streamlit.text(' 🥗  Kale & Bullshit');
streamlit.text(' 🐔  Hard boiled free range eggs');
streamlit.text('  🥑🍞  Avocado Toats');

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
#fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#fruit_to_show=my_fruit_list.loc[fruit_selected]
# Display the table on the page.
#streamlit.dataframe(fruit_to_show)

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?',)
  if not fruit_choice:
    streamlit.error("Please select a fruit")
  else :
    function_result=get_fruitvice_data(fruit_choice)
    streamlit.dataframe(function_result)
except URLError as e:
  streamlit.error();


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

if streamlit.button('Get Fruit List'):
  streamlit.header("The fruit list contains:")
  streamlit.dataframe(get_fruit_load_list())

 
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button("Add a fruit"):
  streamlit.write(insert_row_fruit_snowflake(add_my_fruit))

streamlit.stop();
