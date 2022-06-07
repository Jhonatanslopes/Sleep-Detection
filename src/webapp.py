import streamlit as st
from detector import detection


# main function
def main():

    st.image('src/img/driver3.jpg')
    st.markdown('''
        <h2 align="center">
            Detecção de Fadiga
        </h2>
    ''', unsafe_allow_html=True)
    st.write('_' * 10)

    st.markdown('''
        <p align="center">
            <b>Olá, Sr. motorista/transportador...</b>
        </p>
    ''', unsafe_allow_html=True)
    st.write('')


    st.markdown('''
        <p align="center">
            seja bem vindo ao WebApp de detecção de Fadiga para motoristas que realizam viagens longas, geralmente, motoristas que realizam viagens logísticas levando cargas entre estados/cidades etc.
        </p>
    ''', unsafe_allow_html=True)

    st.markdown('''
        <p align="center">
            Ajudamos a evitar acidentes em estradas detectando se no meio de alguma viagem/trajeto o motorista que consuzirá o veículo terá algum momento de fadiga ou pegarará no sono no
            volante.
        </p>
    ''', unsafe_allow_html=True)

    st.write('')
    st.write('')

    st.markdown('''
        <h4 align="center">
            Como usar:
        </h4>
    ''', unsafe_allow_html=True)

    st.info('''
        1. Coloque o celular em um suporte apropriado.
        2. Confirme se a camera pega os olhos e o rosto do condutor.
        3. Quando tudo pronto, pressione o botão "iniciar" logo abaixo.
        4. Para desligar o vídeo, pressione o "q".
    ''')

    st.write('')
    st.write('')
    st.write('_' * 10)
    button_detection = st.button('Iniciar detecção de fadiga')

    if button_detection:
        detection()


if __name__ == '__main__':
    main()