# streamlit/Home.py
import streamlit as st

# Lo que veremos en la pagina de inicio
st.set_page_config(
    page_title="Curae Veterinaria", 
)

st.title("Curae Veterinaria - Inicio de Sesión")
st.write("Por favor, introduzca sus credenciales para acceder.")

# Pedimos el usuario y la contraseña
usuario = st.text_input("Usuario")
password = st.text_input("Contraseña", type="password")

if st.button("Iniciar Sesión"):
    # Ponemos que el usuario sea ADMIN y la contraseña Curae1234
    if usuario == "ADMIN" and password == "Curae1234":
        st.session_state["login_correcto"] = True
        st.success("¡Login correcto! Accediendo...")
        st.balloons()
    else:
        st.error("El usuario o la contraseña son incorrectos")

# Mensaje de bienvenida si ya está logueado
if "login_correcto" in st.session_state and st.session_state["login_correcto"]:
    st.write("______")
    st.success("¡Bienvenido!")
    st.sidebar.success("Sesión iniciada.")
