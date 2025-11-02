import streamlit as st
from modulos.config.conexion import obtener_conexion

def verificar_usuario(usuario, contrasena):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None
    else:
        st.session_state["conexion_exitosa"] = True

    try:
        cursor = con.cursor()
        query = "SELECT Usuario, Contra FROM Empleados WHERE Usuario = %s AND Contra = %s"
        cursor.execute(query, (usuario, contrasena))
        result = cursor.fetchone()
        return result[0] if result else None   # Devuelve el usuario si existe
    finally:
        con.close()


def login():
    st.title("Inicio de sesión")

    # Mostrar mensaje si hubo conexión previa
    if st.session_state.get("conexion_exitosa"):
        st.success("✅ Conexión a la base de datos establecida correctamente.")

    usuario = st.text_input("Usuario", key="Usuario_input")
    contrasena = st.text_input("Contraseña", type="password", key="Contra_input")

    if st.button("Iniciar sesión"):
        tipo = verificar_usuario(usuario, contrasena)
        if tipo:
            st.session_state["usuario"] = usuario
            st.session_state["tipo_usuario"] = tipo
            st.session_state["sesion_iniciada"] = True
            st.success(f"Bienvenido ({usuario}) 👋")
            st.rerun()
        else:
            st.error("❌ Credenciales incorrectas.")
