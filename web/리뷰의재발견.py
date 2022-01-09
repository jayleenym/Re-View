import streamlit as st
import pandas as pd
from PIL import Image
from models import *

global DATA_URL
global DATA
global PRODUCT_NAME

DATA_URL = "./"

@st.cache()
def load_data():
    data = pd.read_csv("./labeling_합본.csv")
    data = data[data['표준편차'] < 1][['평균', '상품명', '리뷰']]
    return data

DATA = load_data()
PRODUCT_NAME = DATA['상품명'].unique()

def main():
    st.title("✍🏻리뷰의 재발견")
    st.subheader("안녕하세요, 🧠무뇌형 인간🧠입니다")
    
        
         
    st.write(DATA)

    # if selected_box == '상품 보기': product()
        
    
if __name__ == "__main__":
    main()