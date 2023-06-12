import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def main():
    st.title("Selamat Datang")
    st.subheader("Aplikasi Statistik")
    
    lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_boxe3lx3.json")
    lottie_animasi=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_riAqnQrYxZ.json")

    st_lottie(lottie_hello, key="Hello")
    st_lottie(lottie_animasi, key="Animasi")

def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
    
def load_lottieurl(url:str):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

if __name__ == '__main__':
    main()
