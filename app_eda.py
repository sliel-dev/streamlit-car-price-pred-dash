import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda():
    # 데이터를 불러오기
    df = pd.read_csv('./data/Car_Purchasing_Data.csv')

    # 데이터 보여주기
    st.info('이 데이터는 Car_Purchasing_Data.csv 데이터입니다.')
    radio_menu = ['데이터프레임', '기본통계']
    radio_choice = st.radio('선택하세요', radio_menu)
    if radio_choice == radio_menu[0]:
        st.dataframe(df)
    elif radio_choice == radio_menu[1]:
        st.dataframe(df.describe())
    st.subheader('최대 / 최소값 확인')
    min_max_menu = df.columns[4:]
    select_col = st.selectbox('컬럼을 선택하세요', min_max_menu)
    st.info(f'{select_col}는 {int(df[select_col].min())} 부터 {int(df[select_col].max())} 까지입니다.')

    st.subheader('상관관계분석')
    multi_menu = df.columns[4:]
    select_menu_list = st.multiselect('컬럼을 2개 이상 선택하세요', multi_menu)
    
    if len(select_menu_list) <= 1 :
        pass
    else:
        st.dataframe(df[select_menu_list].corr(numeric_only=True))
        fig1 = plt.figure()
        sb.heatmap(data=df[select_menu_list].corr(numeric_only=True), vmin=-1, vmax=1, annot=True, cmap='coolwarm', linewidths=0.8, fmt='.2f')
        st.pyplot(fig1)
        st.info('각 컬럼간의 Pair Plot 입니다.')
        pair = sb.pairplot(data=df, vars=select_menu_list)
        st.pyplot(pair)
    