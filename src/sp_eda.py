import pandas as pd

#SRC para EDA Preliminar, recopilación codigo en una función.
def eda_preliminar(df):

    """
    Realiza un análisis exploratorio preliminar sobre un DataFrame dado.

    Este análisis incluye:
    - Muestra aleatoria de 5 filas del DataFrame.
    - Información general del DataFrame (tipo de datos, nulos, etc.).
    - Porcentaje de valores nulos por columna.
    - Conteo de filas duplicadas.
    - Distribución de valores para columnas categóricas.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.

    Returns:
    None
    """
    
    display(df.sample(5))  #Muestreo aleatorio
    print('--------------------------')
    print('DIMENSIONES DEL DATASET')
    print(f'El conjunto de datos tiene {df.shape[0]} filas y {df.shape[1]} columnas.')
    print('--------------------------')
    print('INFO')
    display(df.info())  #Info del df
    print('--------------------------')
    print('VALORES NULOS')
    display(df.isnull().mean()*100)  # % de nulos
    print('--------------------------')
    print('DUPLICADOS')
    print(f'Hay un total de {df.duplicated().sum()} duplicados') #Duplicados
    print('FRECUENCIAS DE CATEGÓRICAS')
    for col in df.select_dtypes(include='object').columns: 
        print(col.upper())
        print(df[col].value_counts())
        print('--------------------------')
    