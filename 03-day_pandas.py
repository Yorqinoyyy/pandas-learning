import pandas as pd
import numpy as np

# 1. Namuna DataFrame yaratish
data = {
    'Ism': ['Ali', 'Vali', 'Hasan', 'Dilorom', 'Jasur'],
    'Yosh': [25, 30, 22, 27, 35],
    'Shahar': ['Toshkent', 'Samarqand', 'Buxoro', 'Toshkent', 'Samarqand'],
    'Narx': [15000, 23000, 12000, 17000, 20000],
    'Buyurtma': [3, 5, 2, 4, 1],
    'Holat': ['Yangi', 'Eski', 'Yangi', 'Yangi', 'Eski']
}
df = pd.DataFrame(data)

# 2. .apply() yordamida yoshni ikki barobar oshirish
def yoshni_ikki_barobar(qiymat):
    return qiymat * 2
df['Yosh_ikki_barobar'] = df['Yosh'].apply(yoshni_ikki_barobar)

# 3. .map() bilan 'Holat' ustunini raqamli kodlarga aylantirish
mapping = {'Yangi': 1, 'Eski': 0}
df['Holat_kod'] = df['Holat'].map(mapping)

# 4. .replace() yordamida shahar nomini o‘zgartirish
df['Shahar'] = df['Shahar'].replace({'Samarqand': 'Samarkand'})

# 5. .agg() bilan guruhlangan narx ustunida agregat funktsiyalar
agg_result = df.groupby('Shahar')['Narx'].agg(['sum', 'mean', 'max'])

# 6. .apply() va lambda yordamida umumiy summa hisoblash
df['Umumiy_Summa'] = df.apply(lambda row: row['Narx'] * row['Buyurtma'], axis=1)

# 7. .groupby() va sum bilan buyurtma miqdorini guruhlash
grouped = df.groupby('Holat')['Buyurtma'].sum()

# 8. Bo‘sh qiymat yaratish va .fillna() yordamida to‘ldirish
df.loc[2, 'Narx'] = np.nan
df['Narx'] = df['Narx'].fillna(df['Narx'].mean())

# 9. .sort_values() yordamida umumiy summa bo‘yicha kamayish tartibida saralash
df_sorted = df.sort_values(by='Umumiy_Summa', ascending=False)

# 10. .drop_duplicates() yordamida takroriy qatorlarni olib tashlash
df_dup = pd.concat([df, df.iloc[0:1]])
df_no_dup = df_dup.drop_duplicates()

# 11. .astype() yordamida ustun turini o‘zgartirish
df['Buyurtma'] = df['Buyurtma'].astype(float)

# 12. .query() yordamida shart bilan ma'lumotlarni tanlash
df_filtered = df.query('Narx > 15000 and Buyurtma >= 3')

# 13. .pivot_table() yordamida pivot jadval yaratish
pivot = df.pivot_table(values='Buyurtma', index='Shahar', columns='Holat', aggfunc='sum', fill_value=0)

# 14. .reset_index() yordamida indeksni tiklash
grouped_reset = grouped.reset_index()

# 15. .rename() yordamida ustun nomini o‘zgartirish
df.rename(columns={'Yosh_ikki_barobar': 'Yosh_x2'}, inplace=True)

# 16. .applymap() yordamida faqat raqamli ustunlarga funksiya qo‘llash
def plus_100(x):
    if isinstance(x, (int, float)):
        return x + 100
    return x

df_numeric_plus100 = df.select_dtypes(include=[np.number]).applymap(plus_100)

# 17. .between() yordamida yosh oralig‘idagi ma'lumotlarni tanlash
df_between = df[df['Yosh'].between(25, 35)]

# 18. .duplicated() yordamida takroriy qatorlarni topish
duplicates = df_dup[df_dup.duplicated()]

# 19. .sample() yordamida tasodifiy qator tanlash
sample_rows = df.sample(n=2, random_state=1)

# 20. .value_counts() yordamida 'Holat' ustuni qiymatlari sonini hisoblash
holat_counts = df['Holat'].value_counts()

# 21. .corr() yordamida ustunlar orasidagi korrelyatsiya hisoblash
correlation = df[['Yosh', 'Narx', 'Buyurtma']].corr()
