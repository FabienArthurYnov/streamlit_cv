from pathlib import Path
import time

from PIL import Image
import streamlit as st


st.set_page_config(page_title="CV | Fabien ARTHUR", page_icon="📃")


#css
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    st.header("Fabien ARTHUR")
    st.subheader("Etudiant Bachelor 2 Informatique")
with col2:
    st.image(Image.open(current_dir / "assets" / "pdp.webp"))

st.write("#")

col1, col2 = st.columns(2)
with col1:
    st.subheader("⚙️ Languages :")
    st.write("""
            - | Golang
            - | Java
            - | Javascript / HTML / CSS
            - | Python
            - | SQL
    """)
with col2:
    st.subheader("🌍 Langues :")
    st.write("""
             - | Français
             - | Anglais
             """)
    
st.write("#")
st.subheader("💼 Formation")
st.write("➖ Baccalauréat mention TB (Mathématique et Numériques & Sciences Informatiques)")
st.write("- - Lycée Paul Lapie, Courbevoie, France")
st.write("➖ Bachelor Informatique (En cours)")
st.write("- - Paris Ynov Campus, Nanterre")


st.write("#")
st.subheader("🛠️ Compétences")
st.write("""
        - Developpement de site web
        - Developpement de webapp
        - Gestion de base de données SQL
        - Réseau, Linux
         """)


st.write("#")
st.subheader("Projets personels")
tab1, tab2 = st.tabs(["FoxholeLogiHelper", "Better Enchants"])
with tab1:
    st.write("""
       🏹 Développement d'une webapp de suivis de stock pour le jeu Foxhole 🛡️
         - - 🏴 Golang, Javascript, SQL
         - - https://github.com/Fafacraft/FoxholeLogiHelper
        """)
    st.image(Image.open(current_dir / "assets" / "foxholeLogiHelperExemple.png"))
with tab2:
    st.write("""
       ⛏ Développement d'un mod Minecraft 💎
         - - 🏴 Java, json, forge API
         - - https://github.com/Fafacraft/BetterEnchants
        """)
    st.image(Image.open(current_dir / "assets" / "BetterEnchantsExemple.png"))

       
st.write("#")
st.divider()
st.subheader("🪪 Contact")
st.write("""
        - Mail : fabien.arthur@ynov.com
        - Tel : 07 88 50 28 21
        - Adresse : 17 Boulevard de la République, La Grenne Colombes, France
""")

