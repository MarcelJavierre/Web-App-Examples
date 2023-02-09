import streamlit as st

# Abre o arquivo com o documento HTML, lê todo o conteúdo e fecha o arquivo
indexFile = open("./html/index.html", "r", encoding="UTF-8")
indexContent = indexFile.read()
indexFile.close()

# Escreve o conteúdo do documento HTML na página
st.write(indexContent, unsafe_allow_html=True)
