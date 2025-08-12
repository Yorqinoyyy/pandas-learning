import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Talaba': ['Ali', 'Vali', 'Hasan', 'Dilorom', 'Jasur'],
    'Ball': [80, 92, 75, 85, 90],
    'Shahar': ['Toshkent', 'Samarqand', 'Buxoro', 'Toshkent', 'Samarqand'],
    'Status': ['Pass', 'Fail', 'Pass', 'Pass', 'Fail']
}
df = pd.DataFrame(data)

# 1. map: Statusni raqamga o‘zgartirish (Pass→1, Fail→0)
df['Status_kod'] = df['Status'].map({'Pass':1, 'Fail':0})

# 2. apply: Ballga 5 ball qo‘shish
df['Ball_plus5'] = df['Ball'].apply(lambda x: x + 5)

# 3. replace: shahar nomini inglizchaga almashtirish
df['Shahar'] = df['Shahar'].replace({'Samarqand':'Samarkand'})

# 4. agg: guruh bo‘yicha ball summary: sum va mean
agg_summary = df.groupby('Shahar')['Ball'].agg(['sum','mean'])

# 5. applymap: barcha sonli maydonlarga +10%
df_plus10 = df.select_dtypes(include=[np.number]).applymap(lambda x: x * 1.1)

# 6. query: balli 85 dan yuqori talabar
high_score = df.query('Ball > 85')

# 7. agg() per row (axis=1): row bo‘yicha sum
df['row_sum'] = df[['Ball', 'Status_kod']].agg('sum', axis=1)

# 8. fillna: bo‘sh qiymat o‘rniga 0
df.loc[2, 'Ball'] = np.nan
df['Ball'] = df['Ball'].fillna(0)

# 9. drop_duplicates: dublikat qatorlarni olib tashlash
df_dup = pd.concat([df, df.iloc[[0]]])
df_no_dup = df_dup.drop_duplicates()

# 10. sort_values: Ball bo‘yicha pasayish tartibi
df_sorted = df.sort_values(by='Ball', ascending=False)

# 11. between: Ball 80 va 90 oralig‘idagi talabar
df_between = df[df['Ball'].between(80, 90)]

# 12. duplicated: qaysi talabalarda dubliklar
dups = df_dup[df_dup.duplicated()]

# 13. sample: tasodifiy 2 qator tanlash
df_sample = df.sample(n=2, random_state=42)

# 14. value_counts: har bir status nechta
status_counts = df['Status'].value_counts()

# 15. corr: ball va kod o‘rtasidagi korrelyatsiya
corr = df[['Ball','Status_kod']].corr()

# 16. reset_index: grouped summary indeksini tiklash
agg_reset = agg_summary.reset_index()

# 17. rename: ustun nomini o‘zgartirish
df_renamed = df.rename(columns={'Talaba':'Ism'})

# 18. concat: ikki DataFrame‘ni ulash
new_df = pd.DataFrame({'Talaba':['Zafar'], 'Ball':[88], 'Shahar':['Navoiy'], 'Status':['Pass'], 'Status_kod':[1], 'Ball_plus5':[93], 'row_sum':[94]})
df_concat = pd.concat([df, new_df], ignore_index=True)

# 19. pivot_table: Shahar bo‘yicha status sum count
pivot = df.pivot_table(values='Status_kod', index='Shahar', aggfunc=['sum','count'])

# 20. basic statistics: describe()
stats = df.describe()
