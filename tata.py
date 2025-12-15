import pandas as pd

# change the path/name to your actual file
df = pd.read_csv(r"C:\Users\HP\Downloads\Delinquency_prediction_dataset.csv")   # or pd.read_excel("geldium_data.xlsx")

# quick look
print(df.shape)      # rows, columns
print(df.head())
print(df.info())
print(df.describe(include="all"))
# Step 1 – Missing values and basic overview

missing_count = df.isna().sum()
missing_pct = df.isna().mean() * 100
missing_table = pd.DataFrame({
    "missing_count": missing_count,
    "missing_pct": missing_pct.round(2)
}).sort_values("missing_pct", ascending=False)

print(missing_table)
target = "Delinquent_Account"

corr = df.corr(numeric_only=True)[target].sort_values(ascending=False)
print(corr)


