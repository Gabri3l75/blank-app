import streamlit as st

st.title("🎈 Mi nueva app")
st.write(
    "Ok Nueva 2 Vamos a iniciar a construir! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
cantidad = st.slider('Selecciona la cantidad')
st.write(f'La cantidad seleccionada es: {cantidad}')