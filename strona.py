from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Oficjalna Strona Serwera", page_icon=":tada:",layout="wide" )

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#---Assety---
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json")
img_krowa_mu = Image.open("Obrazy/krowa_mu.png")
img_xHUSAIR = Image.open("Obrazy/xHUSAIR.png")
img_mapa1 = Image.open("Obrazy/mapa1.jpg")
img_Discord = Image.open("Obrazy/Discord.jpg")
#---Naglowek---

st.subheader("Witamy :wave:")
st.title("Oficjalna storna naszego serwera.")
st.write("Storna zawiera zasady serwer oraz informację o nim oraz o administratorach")

#---Zasady---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Zasady Serwera")
        st.write("##")
        st.write("Oficjalne Zasady Serwera" \
        "Każdy gracz musi przestrzegać poniższych zasady podzielonych na kategorie:")
        st.subheader("Ogólne:")
        st.write("•	Każdy gracz musi przestrzegać poleceń administracji (**)")
        st.write("•	Obowiązuje zakaz wszystkich zewnętrznych : programów ( x-ray, killaura, wallchack, fly itd.),paczek zasobów( np. x-ray ultimate) oraz launcherów( np. meteor client) (***)")
        st.write("•	Obowiązuje zakaz kradzieży – kradzież nie jest równa pożyczaniu rzeczy. Jeśli ktoś zabierze komuś coś o mniejszej albo nieznacznej wartości np. 5 cobbela nie jest to poważna rzecz i nie jest to kradzież, ludzie ten serwer jest dla zabawy dajcie się bawić innym.  (**)")
        st.write("•	Obowiązuje zakaz rozpowszechniania i propagowania ideologii: nazistowskiej, neonazistowskiej, komunistycznej oraz wszelkich poglądów politycznych. ( *-***) ")
        st.subheader("Kosmetyczne:")
        st.write("•	Należy łatać dziury po creeparach (*)")
        st.write("•	Prosimy o budowanie budynków, które są przyjemne dla oka (przynajmniej względnie) bądź służą serwerowi. Wszystko co będzie wbrew tej zasadzie zostanie usunięte. ")
        st.write("•	Obowiązuje zakaz stawiania mobgrinderów. Wyjątek – Kacper i jego mobgrinder. Sprzeciw = usunięcie oraz *")
        st.subheader("Kulturalne:")
        st.write("•	Nie można przeklinać i być wulgarnym na chacie. (* :*:)")
        st.write("•	Należy być miłym (:*:)")
        st.write("•	Bullying( zabijanie gracza ponad miarę/ gnębienie gracza) jest zakazane. (***)")
        st.write("•	MOŻNA się zabijać lub walczyć")
        #---Kary---
        st.header("Kary:")
        st.write("*= Ban na 4 godziny")
        st.write("**= Ban na 1")
        st.write("***= Ban na 3 dni")
        st.write(":*:= Timeout na czas zależny od admina")
        st.write("‘*’= Ban na czas ustalony przez admina ( może być stosowany dla wszystkich zasad jeśli zostały znacznie przekroczone i żadna kara nie jest adekwatna do przewinienia)")
        st.subheader("Jako kary mogą być stosowane:")
        st.write("-odbieranie itemów ( kradzieże)")
        st.write("-zabijanie ( bullying)")
        st.write("-timeouty na dowolną ilość czasu (wszystkie przewinienia)")
        st.write("Jeśli gracz sam przyjdzie do administratora i przyzna się do oszukiwania jego kara powinna zostać drastycznie zmniejszona. Jeśli przypadek będzie się powtarzać kara powinna być taka jaka przewidziana jest w regulaminie")
        st.header("Do wszystkich!")
        st.subheader("Do graczy:")
        st.write("Prosimy o wyrozumiałość dla innych. Nie bądźcie szczegółowi, nie skazujcie każdego na karę jeśli jest taka możliwość dogadajcie się między sobą.")
        st.subheader("Do administacji:")
        st.write("Proszę o wyrozumiałość, uczciwość i przebaczenie w stosunku do graczy.")
        st.subheader("Zasady pojawiły się trochę późno, ale mam nadzieję, że będą dobrze działać! Miłej gry !")
        
    with right_column:
         st_lottie(lottie_coding, height= 400, key="coding")
         st.header("Administratorzy:")
         st.subheader("krowa_mu")
         st.image(img_krowa_mu)
         st.write("Właściciel i zarządca od spraw in-gameowych serwera.")
         st.subheader("xHUSARIA")
         st.image(img_xHUSAIR)
         st.write("Właściciel i zarządca od spraw technicznych serwera.")
#--- Mapa i inne---
with st.container():
    st.write("---")
    st.header("Mapa!")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with text_column:
        st.subheader("Obserwuj rozwój serwera na interaktywnej mapie!")
        st.write("" 
        "Mapa aktualizuje się raz dzinnie. Można spokojnie obserwować pracę swoje oraz innych graczy i cieszyć się postępami " \
        "całego serwera w każdej chwili, bez koniecznośći wchodzenia do Minecrafta!")
        st.markdown("[MAPA TUTAJ!](http://s1141863.csrv.pl/map)")
    with image_column:
        st.image(img_mapa1)
with st.container():
    st.write("---")
    st.header("Nasz Discord!")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_Discord)
    with text_column:
        st.subheader(" Serdecznie zapraszamy!!!")
        st.write("Na naszym discordzie można uzyskać wsparcie od administratorów, zgłosić błędy serwera oraz inne problemy. Można również miło spędzić czas z innymi graczami!")
        st.markdown("[DISCORD](https://discord.gg/gFpYHEnm)")


    