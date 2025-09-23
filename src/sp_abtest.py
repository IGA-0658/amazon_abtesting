import pandas as pd

def exploracion_df_abtesting (df, col_control):
    for categoria in df[col_control].unique():
        df_filtrado = df[df[col_control] == categoria]
        print(f'Los principales estadísticos de las columnas categóricas para el grupo: {categoria.upper()} son:')
        display(df_filtrado.describe(include='object').T)
        print(f'Los principales estadísticos de las columnas numéricas para el grupo: {categoria.upper()} son:')
        display(df_filtrado.describe().T)
        print('------------------------------------------------------------------------------------------------')