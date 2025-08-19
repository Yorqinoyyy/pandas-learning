# pandas_series_day1.py
# Author: Yorqinoy
# GitHub: https://github.com/yorqinoyyy
# Description: 15 Pandas Series examples — basics, indexing, operations, and cleaning.

import pandas as pd
import numpy as np

print("Pandas version:", pd.version)

# 1. Listdan Series yaratish
values = [10, 20, 30, 40]
s = pd.Series(values)
print("Series from list:\n", s)

# 2. Custom index bilan Series
s2 = pd.Series(values, index=["a", "b", "c", "d"])
print("Series with custom index:\n", s2)

# 3. Dictionarydan Series yaratish
data = {"x": 100, "y": 200, "z": 300}
s3 = pd.Series(data)
print("Series from dict:\n", s3)

# 4. Series elementiga indeks orqali murojaat
print("Access element 'b':", s2["b"])

# 5. Series bo‘ylab matematik amallar
print("s + 5:\n", s + 5)

# 6. Boolean indexing
print("s2 > 25:\n", s2[s2 > 25])

# 7. isnull() va fillna() bilan ishlash
s4 = pd.Series([1, None, 3, np.nan, 5])
print("NaN in Series:\n", s4)
print("Filled NaN with 0:\n", s4.fillna(0))

# 8. dropna() yordamida NaN qiymatlarni olib tashlash
print("dropna result:\n", s4.dropna())

# 9. Value counts amalini qo‘llash
s5 = pd.Series(["apple", "banana", "apple", "cherry", "banana"])
print("Value counts:\n", s5.value_counts())

# 10. String metodlari (upper)
s6 = pd.Series(["apple", "banana", "cherry"])
print("Uppercase:\n", s6.str.upper())

# 11. Indeksni reset qilish
s7 = s2.copy()
s7.index = ["w", "x", "y", "z"]
print("Re-indexed series:\n", s7)

# 12. Convert dtype
s8 = pd.Series(["10", "20", "30"])
s8 = s8.astype(int)
print("Converted dtype to int:\n", s8)

# 13. Agregatsion statistika
print("mean:", s.mean(), "max:", s.max(), "min:", s.min())

# 14. apply() funksiyasi bilan operatsiya
def square(x): return x * x
print("Squared using apply:\n", s.apply(square))

# 15. Series’ni DataFrame’ga aylantirish
df_from_series = s.to_frame(name="Values")
print("Converted to DataFrame:\n", df_from_series.head())
