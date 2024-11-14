# Pandas Cheat Sheet

# region Importar Pandas
import pandas as pd
# endregion

# region Crear un DataFrame
data = {
    "Nombre": ["Ana", "Juan", "María"],
    "Edad": [28, 34, 29],
    "Ciudad": ["Madrid", "Barcelona", "Valencia"]
}
df = pd.DataFrame(data)
df
# endregion

# region Leer archivos CSV
df = pd.read_csv("archivo.csv")
df = pd.read_csv("archivo.csv", header=None)
df.to_csv("archivo_salida.csv", index=False)
# endregion

# region Inspeccionar el DataFrame
df.head()
df.tail()
df.info()
df.describe()
# endregion

# region Seleccionar Datos
df["Nombre"]
df[["Nombre", "Edad"]]
df.iloc[0]
df.iloc[0:2]
df[df["Edad"] > 30]
# endregion

# region Filtrar Datos
df_filtrado = df[df["Edad"] > 30]
df_filtrado
df_filtrado = df[(df["Edad"] > 30) & (df["Ciudad"] == "Barcelona")]
df_filtrado
# endregion

# region Añadir / Eliminar Columnas
df["Salario"] = [3000, 4000, 3500]
df
df = df.drop("Salario", axis=1)
df
df = df.drop(["Ciudad", "Edad"], axis=1)
df
# endregion

# region Modificar Datos
df["Edad"] = df["Edad"] + 1
df
df.loc[df["Nombre"] == "Ana", "Edad"] = 35
df
# endregion

# region Reordenar el DataFrame
df = df.sort_values("Edad", ascending=False)
df
df = df.sort_values(["Ciudad", "Edad"], ascending=[True, False])
df
# endregion

# region Agrupación y Agregación
df_grouped = df.groupby("Ciudad")["Edad"].mean()
df_grouped
df_grouped = df.groupby("Ciudad").agg({"Edad": ["mean", "min", "max"]})
df_grouped
# endregion

# region Operaciones con Nulos
df.isnull()
df.isnull().sum()
df_sin_nulos = df.dropna()
df_sin_nulos
df_relleno = df.fillna(0)
df_relleno
# endregion

# region Combinar DataFrames
df_concatenado = pd.concat([df1, df2], axis=0)
df_concatenado
df_concatenado = pd.concat([df1, df2], axis=1)
df_concatenado
df_merged = pd.merge(df1, df2, on="ID")
df_merged
# endregion

# region Cambiar el Índice
df = df.set_index("Nombre")
df
df = df.reset_index()
df
# endregion

# region Pivot Table
pivot = df.pivot_table(values="Edad", index="Ciudad", columns="Nombre", aggfunc="mean")
pivot
# endregion

# region Guardar y Cargar DataFrames
df.to_csv("archivo.csv", index=False)
df.to_excel("archivo.xlsx", index=False)
df = pd.read_excel("archivo.xlsx")
df
# endregion

# region Importación de Librerías y Configuración Inicial
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# endregion

# region Importar el Dataset desde un Archivo Pickle
# Cargar el archivo pickle
renfe = pd.read_pickle("./df_renfe_clean")
# endregion

# region Eliminar Múltiples Columnas del DataFrame
# Eliminar varias columnas del DataFrame
renfe = renfe.drop(['CIUDAD_ORIGEN', 'CIUDAD_DESTINO', 'TIPO_TREN', 'TIPO_TARIFA', 'CLASE',
                    'PRECIO', 'TIEMPO_VIAJE', 'DIF_INI_BUS', 'FECHA_INICIO_HORA',
                    'FECHA_INICIO_NOMBREDIA', 'FECHA_INICIO_DIA', 'FECHA_INICIO_MES',
                    'FECHA_FIN_HORA', 'FECHA_FIN_NOMBREDIA', 'FECHA_FIN_DIA'], axis=1)
# endregion

# region Análisis de Correlación y Creación de un Heatmap
# Seleccionar solo columnas numéricas del DataFrame
numeric_df = renfe.select_dtypes(include=np.number)

# Calcular la matriz de correlación
corr = numeric_df.corr()

# Crear un heatmap de la matriz de correlación
plt.figure(figsize=(12, 8))  # Ajustar el tamaño de la figura
sns.heatmap(corr, cmap='coolwarm', annot=True, xticklabels=corr.columns, yticklabels=corr.columns)
plt.show()
# endregion

# region Ejemplos de Gráficos Usando Pandas y Matplotlib

# region Line Plot
# Usar 'FECHA_INICIO_DIA' como eje x para el line plot
renfe.plot(x='FECHA_INICIO_DIA', y='PRECIO', kind='line', title='Precio Over FECHA_INICIO_DIA')
plt.xlabel('Fecha de Inicio (Día)')
plt.ylabel('Precio')
plt.show()
# endregion

