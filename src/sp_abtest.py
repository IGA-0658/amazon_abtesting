import pandas as pd

import scipy.stats as stats

def exploracion_df_abtesting (df, col_control):
    for categoria in df[col_control].unique():
        df_filtrado = df[df[col_control] == categoria]
        print(f'Los principales estadísticos de las columnas categóricas para el grupo: {categoria.upper()} son:')
        display(df_filtrado.describe(include='object').T)
        print(f'Los principales estadísticos de las columnas numéricas para el grupo: {categoria.upper()} son:')
        display(df_filtrado.describe().T)
        print('------------------------------------------------------------------------------------------------')

#Test de normalidad
def normalidad (df, lista_metricas):
    for metrica in lista_metricas:
        statistic, p_value = stats.shapiro(df[metrica])

        if p_value > 0.05:
            print(f'Para la columna {metrica.upper()} los datos SI siguen una distribución normal')
        else:
            print(f'Para la columna {metrica.upper()} los datos NO siguen una distribución normal')

#Test de homocedasticidad
def homocedascidad (df, col_control, lista_metricas):

    for metrica in lista_metricas:
        df_grupos = []
      
        for valor in df[col_control].unique():
            
            df_grupos.append(df[df[col_control] == valor] [metrica])
            
        statistic, p_value = stats.levene(*df_grupos)
        if p_value > 0.05:
            print(f'Para la columna {metrica.upper()} las varianzas son homogéneas entre grupos, SI hay homocedascidad')
        else:
            print(f'Para la columna {metrica.upper()} las varianzas NO son homogéneas entre grupos, NO hay homocedascidad')

#Test de Mann-Whitney U
def mannwhitneyu (df, col_control, lista_metricas):

    for metrica in lista_metricas:
      
        valores_control = df[col_control].unique()

        control = df[df[col_control] == valores_control[0]][metrica]
        test = df[df[col_control] == valores_control[1]][metrica]

        statistic, p_value = stats.mannwhitneyu(control, test)
        if p_value > 0.05:
            print(f'Para la métrica {metrica.upper()}, las medianas son iguales, es decir, NO hay diferencias entre los grupos')
        else:
            print(f'Para la métrica {metrica.upper()}, las medianas NO son iguales, es decir, SÍ hay diferencias significativas entre los grupos')