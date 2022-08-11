import snowflake.connector
import streamlit
import pandas

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("Select COLOR_OR_STYLE from Catalog")
my_data_row = my_cur.fetchall()
df = pandas.DataFrame(my_data_row)
streamlit.header("Zena's Amazing Athleisure Catalog")
streamlit.text('Pick a sweatsuit color or style:')


streamlit.write(df)


