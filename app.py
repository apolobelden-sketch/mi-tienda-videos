import streamlit as st
from supabase import create_client

# Ponemos las llaves directo para evitar errores de Secrets
URL = "https://caocdtdhumyybumwenus.supabase.co"
KEY = "sb_publishable_LGVv1UzhDyxr1a90kT1ynw_HQPLH-Fa"

# Conexión profesional
supabase = create_client(URL, KEY)

st.title("🎬 Mi Tienda Digital")

try:
    # Usamos el comando correcto que NO da error
    response = supabase.table("productos").select("*").execute()
    
    if response.data:
        for item in response.data:
            st.subheader(item.get('nombre', 'Sin nombre'))
            # Si tienes una columna llamada 'url', mostrará el video
            url_video = item.get('url', '')
            if url_video:
                st.video(url_video)
            st.write("---")
    else:
        st.info("Conectado, pero la tabla 'productos' está vacía.")

except Exception as e:
    st.error(f"Error de conexión: {e}")
