# pandas_day5_6_practice.py
# Author: Yorqinoy
# GitHub: https://github.com/yorqinoyyy
# Description: 16 Pandas exercises covering selections, filtering, grouping, aggregation, merging, and handling duplicates.

import pandas as pd

# 1. CSV fayldan DataFrame yaratish
url = "https://raw.githubusercontent.com/praktikum-datasets/restaurant_sales.csv"
df = pd.read_csv(url)
print("Dataset loaded. Shape:", df.shape)

# 2. Bir nechta ustun tanlash
df_sel = df[["Category", "Quantity", "Total_Sales"]]
print("\n Selected columns:\n", df_sel.head())

# 3. Faqat toifasi 'Drinks' bo‘lganlar
drinks = df[df["Category"] == "Drinks"]
print("\n Drinks category:\n", drinks.head())

# 4. Miqdori 10 dan katta bo‘lgan satrlar
high_qty = df[df["Quantity"] > 10]
print("\n Quantity > 10:\n", high_qty.head())

# 5. Har bir toifa bo‘yicha jami sotuvlar
sales_by_cat = df.groupby("Category")["Total_Sales"].sum()
print("\n Total sales by category:\n", sales_by_cat)

# 6. Har bir filial bo‘yicha o‘rtacha narx
avg_price_branch = df.groupby("Branch")["Price"].mean()
print("\n Average price by branch:\n", avg_price_branch)

# 7. Pivot jadval: filial x toifa bo‘yicha jami miqdor
pivot_qty = df.pivot_table(index="Branch", columns="Category", values="Quantity", aggfunc="sum", fill_value=0)
print("\n Pivot table - total quantities:\n", pivot_qty)

# 8. DataFrame tartiblash: Total_Sales bo‘yicha kamayish tartibida
sorted_df = df.sort_values(by="Total_Sales", ascending=False).head(5)
print("\n Top 5 sales records:\n", sorted_df)

# 9. Yangi ustun: price * quantity
df["Revenue"] = df["Price"] * df["Quantity"]
print("\n Added Revenue column:\n", df[["Price", "Quantity", "Revenue"]].head())

# 10. Dublyat satrlarni aniqlash
duplicates = df[df.duplicated()]
print("\n Duplicate records:\n", duplicates)

# 11. Takroriy satrlarni olib tashlash
df_no_dup = df.drop_duplicates()
print("\n Shape after dropping duplicates:", df_no_dup.shape)

# 12. Ikkita DataFrame birlashtirish (filter qilingan va original)
merged = df.merge(drinks, how="left", indicator=True, on=list(df.columns))
print("\n Merged indicator:\n", merged["_merge"].value_counts())

# 13. GroupBy va agregatsiya bir nechta ustuniga
summary = df.groupby("Branch").agg({'Quantity':'sum','Total_Sales':'mean'}).reset_index()
print("\n Branch summary:\n", summary)

# 14. Filtrlash: Total_Sales > median
median_sales = df["Total_Sales"].median()
above_med = df[df["Total_Sales"] > median_sales]
print("\n Sales > median:", above_med.shape[0], "rows")

# 15. Indeksni datetime formatga o‘tkazish va turli vaqt bo‘yicha filter
df["Date"] = pd.to_datetime(df["Date"])
march = df[df["Date"].dt.month == 3]
print("\n Records in March:", march.shape[0])

# 16. Iloji bo‘lsa, indexni yangi qildik va sashiy kodni DataFrame saqladik
df_final = df.set_index(["Branch", "Category"])
df_final.to_csv("pandas_day5_6_output.csv")
print("\n Multi-index DataFrame saved to CSV. New shape:", df_final.shape)
