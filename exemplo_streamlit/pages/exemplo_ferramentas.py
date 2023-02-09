"""
Página com os exemplos das feramentas do Streamlit.
"""

import numpy as np
import streamlit as st

# A função write recebe uma string com o conteúdo em markdown
st.write("""
# Exemplo das Ferramenas do Streamlit

## Títulos

Títulos são colocados com o caractere '#'. Quanto mais '#' o título possui, menor ele é.

## Imagens

![Logo do LNTSold](http://www.lntsold.com.br/images/logos/logo_linkedin.png)

## Tabelas

Número | Par ou Ímpar
:----: | :----:
1      | Ímpar
2      | Par
3      | Ímpar
4      | Par
5      | Ímpar
6      | Par
7      | Ímpar
8      | Par

## Gráficos
""")

# Vetor de exemplo com vários dados
y = np.array(range(100))

# A função line_chart é utilizada para criar gráficos
st.line_chart(y)
