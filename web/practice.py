import streamlit as st
import pandas as pd
from PIL import Image

global DATA_URL
global DATA
global PRODUCT_NAME


st.title("✍🏻리뷰의 반란")

DATA_URL = "../reviews/"

@st.cache()
def load_data():
    data = pd.read_csv(DATA_URL + "0to499_labeling_합본.csv")
    data = data[data['표준편차'] < 1][['평균', '상품명', '리뷰']]
    return data

DATA = load_data()
PRODUCT_NAME = DATA['상품명'].unique()

def images():
    # 라벨링된 상품 이미지 보여주기
    st.write("유용성 평가를 할 수 있는 상품 목록입니다")
    IMAGE_PATH = "../images/"
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(Image.open("../images/라운드랩 자작나무 수분 크림 1+1.jpg"), use_column_width=True)
        st.radio("", (DATA['상품명'].unique()[0], ""))
        st.image(Image.open("../images/라운드랩 자작나무 수분 크림 1+1.jpg"), caption = PRODUCT_NAME[0])
    with col2:
        st.image(Image.open("../images/라운드랩 자작나무 수분 크림 1+1.jpg"), caption= DATA['상품명'].unique()[0])

    with col3:
        st.image(Image.open("../images/라운드랩 자작나무 수분 크림 1+1.jpg"), caption= DATA['상품명'].unique()[0])

    with col4: st.image(Image.open("../images/라운드랩 자작나무 수분 크림 1+1.jpg"), caption= DATA['상품명'].unique()[0])

def product():
    pro = st.radio("리뷰 분석이 가능한 상품 목록입니다", (PRODUCT_NAME))

    if pro == PRODUCT_NAME[0]:
       st.image(Image.open("../images/라운드랩 자작나무 수분 크림 1+1.jpg"), width = 400, caption = PRODUCT_NAME[0]) 

    




def main():
    selected_box = st.sidebar.selectbox(
    'Choose one of the following',
    ('Home', '상품 보기') 
    )

    if selected_box == "Home" :
         st.subheader("안녕하세요, 🧠무뇌형 인간🧠입니다")
        #  st.write(DATA)

    if selected_box == '상품 보기': product()
        
    
if __name__ == "__main__":
    main()