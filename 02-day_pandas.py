import pandas as pd

# 1. DataFrame yaratish
data = {'Ism': ['Ali', 'Vali', 'Hasan'],
        'Yosh': [25, 30, 22],
        'Shahar': ['Toshkent', 'Samarqand', 'Buxoro']}
df = pd.DataFrame(data)
print("DataFrame yaratish:")
print(df)

# 2. CSV fayldan ma'lumotlarni o'qish
df = pd.read_csv('fayl_nomi.csv')
print("CSV fayldan ma'lumotlarni o'qish")

# 3. Ustun tanlash
print("\n 'Ism' ustunini tanlash:")
print(df['Ism'])

# 4. Bir nechta ustun tanlash
print("\n 'Ism' va 'Yosh' ustunlarini tanlash:")
print(df[['Ism', 'Yosh']])

# 5. Qatorlarni tanlash (.iloc)
print("\n Birinchi qatorni tanlash:")
print(df.iloc[0])

# 6. Filtrlash: yosh 25 dan katta bo‘lganlar
print("\n Yosh 25 dan katta bo‘lganlar:")
print(df[df['Yosh'] > 25])

# 7. Yangi ustun qo‘shish: yoshdan 5 yil keyin
df['Yoshdan 5 yil keyin'] = df['Yosh'] + 5
print("\n Yangi ustun qo‘shish:")
print(df)

# 8. Ustun nomini o‘zgartirish
df.rename(columns={'Ism': 'Ism_Familiya'}, inplace=True)
print("\n Ustun nomini o‘zgartirish:")
print(df)

# 9. Qator o‘chirish: indeks 0
df.drop(0, axis=0, inplace=True)
print("\n Qator o‘chirish (indeks 0):")
print(df)

# 10. Ustun o‘chirish: 'Shahar'
df.drop('Shahar', axis=1, inplace=True)
print("\n Ustun o‘chirish ('Shahar'):")
print(df)

# 11. Missing qiymatlarni tekshirish
print("\n Missing qiymatlarni tekshirish:")
print(df.isnull().sum())

# 12. Missing qiymatlarni to‘ldirish (agar mavjud bo‘lsa)
df['Yosh'] = df['Yosh'].fillna(df['Yosh'].mean()) #o'rta qiymat bilan to'ldirish

# 13. Saralash: yosh bo‘yicha kamayish tartibida
df_sorted = df.sort_values(by='Yosh', ascending=False)
print("\n Saralash (Yosh bo‘yicha kamayish):")
print(df_sorted)

# 14. Guruhlash va o‘rtacha hisoblash (yangi ma'lumot bilan)
data2 = {'Shahar': ['Toshkent', 'Samarqand', 'Toshkent', 'Buxoro'],
         'Yosh': [25, 30, 28, 22]}
df2 = pd.DataFrame(data2)
grouped = df2.groupby('Shahar')['Yosh'].mean()
print("\n Guruhlash va o‘rtacha hisoblash:")
print(grouped)

# 15. Pivot jadval yaratish
pivot = df2.pivot_table(values='Yosh', index='Shahar', aggfunc='mean')
print("\n Pivot jadval:")
print(pivot)

# 16. DataFrame birlashtirish (concat)
df3 = pd.DataFrame({'Ism_Familiya': ['Diyor', 'Zafar'],
                    'Yosh': [28, 35]})
df_concat = pd.concat([df, df3], ignore_index=True)
print("\n DataFrame birlashtirish:")
print(df_concat)

# 17. DataFrame-ni CSV faylga saqlash
df_concat.to_csv('yangi_data.csv', index=False)
