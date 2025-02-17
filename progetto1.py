import streamlit as st

add_sidebar = st.sidebar.selectbox('Menu', ('Home','Calcolatore previsione', 'I nostri risultati'))

if add_sidebar=='Home':
    from PIL import Image
    logo_insubria = Image.open("Logoinsubria.png")
    logo_manfredini = Image.open("Logo_Manfredini.png")

    #col1 e col2 servono per mettere le immagini affiancate, se volete metterle sovrapposte invece non c'è bisogno di usare col1 e col2
    # Intestazione
    col1, col2 = st.columns(2)
    with col1:
        st.image(logo_insubria, width=150)
    with col2:
        st.image(logo_manfredini, width=150)

    st.title('Benvenuto nel nostro sito!')
    st.write('Questo sito prevedrà la tua spesa totale in base ai dati che inserirai.')
    st.title('Chi siamo noi?')
    st.write('Noi siamo un gruppo di ragazzi che lavorando sui dati ISTAT ed imparando a programmare hanno creato un sito dove era possibile calcolare la vostra spesa totale inserendo le vostre variabili.')

if add_sidebar== 'Calcolatore previsione':

    intercetta= -229.72625155569813
    c_fam_decile_red_eq= 101.248
    c_crisis= -88.329
    c_spesa_01= 2.202
    c_spesa_04= 1.342
    st.header("Calcolatore previsione")
    fam_decile_red_eq= st.number_input("Inserisci il tuo decile reddito equivalente:", value=0.0)
    crisis = st.number_input("Inserisci il tuo anno:", value=0.0)
    spesa_01 = st.number_input("Inserisci la tua spesa 01:", value=0.0)
    spesa_04 = st.number_input("Inserisci la tua spesa 04:", value=0.0)
    if st.button("Fai una previsione"):
       spesa_tot = intercetta + c_fam_decile_red_eq*fam_decile_red_eq + c_crisis*crisis + c_spesa_01*spesa_01 + c_spesa_04*spesa_04
       st.success(f"La spesa totale è:{spesa_tot}")



if add_sidebar=='I nostri risultati':

    intercetta= -229.72625155569813
    c_fam_decile_red_eq= 101.248
    c_crisis= -88.329
    c_spesa_01= 2.202
    c_spesa_04= 1.342
    st.header("Le nostre previsioni")
    fam_decile_red_eq= st.number_input("Inserisci il tuo  decile reddito equivalente:", value= 101.248)
    crisis = st.number_input("Inserisci il tuo anno:", value= -88.329)
    spesa_01 = st.number_input("Inserisci la tua spesa 01:", value= 2.202)
    spesa_04 = st.number_input("Inserisci la tua spesa 04:", value= 1.342)
    if st.button("Fai una previsione"):
      spesa_tot = intercetta + c_fam_decile_red_eq + c_crisis + c_spesa_01 + c_spesa_04
      st.success(f"La nostra spesa totale è:{spesa_tot}")

