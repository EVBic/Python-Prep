

#Escenario: Imagina un conjunto de datos de edades y queremos categorizarlas como "Joven" o "Adulto" según un umbral.
#Implementación:

import pandas as pd

# DataFrame de ejemplo
datos = {'Edades': [25, 30, 18, 40, 15]}
df = pd.DataFrame(datos)

# Función where
df['Categoria'] = df['Edades'].where(df['Edades'] > 18, 'Joven')


#Escenario: Tenemos datos financieros y queremos clasificar las transacciones como "Ingreso" o "Gasto" según el monto.
#Implementación:

import pandas as pd

# DataFrame de ejemplo
datos_financieros = {'Transacciones': ['Compra', 'Venta', 'Transferencia', 'Compra', 'Transferencia'],
                     'Monto': [ -500, 1000, -200, -300, -150]}
df_financiero = pd.DataFrame(datos_financieros)

# Función where
df_financiero['Tipo'] = df_financiero['Monto'].where(df_financiero['Monto'] > 0, 'Gasto').where(df_financiero['Monto'] <= 0, 'Ingreso')