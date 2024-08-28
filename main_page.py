import streamlit as st
import uuid


# Estilo da página
st.sidebar.markdown("main page") 

st.markdown(
    """
    <h1 style='color: #034001; font-size: 70px;'>Home page</h1>
    """, 
    unsafe_allow_html=True
)

# URL do outro aplicativo do Streamlit
other_app_url = "http://localhost:8501/cria_fabrico_heineken"  # Substitua pelo URL do outro app

#import streamlit as st

# Criar um botão usando HTML e CSS
st.markdown(f'''
    <a href="{other_app_url}" target="_blank">
        <button style="background-color:#4CAF50; color:white; padding:15px 32px; text-align:center;
        text-decoration:none; display:inline-block; font-size:16px; border:none; border-radius:5px;">
            Fabrico
        </button>
    </a>
    ''', unsafe_allow_html=True)


from streamlit_drawable_canvas import st_canvas

# Configurações do canvas
st.write("Por favor, assine abaixo:")

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Cor de preenchimento
    stroke_width=2,                       # Espessura da linha
    stroke_color="#000000",               # Cor da linha
    background_color="#ffffff",           # Cor de fundo
    update_streamlit=True,
    height=150,                           # Altura do canvas
    width=400,                            # Largura do canvas
    drawing_mode="freedraw",              # Modo de desenho
    key="canvas",
)

# Salva a assinatura quando o botão for clicado
if st.button("Salvar assinatura"):
    if canvas_result.image_data is not None:
        st.image(canvas_result.image_data, caption="Sua assinatura")
        # Você pode salvar a imagem usando o OpenCV ou PIL, se necessário
    else:
        st.error("Por favor, assine antes de salvar.")

