import streamlit as st
from modulos.config.conexion import obtener_conexion

def mostrar_producto():
    st.header("📦 Gestión de productos")

    try:
        con = obtener_conexion()
        cursor = con.cursor()

        # Formulario para agregar un producto
        with st.form("form_producto"):
            nombre = st.text_input("Nombre del producto")
            marca = st.text_input("Marca del producto")
            enviar = st.form_submit_button("✅ Agregar producto")

            if enviar:
                if nombre.strip() == "":
                    st.warning("⚠️ Debes ingresar el nombre del producto.")
                elif marca.strip() == "":
                    st.warning("⚠️ Debes ingresar la marca del producto.")
                else:
                    try:
                        cursor.execute(
                            "INSERT INTO Productos (Nombre_producto, Marca) VALUES (%s, %s)",
                            (nombre, marca)
                        )
                        con.commit()
                        st.success(f"✅ Producto agregado: {nombre} (Marca: {marca})")
                        st.experimental_rerun()
                    except Exception as e:
                        con.rollback()
                        st.error(f"❌ Error al agregar el producto: {e}")

        # Mostrar productos existentes
        cursor.execute("SELECT Id_producto, Nombre_producto, Marca FROM Productos ORDER BY Id_producto DESC")
        productos = cursor.fetchall()
        if productos:
            st.subheader("🗂️ Productos existentes")
            st.dataframe(productos, use_container_width=True)
        else:
            st.info("No hay productos registrados aún.")

    except Exception as e:
        st.error(f"❌ Error general: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()

