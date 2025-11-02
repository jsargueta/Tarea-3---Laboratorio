import streamlit as st
from modulos.config.conexion import obtener_conexion

def mostrar_producto():
    st.header("📦 Gestión de productos")

    try:
        con = obtener_conexion()
        cursor = con.cursor()

        # Formulario para agregar productos
        with st.form("form_producto"):
            nombre = st.text_input("Nombre del producto")
            precio = st.number_input("Precio", min_value=0.0, step=0.01, format="%.2f")
            stock = st.number_input("Stock", min_value=0, step=1)
            enviar = st.form_submit_button("✅ Agregar producto")

            if enviar:
                if nombre.strip() == "":
                    st.warning("⚠️ Debes ingresar un nombre para el producto.")
                else:
                    try:
                        cursor.execute(
                            "INSERT INTO Productos (Nombre, Precio, Stock) VALUES (%s, %s, %s)",
                            (nombre, precio, stock)
                        )
                        con.commit()
                        st.success(f"✅ Producto agregado: {nombre} (Precio: {precio}, Stock: {stock})")
                        st.experimental_rerun()
                    except Exception as e:
                        con.rollback()
                        st.error(f"❌ Error al agregar producto: {e}")

        # Mostrar productos existentes
        cursor.execute("SELECT ID, Nombre, Precio, Stock FROM Productos ORDER BY ID DESC")
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
