import streamlit as st
import time

st.set_page_config(page_title="Password", layout="centered")

st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("Réinitialisation du mot de passe")

utms = st.query_params
if "token" not in utms.keys():
    st.switch_page("Home.py")
else:
    new_mdp_1 = st.text_input("Nouveau mot de passe:", type="password")
    new_mdp_2 = st.text_input("Confirmer nouveau mot de passe:", type="password")
    if st.button("Réinitialiser") or (new_mdp_1 and new_mdp_2):
        if len(new_mdp_1 or "") >= 4 and new_mdp_1 == new_mdp_2:
            auth = update_password(token, new_mdp_1)
            if auth:
                st.success("Votre mot de passe a bien été mis à jour")
                st.session_state.token = auth["token"]
                time.sleep(3)
                st.switch_page("Home.py")
            else:
                st.error("Le token renseigné n'est pas valide")
                time.sleep(3)
                st.switch_page("pages/LogIn.py")
        elif len(new_mdp_1 or "") < 4:
            st.error("Le mot de passe doit comporter quatre caractères ou plus")
        else:
            st.error("Les mots de passe renseignés doivent être identiques")