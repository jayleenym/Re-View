import streamlit as st
import pandas as pd
import re

DATA_URL = "./"

@st.cache()
def load_data():
    data = pd.read_csv(DATA_URL+"labeling_합본.csv")
    data = data[['평가', '상품명', '리뷰']]
    data['상품명'] = data['상품명'].apply(lambda x: re.sub(" ", " ", x))
    data['평가'] = data['평가'].apply(lambda x: round(x, 1))
    return data

DATA = load_data()
PRODUCT_NAME = DATA['상품명'].unique()

def page():
    st.title("상품 목록")
    st.markdown('''현재 분석 가능한 상품 목록입니다.  원하는 상품을 선택해주세요!''')
    # st.write(PRODUCT_NAME)

    st.subheader("리뷰 유용성 평가")
    review = st.text_input("새로운 리뷰를 입력하세요.")
    review = '너무 좋아요 저 건성인데 이거 쓰니까 괜찮았어요'
    _, c2 = st.columns([6, 1])
    with c2:
        rv_btn = st.button('평가하기')
    
    if rv_btn:
        st.write("{'useful' : 0.99, 'useless' : 0.01}")
        st.write("99%의 확률로 유용한 리뷰입니다.")

    st.markdown("#### 유용성 결정 요인")

    c1, c2, c3 = st.columns(3)
    with c1: 
        st.image("https://image.oliveyoung.co.kr/uploads/images/goods/550/10/0000/0015/A00000015329101ko.jpg?l=ko", caption = PRODUCT_NAME[0])
        st.button("선택", key = 1)

        st.image("https://image.oliveyoung.co.kr/uploads/images/goods/550/10/0000/0013/A00000013718012ko.jpg?l=ko", caption = PRODUCT_NAME[3])
        st.button('선택', key = 4)

    with c2:
        st.image("https://image.oliveyoung.co.kr/uploads/images/goods/550/10/0000/0015/A00000015525301ko.jpg?l=ko", caption = PRODUCT_NAME[1])
        st.button("선택", key = 2)
    with c3:
        st.image("https://image.oliveyoung.co.kr/uploads/images/goods/550/10/0000/0014/A00000014557912ko.jpg?l=ko", caption = PRODUCT_NAME[2])
        st.button('선택', key = 3)
