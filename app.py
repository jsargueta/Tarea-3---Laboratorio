import streamlit as st
from modulos.venta import mostrar_venta
from modulos.login import login

# Inicializamos las variables de sesión si no existen
if "sesion_iniciada" not in st.session_state:
    st.session_state["sesion_iniciada"] = False
if "usuario" not in st.session_state:
    st.session_state["usuario"] = ""
if "tipo_usuario" not in st.session_state:
    st.session_state["tipo_usuario"] = ""

# Verificamos si la sesión está iniciada
if st.session_state["sesion_iniciada"]:
    # Mostrar menú lateral
    opciones = ["Ventas", "Otra opción"]
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    # Según la opción seleccionada
    if seleccion == "Ventas":
        mostrar_venta()
    elif seleccion == "Otra opción":
        st.write("Has seleccionado otra opción.")
else:
    # Si la sesión no está iniciada, mostramos el login
    login()










