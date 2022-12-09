import streamlit as st

st.title("Mon application")
a="Mon ami boby est à Baobab"
menu=["D1","D2","D3"]
choice=st.sidebar.selectbox("Menu",menu)
st.title(a)
st.markdown("Bini est de retour à Baby")
st.header("Famille PEM")
st.info("Pem commence bientôt")
a=st.text_input("Entrer votre nom")
st.success( a+" "+"Vous êtes en D1")
st.error("Vous devez valider la D1")
st.markdown("WOW")
st.slider("Années d'étude", min_value=10,max_value=20)
sepcialite=st.multiselect("Domaine",options=["PEM", "ED","GE","Ma"])

selection=st.selectbox("Diplome",options=("Licence","Master"))
data=st.date_input("Entrer la date")
