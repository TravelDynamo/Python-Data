import pandas as pd

# 1. Load the CSV file
df = pd.read_csv("sales.csv")

# 2. Displaying rows
print("1.i) First 25 rows:")
print(df.head(25), "\n")

print("1.ii) Last 25 rows:")
print(df.tail(25), "\n")

print("1.iii) First 15 customer_name:")
print(df["customer_name"].head(15), "\n")

print("1.iv) First 15 city:")
print(df["city"].head(15), "\n")

# 3. Filtering rows: simple equality
print("2.i) Rows where Product ID == 'PD_06':")
print(df[df["Product ID"] == "PD_06"], "\n")

print("2.ii) Rows where payment_method == 'PayPal':")
print(df[df["payment_method"] == "PayPal"], "\n")

# 4. Filtering rows: AND conditions
print("3.i) Category == 'Electronics':")
print(df[df["Category"] == "Electronics"], "\n")

print("3.ii) Product ID == 'PD_06' AND payment_method == 'UPI':")
print(df[(df["Product ID"] == "PD_06") & (df["payment_method"] == "UPI")], "\n")

print("3.iii) payment_method == 'PayPal' AND Category == 'Sports & Outdoors':")
print(df[(df["payment_method"] == "PayPal") & (df["Category"] == "Sports & Outdoors")], "\n")

print("3.iv) Category == 'Electronics' AND location_id == 'LOC_01':")
print(df[(df["Category"] == "Electronics") & (df["location_id"] == "LOC_01")], "\n")

# 5. Filtering rows: OR conditions
print("4.i) Product ID == 'PD_03' OR 'PD_14':")
print(df[df["Product ID"].isin(["PD_03","PD_14"])], "\n")

print("4.ii) payment_method == 'PayPal' OR 'Net Banking':")
print(df[df["payment_method"].isin(["PayPal", "Net Banking"])], "\n")

print("4.iii) Category == 'Electronics' OR 'Home & Kitchen':")
print(df[df["Category"].isin(["Electronics", "Home & Kitchen"])], "\n")

# 6. Create new DataFrame for selected products and save to CSV
df_selected_products = df[df["Product ID"].isin(["PD_03","PD_14"])]
print("5.i) df_selected_products preview:")
print(df_selected_products.head(), "\n")

output_path = "selected_products.csv"
df_selected_products.to_csv(output_path, index=False)
print(f"6.i) Written df_selected_products to '{output_path}'")