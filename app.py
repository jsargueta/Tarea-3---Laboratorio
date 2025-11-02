import streamlit as st
from modulos.venta import mostrar_venta
from modulos.compra import mostrar_compra
from modulos.prdocuto import mostrar_producto
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
    opciones = ["Ventas", "Compras", "Productos"]
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    # Según la opción seleccionada
    if seleccion == "Ventas":
    mostrar_venta()
elif seleccion == "Compras":
    mostrar_compra()
elif seleccion == "Productos":
    mostrar_producto()
else:
    # Si la sesión no está iniciada, mostramos el login
    login()











