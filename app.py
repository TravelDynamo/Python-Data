# Importing the Streamlit library to create a web app
import streamlit as st

# Importing the pandas library to work with data in tables
import pandas as pd

# —————————————— Load Data —————————————— #
# This function loads the data from a file called "sales.csv"
# The @st.cache_data decorator makes sure the data is loaded only once to make the app faster
@st.cache_data
def load_data():
    return pd.read_csv("sales.csv")  # Read the CSV file and return it as a DataFrame (a table)

# Load the data into a variable called 'df'
df = load_data()

# Set the title of the web app
st.title("📊 Pandas Basic 1 — Interactive Answers")

# —————————————— 1. Displaying Rows —————————————— #
# Add a big header to show this section is about displaying rows
st.header("1. Displaying Rows")

# Add a smaller header for showing the first 25 rows of the table
st.subheader("1.1 First 25 rows")
st.dataframe(df.head(25))  # Show the first 25 rows of the table

# Add a smaller header for showing the last 25 rows of the table
st.subheader("1.2 Last 25 rows")
st.dataframe(df.tail(25))  # Show the last 25 rows of the table

# Add a smaller header for showing the first 15 rows of the "customer_name" column
st.subheader("1.3 First 15 rows of column `customer_name`")
st.dataframe(df["customer_name"].head(15))  # Show the first 15 rows of the "customer_name" column

# Add a smaller header for showing the first 15 rows of the "city" column
st.subheader("1.4 First 15 rows of column `city`")
st.dataframe(df["city"].head(15))  # Show the first 15 rows of the "city" column

# —————————————— 2. Filtering Rows (simple) —————————————— #
# Add a big header to show this section is about filtering rows
st.header("2. Filtering Rows — Simple Equality")

# Add a smaller header for filtering rows where "Product ID" is "PD_06"
st.subheader("2.1 `Product ID` == 'PD_06'")
st.dataframe(df[df["Product ID"] == "PD_06"])  # Show rows where "Product ID" is "PD_06"

# Add a smaller header for filtering rows where "payment_method" is "PayPal"
st.subheader("2.2 `payment_method` == 'PayPal'")
st.dataframe(df[df["payment_method"] == "PayPal"])  # Show rows where "payment_method" is "PayPal"

# Add a smaller header for filtering rows where "Category" is "Electronics"
st.subheader("2.3 `Category` == 'Electronics'")
st.dataframe(df[df["Category"] == "Electronics"])  # Show rows where "Category" is "Electronics"

# —————————————— 3. Filtering Rows — AND —————————————— #
# Add a big header to show this section is about filtering rows with AND conditions
st.header("3. Filtering Rows — AND Conditions")

# Add a smaller header for filtering rows where "Product ID" is "PD_06" AND "payment_method" is "UPI"
st.subheader("3.1`Product ID` == 'PD_06' AND `payment_method` == 'UPI'")
st.dataframe(df[(df["Product ID"] == "PD_06") & (df["payment_method"] == "UPI")])  # Show rows matching both conditions

# Add a smaller header for filtering rows where "payment_method" is "PayPal" AND "Category" is "Sports & Outdoors"
st.subheader("3.2 `payment_method` == 'PayPal' AND `Category` == 'Sports & Outdoors'")
st.dataframe(df[(df["payment_method"] == "PayPal") & (df["Category"] == "Sports & Outdoors")])  # Show rows matching both conditions

# Add a smaller header for filtering rows where "Category" is "Electronics" AND "location_id" is "LOC_01"
st.subheader("3.3 `Category` == 'Electronics' AND `location_id` == 'LOC_01'")
st.dataframe(df[(df["Category"] == "Electronics") & (df["location_id"] == "LOC_01")])  # Show rows matching both conditions

# —————————————— 4. Filtering Rows — OR —————————————— #
# Add a big header to show this section is about filtering rows with OR conditions
st.header("4. Filtering Rows — OR Conditions")

# Add a smaller header for filtering rows where "Product ID" is either "PD_03" or "PD_14"
st.subheader("4.1 `Product ID` is PD_03 or PD_14")
st.dataframe(df[df["Product ID"].isin(["PD_03","PD_14"])])  # Show rows matching either condition

# Add a smaller header for filtering rows where "payment_method" is either "PayPal" or "Net Banking"
st.subheader("4.2 `payment_method` is PayPal or Net Banking")
st.dataframe(df[df["payment_method"].isin(["PayPal","Net Banking"])])  # Show rows matching either condition

# Add a smaller header for filtering rows where "Category" is either "Electronics" or "Home & Kitchen"
st.subheader("4.3 `Category` is Electronics or Home & Kitchen")
st.dataframe(df[df["Category"].isin(["Electronics","Home & Kitchen"])])  # Show rows matching either condition

# —————————————— 5. New DataFrame + CSV —————————————— #
# Add a big header to show this section is about creating a new table and exporting it
st.header("5. New DataFrame & Export")

# Add a smaller header for creating a new table with rows where "Product ID" is "PD_03" or "PD_14"
st.subheader("5.1 Create `df_selected_products` where `Product ID` is PD_03 or PD_14")
df_selected_products = df[df["Product ID"].isin(["PD_03","PD_14"])]  # Create a new table with filtered rows
st.dataframe(df_selected_products)  # Show the new table

# Add a button to let users download the new table as a CSV file
st.markdown("**Download `df_selected_products.csv`**")
csv = df_selected_products.to_csv(index=False).encode('utf-8')  # Convert the table to a CSV file
st.download_button(
    label="Download CSV",  # Label for the button
    data=csv,  # The CSV file data
    file_name='df_selected_products.csv',  # Name of the file to download
    mime='text/csv'  # File type
)