# region Bar Plot
# Bar plot mostrando el precio promedio por tipo de tren
renfe.groupby('TIPO_TREN')['PRECIO'].mean().plot(kind='bar', title='Average Precio per Tipo de Tren')
plt.xlabel('Tipo de Tren')
plt.ylabel('Average Precio')
plt.show()
# endregion

# region Histogram
# Histograma de la columna 'PRECIO' para ver la distribución
renfe['PRECIO'].plot(kind='hist', bins=20, title='Distribución del Precio')
plt.xlabel('Precio')
plt.show()
# endregion

# region Scatter Plot
# Scatter plot entre TIEMPO_VIAJE y PRECIO
renfe.plot(x='TIEMPO_VIAJE', y='PRECIO', kind='scatter', title='Precio vs. Tiempo de Viaje')
plt.xlabel('Tiempo de Viaje')
plt.ylabel('Precio')
plt.show()
# endregion

# region Box Plot
# Box plot para 'PRECIO' agrupado por 'CLASE'
renfe.boxplot(column='PRECIO', by='CLASE', grid=False)
plt.title('Box Plot of Precio by Clase')
plt.xlabel('Clase')
plt.ylabel('Precio')
plt.show()
# endregion

# endregion

# region Resumen de Comandos
# 1. Importar librerías: `import pandas as pd`, `import numpy as np`, `import matplotlib.pyplot as plt`, `import seaborn as sns`
# 2. Cargar pickle: `renfe = pd.read_pickle("./df_renfe_clean")`
# 3. Eliminar columnas: `renfe.drop(columns, axis=1)`
# 4. Seleccionar columnas numéricas: `numeric_df = renfe.select_dtypes(include=np.number)`
# 5. Matriz de correlación: `corr = numeric_df.corr()`
# 6. Heatmap: `sns.heatmap(corr, cmap='coolwarm', annot=True)`
# 7. Line plot: `renfe.plot(x, y, kind='line')`
# 8. Bar plot: `renfe.groupby().mean().plot(kind='bar')`
# 9. Histogram: `renfe['PRECIO'].plot(kind='hist', bins=20)`
# 10. Scatter plot: `renfe.plot(x, y, kind='scatter')`
# 11. Box plot: `renfe.boxplot(column, by, grid)`
# endregion

# region Proyecto de Análisis de Datos con Python, Numpy y Pandas

# region Importación de Librerías y Configuración
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, MinMaxScaler
# endregion

# region Conexión a Google Drive (Opcional para Google Colab)
# from google.colab import drive
# drive.mount('/content/drive')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
# endregion

# region Carga y Exploración Inicial del Dataset
renfe = pd.read_csv("renfe.csv")
renfe.head()
renfe.shape
renfe.columns
renfe.isnull().sum()
# endregion

# region Análisis de Valores Nulos y Tipos de Datos
renfe.info()
renfe.isnull().any()
# endregion

# region Conversión de Fechas a Formato DateTime
for col in ["FECHA_CONSULTA", "FECHA_INICIO", "FECHA_FIN"]:
    renfe[col] = pd.to_datetime(renfe[col])
renfe.info()
# endregion

# region Eliminación de Duplicados
renfe_sin_duplicados = renfe.drop_duplicates().copy(deep=True)
# endregion

# region Creación de Nuevas Variables
renfe_sin_duplicados["TIEMPO_VIAJE"] = (renfe_sin_duplicados["FECHA_FIN"] - renfe_sin_duplicados["FECHA_INICIO"]) / np.timedelta64(1, 'm')
renfe_sin_duplicados["DIF_INI_BUS"] = (renfe_sin_duplicados["FECHA_INICIO"] - renfe_sin_duplicados["FECHA_CONSULTA"]) / np.timedelta64(1, 'm')
# endregion

# region Análisis y Filtrado de Variables Categóricas
renfe_sin_duplicados["TIPO_TREN"].unique()
renfe_sin_duplicados["CLASE"].unique()
# endregion

# region Identificación de Valores Raros para Eliminar
def obten_lista_eliminar(dataset, columna, umbral):
    lista_borrar = []
    tabla = dataset[columna].value_counts().reset_index()
    for i in range(len(tabla)):
        if tabla.iloc[i]["count"] < umbral:
            lista_borrar.append(tabla.iloc[i][columna])
    return lista_borrar

lista_eliminar_tarifa = obten_lista_eliminar(renfe_sin_duplicados, "TIPO_TARIFA", 400)
# endregion

# region Limpieza y Relleno de Nulos
renfe_sin_duplicados.drop(renfe_sin_duplicados[renfe_sin_duplicados["DIF_INI_BUS"] < 0].index, inplace=True)
renfe_sin_duplicados["CLASE"].fillna(renfe_sin_duplicados["CLASE"].mode()[0], inplace=True)
# endregion

# region Visualización de Datos
renfe_sin_duplicados.hist("PRECIO")
# endregion

# region Guardar el DataFrame Limpio
pd.to_pickle(renfe_sin_duplicados, "/content/drive/MyDrive/Colab Notebooks/Project TrenMax/dataset/renfe_clean.pkl")
# endregion

# endregion
