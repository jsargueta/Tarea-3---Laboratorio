import streamlit as st
from modulos.config.conexion import obtener_conexion

def mostrar_compra():
    st.header("📦 Registrar compra simple")

    try:
        con = obtener_conexion()
        cursor = con.cursor()

        # Formulario para registrar la compra
        with st.form("form_compra"):
            producto = st.text_input("Nombre del producto")
            cantidad = st.number_input("Cantidad", min_value=1, step=1)
            proveedor = st.text_input("Proveedor")
            enviar = st.form_submit_button("✅ Guardar compra")

            if enviar:
                if producto.strip() == "":
                    st.warning("⚠️ Debes ingresar el nombre del producto.")
                elif proveedor.strip() == "":
                    st.warning("⚠️ Debes ingresar el nombre del proveedor.")
                else:
                    try:
                        cursor.execute(
                            "INSERT INTO Compras (Producto, Cantidad, Proveedor) VALUES (%s, %s, %s)",
                            (producto, str(cantidad), proveedor)
                        )
                        con.commit()
                        st.success(f"✅ Compra registrada correctamente: {producto} (Cantidad: {cantidad}, Proveedor: {proveedor})")
                        st.experimental_rerun()
                    except Exception as e:
                        con.rollback()
                        st.error(f"❌ Error al registrar la compra: {e}")

        # Mostrar todas las compras registradas
        cursor.execute("SELECT ID, Producto, Cantidad, Proveedor, Fecha FROM Compras ORDER BY Fecha DESC")
        compras = cursor.fetchall()
        if compras:
            st.subheader("🗂️ Compras registradas")
            st.dataframe(compras, use_container_width=True)
        else:
            st.info("No hay compras registradas aún.")

    except Exception as e:
        st.error(f"❌ Error general: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()

