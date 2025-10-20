import streamlit as st

def run_home():
    st.subheader('자동차 데이터를 분석하고, 예측하는 앱')
    st.info('데이터는 Kaggle에 있는 Car_Purchaing_data.csv 파일을 사용했습니다.')
    st.text('탐색적 데이터 분석과, 자동차 구매 예상 금액을 예측하는 앱입니다.')
    st.image('./image/car_preview.jpg', use_container_width=True)