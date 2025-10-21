import pandas as pd

orders = pd.read_csv("orders.csv")
rma = pd.read_csv("rma.csv")

# Top products sold
top_sold = orders.groupby("ProductName")["Quantity"].sum().sort_values(ascending=False).head(3)

# Returns by state
returns = rma.merge(orders[["OrderID","State","ProductName"]], on="OrderID", how="left")
returns_by_state = returns.groupby("State")["RMAID"].count().sort_values(ascending=False)

# Return rate by product
sold_by_product = orders.groupby("ProductName")["Quantity"].sum()
returns_by_product = returns.groupby("ProductName")["RMAID"].count()
return_rate = (returns_by_product / sold_by_product).fillna(0).sort_values(ascending=False)

print("=== Top Products Sold ===")
print(top_sold.to_string())
print("\n=== Returns by State ===")
print(returns_by_state.to_string())
print("\n=== Return Rate by Product (events per unit sold) ===")
print(return_rate.to_string())