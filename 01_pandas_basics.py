#  Day 1 - Pandas Practice
# Author: Yorqinoy
# GitHub: https://github.com/yorqinoyyy
# Description: This file contains Pandas practice examples 
import pandas as pd
import numpy as np

# 1. Pandas versiyasini tekshirish
print(pd.version)

# 2. Dictionary dan DataFrame yaratish
data = {
    "Name": ["Ali", "Vali", "Hasan", "Husan"],
    "Age": [25, 30, 28, 35],
    "City": ["Tashkent", "Samarkand", "Bukhara", "Andijan"]
}
df = pd.DataFrame(data)
print(df)

# 3. CSV fayl yuklash (onlayn manbadan)
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df_csv = pd.read_csv(url)
print(df_csv.head())

# 4. DataFrame haqida umumiy ma’lumot olish
print(df.info())

# 5. Ustunlarni ko‘rish
print(df.columns)

# 6. Qatorlar va ustunlar soni
print(df.shape)

# 7. Bir ustunni tanlash
print(df["Name"])

# 8. Bir nechta ustunlarni tanlash
print(df[["Name", "City"]])

# 9. Qatorlarni indeks bo‘yicha olish (iloc)
print(df.iloc[0])  # Birinchi qator
print(df.iloc[0:2])  # Birinchi ikki qator

# 10. Qatorlarni shart bo‘yicha filtrlash
print(df[df["Age"] > 28])

# 11. Yangi ustun qo‘shish
df["Country"] = "Uzbekistan"
print(df)

# 12. Ustun nomini o‘zgartirish
df.rename(columns={"Name": "Full Name"}, inplace=True)
print(df)

# 13. NaN qiymatlar yaratish va to‘ldirish
df_nan = df.copy()
df_nan.loc[1, "Age"] = np.nan
print(df_nan)
df_nan.fillna({"Age": df_nan["Age"].mean()}, inplace=True)
print(df_nan)

# 14. Ustun bo‘yicha tartiblash
print(df.sort_values(by="Age", ascending=False))

# 15. DataFrame’ni CSV faylga saqlash
df.to_csv("pandas_day1_output.csv", index=False)
