import streamlit as st
from supabase import create_client

# Leemos las llaves de los Secrets de Streamlit
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_ANON_KEY"]

# Creamos el cliente de conexión
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("🎬 Mi Tienda Digital")

try:
    # Intentamos traer los datos
    data = supabase.table("productos").select("*").execute()
    st.success("✅ Conectado correctamente")
    
    if data.data:
        st.write(data.data)
    else:
        st.info("La tabla 'productos' está vacía, pero la conexión funciona.")
        
except Exception as e:
    st.error(f"❌ Error de conexión: {e}")
