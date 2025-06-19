import streamlit as st
import pandas as pd
st.set_page_config(page_title="Salario mínimo nominal vs real Costa Rica 2010-2024")

st.markdown("""
# Salario mínimo nominal vs Salario real
*Josué Arias Gauna - [Email](mailto:josuearias.crc@gmail.com) - [Github](https://github.com/ariasj07) - [Website](https://github.com/ariasj07)*

### Se busca demostrar cúal es el salario mínimo real de Costa Rica año por año, tomando en cuenta como año base el salario minimo nominal del año 2010
#### Conceptos: 
- Salario nominal:
Es el monto númerico de salario, el valor absoluto
- Salario real:
Es el monto númerico de salario, ajustado a la inflación, usando el IPC (Indice de precios al consumidor)
> Númericamente un salario de año "x", se puede ver mayor al de año "y", sin embargo, puede que el poder adquisitivo con ese monto sea igual, o incluso menor que el salario del año(s) anterior(es) comparado(s), aún asi, siendo el salario númericamente mayor

Se usa la siguiente formúla para calcular el monto de **salario real**:
""")
st.latex(r"""
\text{Salario real} = \frac{\text{Salario nominal}}{\text{IPC}} * 100
""")
st.markdown("""
Este analísis usa como año base el año **2010**, con los siguientes datos, que fueron extraidos, limpiados y ordenados:
""")
salarios = pd.read_excel("salarios_2010_2024.xlsx")
ipc = pd.read_excel("ipc_2010_2024.xlsx")
st.markdown("#### Salarios mínimos por año en Costa Rica (2010-2024)")
st.dataframe(salarios[["Year", "Amount"]], hide_index=True)
st.markdown("#### IPC Costa Rica años 2010-2024 (2010=100)")
st.dataframe(ipc[["Year", "IPC"]], hide_index=True)
st.caption("Fuente: INEC (Instituto Nacional de Estadísticas y Censos)")
st.markdown(r"""
#### Crecimiento del IPC por año (2010-2024)
""")
#st.image("./aumento_ipc_2010_2024.png", caption="Elaboración: Josué Arias G. Fuente: Banco Mundial")
st.line_chart(ipc, x="Year", y="IPC_Change", x_label="Años", y_label="Porcentaje")
st.caption("Gráfico: Josué Arias Gauna. Fuente: Banco Mundial")
st.markdown(r"""
#### Crecimiento del Salario mínimo vs IPC por año (2010-2024)
""")
# st.image("./ipc_salario_minimo_porcentajes_aumento_2010_2024.png", caption="Elaboración: Josué Arias G. Fuente: Banco Mundial")
years = salarios["Year"]
print(list(years))
salarios_pct = list(salarios["Amount_Change"])
print(salarios_pct)
ipc_change = list(ipc["IPC_Change"])
print(ipc_change)
salarios_reales = pd.read_excel("salarios_reales_2010_2024.xlsx")
pct_change = pd.DataFrame({"Year": years, "Cambio en salario mínimo": salarios_pct, "Cambio en IPC": ipc_change, "Salario nominal": salarios["Amount"], "Salario real": salarios_reales["Amount"]})
print(pct_change)
st.line_chart(pct_change, x="Year", y=["Cambio en salario mínimo", "Cambio en IPC"], y_label="Porcentaje", x_label="Años")
st.caption("Gráfico: Josué Arias Gauna. Fuente: Banco Mundial")
st.markdown(r"""
#### Valor absoluto: Salario mínimo nominal vs Salario mínimo real por año (2010-2024)
""")
st.line_chart(pct_change, x="Year", y=["Salario nominal", "Salario real"], x_label="Años", y_label="Monto en colones")
st.caption("Gráfico: Josué Arias Gauna. Fuente: Banco Mundial")
