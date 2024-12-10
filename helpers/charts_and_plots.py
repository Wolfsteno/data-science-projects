# pie chart / plots
df_gps = df['gps'].value_counts().reset_index()
df_gps.columns = ['gps', 'count'] 

plt.figure(figsize=(5, 5))
plt.pie(df_gps['count'], labels=df_gps['gps'], autopct='%1.1f%%', startangle=90)
plt.title('Distribucion de los valores GPS')
plt.show()


# Violin Plot: tiempo vs precio
sns.violinplot(x='tiempo', y='precio', data=df)
plt.title('Violin Plot: tiempo vs precio')
plt.xlabel('Tiempo')
plt.ylabel('Precio')
plt.show()


# modelo vs precio (Grupo 1)
plt.figure(figsize=(20, 6))
sns.boxplot(x='modelo', y='precio', data=df[df['modelo'].isin(models_group_1)])
plt.title('modelo vs precio (Grupo 1)')
plt.xticks(rotation=90)
plt.show()
