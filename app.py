import streamlit as st
from supabase import create_client

# Conexión con los Secrets que ya guardaste
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.title("🎬 Mi Tienda Digital")

try:
    # Traemos los datos de la tabla 'productos'
    datos = supabase.table("productos").select("*").execute()
    
    if datos.data:
        for item in datos.data:
            st.subheader(item.get('nombre', 'Sin nombre'))
            # Si en tu tabla la columna se llama 'url', aquí se verá el video
            st.video(item.get('url', ''))
    else:
        st.info("La base de datos está vacía.")
        
except Exception as e:
    st.error(f"Error: {e}")
