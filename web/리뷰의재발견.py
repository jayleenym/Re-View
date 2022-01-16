from itertools import product
from pickletools import float8
from turtle import width
import streamlit as st
import pandas as pd
from PIL import Image
import pickle
import os
import re
from wordcloud import WordCloud
from konlpy.tag import Mecab
from collections import Counter

from models import *

global DATA_URL
global DATA
global PRODUCT_NAME

DATA_URL = "./"

@st.cache()
def load_data():
    data = pd.read_csv(DATA_URL+"labeling_합본.csv")
    data = data[data['표준편차'] < 1][['평균', '상품명', '리뷰']]
    data['상품명'] = data['상품명'].apply(lambda x: re.sub(" ", " ", x))
    data['평균'] = data['평균'].apply(lambda x: round(x, 1))
    return data

DATA = load_data()
PRODUCT_NAME = DATA['상품명'].unique()


def home_page():
    global next
    st.title("✍🏻리뷰의 재발견")
    # st.subheader("안녕하세요, 🧠무뇌형 인간🧠입니다")
    st.markdown("""
    #### 팀원 소개
문예진 | 이상민 | 정수연 | 정승연 | 황의린


#### Review? Re-View!""")
    c1, c2 = st.columns([1, 5])
    with c1: pass
    with c2: st.image("../images/home1.png", caption = '출처: 올리브영', width = 500)
    st.markdown("""
###### 물건 살 때 여러분이 보는 그 리뷰의 **⭐️유용성⭐️**, 저희가 알려드립니다! 

📌 리뷰 유용성 판단부터   
📌 토픽으로 알아보는 리뷰 유용성 결정 요인 분석  
📌 군집화를 통한 대표 리뷰 추출까지

*우리 같이 Review를 Re-View해봐요♥️*
 """)
    _, c2 = st.columns([16, 1])
    with c2: next = st.button('Next')


def product_page():
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

    df = DATA[DATA['상품명'] == PRODUCT_NAME[0]][['리뷰', '평균']]
    st.markdown("#### 유용성 결정 요인")
    mecab = Mecab()
    word = mecab.nouns(df['리뷰'].sum().replace("것", " ").replace("사용", " ").replace('거', " ").replace('제품', " "))
    counts = Counter(word).most_common(50)
    wc = WordCloud(font_path = '/Library/Fonts/applegothic.ttf', background_color = 'white')
    cloud = wc.generate_from_frequencies(dict(counts))
    # st.write((type(cloud)))
    cloud.to_file('../images/wc.png')
    st.image('../images/wc.png')

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
        

def one_product(i):
    st.title(PRODUCT_NAME[i])
    # 새로운 리뷰 평가
    st.subheader("리뷰 유용성 평가")
    review = st.text_input("새로운 리뷰를 입력하세요.")
    review = '너무 좋아요 저 건성인데 이거 쓰니까 괜찮았어요'
    _, c2 = st.columns([6, 1])
    with c2:
        rv_btn = st.button('평가하기')
    
    if rv_btn:
        st.write("{'useful' : 0.99, 'useless' : 0.01}")
        st.write("99%의 확률로 유용한 리뷰입니다.")

    st.markdown('----')
    c1, c2 = st.columns(2)
    # 유용성 판단
    with c1:
        st.markdown('#### 리뷰 필터링')
        btn = st.button('유용한 순')
        df = DATA[DATA['상품명'] == PRODUCT_NAME[i]][['리뷰', '평균']]
        df['유용성'] = (df['평균'] / 5 * 100).astype('str') + '%'
        if btn : 
            # st.write(df.sort_values(by = '유용성'))
            # st.write(df)
            st.dataframe(df.sort_values(by = '평균', ascending=False)[['리뷰', '유용성']])
        else:
            st.dataframe(df[['리뷰', '유용성']])
            # st.set_option('wideMode', True)
            # st.write(df)
    
    # with c2:
        # (임시) WordCloud
        

    # 군집화 결과
    st.markdown('#### 군집화 결과')
    cluster = st.radio('분류된 군집을 선택하세요', ('A : 패드, 좁쌀, 수분', 
                                              'B : 끈적, 건성, 흡수', 
                                              'C : 따가움, 염증, 피부'))
    if cluster == 'A : 패드, 좁쌀, 수분':
        st.dataframe(df[df['평균'].astype('float') >= 3]['리뷰'].head(5))
    else:
        pass


    
if __name__ == "__main__":
    # home_page()
    my_button = st.sidebar.selectbox('Page Navigation', ("Home", "상품 목록"))
    # # print(next)
    # if my_button == "Home":
    #     home_page()
    #     if next : 
    #         product_page()
    #         next = False
    # elif my_button == '상품 목록':
    #     next = False
    product_page()
    # one_product(0)
