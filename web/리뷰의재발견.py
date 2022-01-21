# from itertools import product
# from pickletools import float8
# from turtle import home, width
import streamlit as st
# from streamlit_pages.streamlit_pages import Multipage
import pandas as pd
from PIL import Image
import pickle
import os
import re
# from wordcloud import WordCloud
# from konlpy.tag import Mecab
from collections import Counter


from multipage import MultiPage
from pages import home, models, product_page
from pages.home import *
from pages.product_page import *


app = MultiPage()

# add pages
app.add_page('Home', home.page)
app.add_page("상품목록", product_page.page)



        

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


app.run()
