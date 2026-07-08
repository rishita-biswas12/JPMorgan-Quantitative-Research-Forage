import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Gas_Nat(2).csv")

df["Dates"] = pd.to_datetime(df["Dates"])

print(df.head())
print(df.info())
print(df.describe())

plt.figure(figsize=(10,5))
plt.plot(df["Dates"], df["Prices"], marker="o")
plt.title("Natural Gas Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.show()


import pandas as pd
from datetime import datetime

# Load data
df = pd.read_csv("Gas_Nat(2).csv")
df["Dates"] = pd.to_datetime(df["Dates"])


def price_storage_contract(
    injection_date,
    withdrawal_date,
    volume,
    injection_cost,
    withdrawal_cost,
    storage_cost_per_month,
):
    # Get prices for the given dates
    buy_price = df.loc[df["Dates"] == pd.to_datetime(injection_date), "Prices"].values[0]
    sell_price = df.loc[df["Dates"] == pd.to_datetime(withdrawal_date), "Prices"].values[0]

    # Calculate storage duration in months
    months = (
        (pd.to_datetime(withdrawal_date).year - pd.to_datetime(injection_date).year) * 12
        + (pd.to_datetime(withdrawal_date).month - pd.to_datetime(injection_date).month)
    )

    # Profit calculation
    revenue = sell_price * volume
    purchase = buy_price * volume
    storage_cost = months * storage_cost_per_month
    total_cost = purchase + injection_cost + withdrawal_cost + storage_cost

    profit = revenue - total_cost

    return profit


# Example
profit = price_storage_contract(
    injection_date="2023-01-31",
    withdrawal_date="2023-09-30",
    volume=1000000,
    injection_cost=10000,
    withdrawal_cost=10000,
    storage_cost_per_month=1000,
)

print(f"Estimated Profit: ${profit:,.2f}")


def price_storage_contract(injection_date, withdrawal_date,
                           volume, injection_cost,
                           withdrawal_cost, storage_cost_per_month):

    # Get the purchase price
    buy_price = df.loc[df["Dates"] == pd.to_datetime(injection_date), "Prices"].values[0]

    # Get the selling price
    sell_price = df.loc[df["Dates"] == pd.to_datetime(withdrawal_date), "Prices"].values[0]

    # Calculate storage duration in months
    months = (pd.to_datetime(withdrawal_date).year - pd.to_datetime(injection_date).year) * 12 + \
             (pd.to_datetime(withdrawal_date).month - pd.to_datetime(injection_date).month)

    # Calculate profit
    purchase_cost = buy_price * volume
    revenue = sell_price * volume
    storage_cost = months * storage_cost_per_month

    contract_value = revenue - purchase_cost - injection_cost - withdrawal_cost - storage_cost

    return contract_value


# Example
value = price_storage_contract(
    "2023-01-31",
    "2023-09-30",
    1000000,
    10000,
    10000,
    1000
)

print("Contract Value:", value)