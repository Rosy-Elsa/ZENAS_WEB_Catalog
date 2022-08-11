import snowflake.connector
import streamlit
import pandas

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("Select COLOR_OR_STYLE from Catalog")
my_data_row = my_cur.fetchall()
df = pandas.DataFrame(my_data_row)
streamlit.header("Zena's Amazing Athleisure Catalog")
#streamlit.text('Pick a sweatsuit color or style:')
#streamlit.write(df)

# put the first column into a list
color_list = df[0].values.tolist()
#print(color_list)

#streamlit.multiselect(list(color_list))
#streamlit.multiselect("Pick a sweatsuit color or style:", list(color_list)) ---This works
#streamlit.multiselect(list(color_list)) --This doesnt work!!

# Let's put a pick list here so they can pick the color
#option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))
streamlit.list(color_list)

