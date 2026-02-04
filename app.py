import streamlit as st
from st_supabase_connection import SupabaseConnection

# 1. Configuración de la pantalla
st.set_page_config(page_title="Mi Tienda de Videos", layout="centered")
st.title("🎥 Mi Vitrina Digital")

# 2. Conexión con tu base de datos (Supabase)
# Usaremos las llaves que encontraste en los pasos anteriores
conn = st.connection("supabase", type=SupabaseConnection)

# 3. Traer los productos de tu tabla 'productos'
items = conn.query("*", table="productos").execute()

if items.data:
    st.write("### Nuestros Productos")
    for producto in items.data:
        with st.container():
            st.subheader(f"📦 {producto['nombre']}")
            st.write(f"**Precio:** ${producto['precio']}")
            
            # Buscar el video relacionado en la tabla 'media'
            media = conn.query("url_video", table="media").eq("producto_id", producto["id"]).execute()
            
            if media.data:
                # Mostramos el video de YouTube/Drive que guardaste
                st.video(media.data[0]["url_video"])
            
            st.button(f"Comprar {producto['nombre']}", key=f"btn_{producto['id']}")
            st.divider()
else:
    st.info("Conectando con la base de datos... Asegúrate de configurar las llaves en Streamlit.")
