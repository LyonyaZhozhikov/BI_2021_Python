# # 4
#
# import numpy as np
# import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# file_gff = 'rrna_annotation.gff'
# def read_gff(file):
#     list_col = ['chromosome', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes']
#     gff_like = pd.read_csv(file, sep='\t', names=list_col, comment='#')
#     return gff_like
#
# read_gff(file_gff).head()
#
# file_bed = 'alignment.bed'
# def read_bed6(file):
#     list_col = ['chromosome', 'start', 'end', 'name', 'score', 'strand']
#     bed_like = pd.read_csv(file, sep='\t', names=list_col)
#     return bed_like
#
# read_bed6(file_bed).head()
#
# file_gff = 'rrna_annotation.gff'
# def read_gff_modified(file):
#     list_col = ['chromosome', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes']
#     gff_like = pd.read_csv(file, sep='\t', names=list_col, comment='#')
#     gff_like['attributes'] = gff_like['attributes'].str[5:8].replace({'5S_': '5S'})
#     return gff_like
#
# read_gff_modified(file_gff)
#
# def RNA_counter(file):
#     return read_gff_modified(file).groupby('chromosome').attributes.value_counts()
# RNA_counter(file_gff)
#
# plt.rcParams['figure.figsize'] = 25, 15
# RNA_counter(file_gff).unstack().plot.barh();
#
# df_gff = read_gff_modified(file_gff)
# df_gff
#
# df_bed = read_bed6(file_bed)
# df_bed
#
# merged = df_gff.merge(df_bed, on=['chromosome'], suffixes=('_gff', '_bed'))
# merged
#
# merged_modified = merged.query('(start_gff-1) >= start_bed and (end_gff-1) < end_bed')
#
# merged_modified
#
# # 3
#
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set();
#
# df = pd.read_csv('cardio_train.csv', sep=';')
# df.set_index('id', inplace=True)
#
# df.head()
#
# df.head().T
#
# # some info
# df.info()
#
# # some statistics
# df.describe().T
#
# # how many of them have heart disease
# df['cardio'].value_counts()
#
# # % representing
# df['cardio'].value_counts(normalize=True) * 100
#
# # normal distribution found
# df['height'].hist(bins=40);
#
# # увидим 'выбросы' на этом графике
# sns.boxplot(x=df['height']);
#
# # преобразуем возраст - дни в количество лет
# df['age'] = (df['age'] / 365).round()
# df.head()
#
# # узнаем средний возраст больных и здоровых по ССЗ
# df.groupby('cardio')['age'].mean()
#
# df.groupby('cardio')['age'].mean().plot.bar(rot=0,xlabel='heart broken)', ylabel='Age');
#
# # distribution of sick and healthy peaple by age
# plt.figure(figsize=(25, 10)) # starting from 55 age sick people are prevalent
# sns.countplot(y='age', hue='cardio', data=df);
#
# plt.scatter(df['age'], df['height']);
#
# sns.jointplot(x='height', y='weight', data=df);
# # похоже есть аномалии в данных, либо исследования проводились у людей с низкорослостью
#
# df.pivot_table(values=['age', 'cardio'], index=['smoke', 'alco'], aggfunc='mean')
# # strange thing that smoking is not correlating with alco
# # наоборот среди курящих и пьющих ССЗ встречается реже) но только если курить, у некурящих пьющих всё плохо
#
# pd.crosstab(df['smoke'], df['alco'])
# # но на кросстаблице видно что подавляющее большинство респондентов непьющие и некурящие, скорее всего сказки выше
# стоит забыть
#
# h = df['height'] # looks like data in cm
# h
#
# h_meters = h / 100 # cm > m
# h_meters[:10] # now it can fit for further BMI index calculations
#
# # вот столько пацеинтов с низкорослостью нашлось, почти столько же сколько в выборке моей кандидатской)
# h[h < 125].shape[0]
#
# # средний возраст курящих
# df[df['smoke'] == 1]['age'].mean()
#
# # средний возраст курящих гипертоников
# df[(df['smoke'] == 1) & (df['cardio'] == 1)]['age'].mean()
#
# # удалим всех с аномальным ростом
# dummy_df = df.drop(df[(df['height'] < 125) | (df['height'] > 200)].index)
# # посмотрим сколько они занимали места в выборке
# dummy_df.shape[0] / df.shape[0]
#
# df = df.drop(df[(df['height'] < 125) | (df['height'] > 200)].index)
#
# # add column with metres for height and deletes previous with cm
# df['height_m'] = df['height'] / 100
# df = df.drop('height', axis=1)
# df.head()
#
# # same thing with cgolesterol
# NEW_cholesterol = {1:'malo', 2:'norm', 3:'mnogo'}
# df['NEW_cholesterol'] = df['cholesterol'].map(NEW_cholesterol)
# df = df.drop('cholesterol', axis=1)
# df.head()
#
# # converting 1/0 to True/False
# df['cardio'] = df['cardio'].astype(bool)
# df['gluc'] = df['gluc'].astype(bool)
# df['smoke'] = df['smoke'].astype(bool)
# df['active'] = df['active'].astype(bool)
# df['alco'] = df['alco'].astype(bool)
# df.head()
#
# # lets find male and female (males are taller that females)
# mystery1 = df[df['gender'] == 1]['height_m'].mean()
# mystery2 = df[df['gender'] == 2]['height_m'].mean()
# if mystery1 > mystery2:
#     print('mystery1 is Male')
# else:
#     print('mystery1 is Female')
#
# NEW_gender = {1:'Female', 2:'Male'}
# df['NEW_gender'] = df['gender'].map(NEW_gender)
# df = df.drop('gender', axis=1)
#
# df
#
# df['BMI'] = df['weight']/df['height_m']**2
#
# # вроде бы все
# df
#
# # PS: still some strange things remaining :(
# sns.jointplot(x='BMI', y='weight', data=df);
#
# sns.jointplot(x='BMI', y='height_m', data=df);
#
# # as can be seen anomalies are low height and high weight
#
# # 2
#
# df = pd.read_csv('https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv')
# df.query('matches > matches.mean()')
#
# df_selected = df.query('matches > matches.mean()').loc[: ,['pos', 'reads_all', 'mismatches', 'deletions',
# 'insertions']].set_index('pos')
#
# df_selected
#
# # 1
#
# df = pd.read_csv('https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv')
# df.loc[:,"A":"G"]
# df.set_index('pos', inplace=True)
#
# plt.rcParams['figure.figsize'] = 10, 5
# df.loc[:,"A":"G"].sum().plot.bar(ylabel='Total reads number', xlabel='Nucleotide', rot=0);
#
# plt.rcParams['figure.figsize'] = 10, 5
# df.loc[:,"A":"G"].plot.bar(stacked=True, ylabel='Number of reads', xlabel='Number of position');
#
# cutting_reads_num=6
#
# plt.rcParams['figure.figsize'] = 25, 10
# df.loc[:,"A":"G"].iloc[cutting_reads_num:-cutting_reads_num].plot.bar(stacked=True, ylabel='Number of reads',
# xlabel='Number of position',rot = 0);
# # plt.savefig('HW-pandas-1-1.png')
#
# plt.rcParams['figure.figsize'] = 25, 10
# df.loc[:,"A":"G"].iloc[cutting_reads_num:-cutting_reads_num].plot.bar(subplots=True, ylabel='Number of reads',
# xlabel='Number of position',rot = 0);
# # plt.savefig('HW-pandas-1-2.png')
#
