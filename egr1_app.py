import streamlit as st
import io

def main():
    
    st.markdown("# ZENK PROJECT")
    st.markdown("*Bioinformática, RPA (robotic process automation), Scraping, Análise de Dados, Estatística*")
    
    st.markdown("""---""")
    col1, col2, col3 = st.columns([15,1,1])
    with col1:
        st.markdown("Abraão Andrade — 28 Dez 2022 — 1 min leitura")
    with col2:
        st.markdown("[![Title](https://img.icons8.com/ios-glyphs/30/null/github.png)](https://github.com/AbraaoAndrade/b2b_prospection)")
    with col3:
        st.markdown("[![Title](https://img.icons8.com/ios-glyphs/30/null/linkedin-circled--v1.png)](https://linkedin.com/in/abraão-andrade-3632031b0)")
    

    
    f = io.open('data/textos.txt', mode="r", encoding="utf-8")
    resumo = f.read()

    st.warning('Prêmio de Trabalho Destaque de Iniciação Científica 2022', icon="🏆")
    st.warning('Colaboração em Publicação Internacional - [Acesse](https://doi.org/10.1016/j.celrep.2022.111152)', icon="📄")
    with st.expander(""):
        st.image("images/cellreports_title.jpg")

    st.markdown("## Contextualização")
    st.video("https://www.youtube.com/watch?v=7RhojlXYPEA")
    with st.expander("Introdução"):
        
        st.markdown(resumo)
    # file_ = open("D:\PYTHON\Streamlit-Course\data\jaspar_2.gif", "rb")
    # contents = file_.read()
    # data_url = base64.b64encode(contents).decode("utf-8")
    # file_.close()
    # st.markdown(
    #     f'<img src="data:image/gif;base64,{data_url}" alt="cat gif" width="600" />',
    #     unsafe_allow_html=True,
    # )


    _left, _right = st.columns(2)
    video_file = open("images/transfac.mp4", "rb").read()
    with _left:
        st.video(video_file, start_time=1)

    video_file = open("images/jaspar.mp4", "rb").read()
    with _left:
        st.video(video_file, start_time=1)

    video_file = open("images/fimo.mp4", "rb").read()
    with _left:
        st.video(video_file, start_time=1)

if __name__ == '__main__':
    main()