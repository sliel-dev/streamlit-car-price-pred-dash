import streamlit as st
import joblib
import pandas as pd

def run_ml():
    st.subheader('구매 금액 예측하기')
    st.info('아래 정보를 입력하면 금액을 예측해드립니다.')
    # Age, Annual Salary, Credit Card Debt, Net Worth
    age = st.number_input('나이를 입력하세요', min_value=20, max_value=90)
    salary = st.number_input('연봉을 입력하세요 ($)', min_value=10000)
    card_debt = st.number_input('카드 빛을 입력하세요 ($)', min_value=0)
    net_worth = st.number_input('자산을 입력하세요 ($)', min_value=10000, step=100)
    
    if st.button('예측해보기') :
        regressor = joblib.load('./model/regressor.pkl')
        new_data = [{'Age' : age, 'Annual Salary' : salary,  'Credit Card Debt' : card_debt, 'Net Worth' : net_worth}]
        new_data = pd.DataFrame(data=new_data)
        y_pred = regressor.predict(new_data)
        if y_pred < 0 :
            st.warning('구매 금액 예측이 어렵습니다.')
        else :
            # st.info(f'예측한 금액은 {int(y_pred)}($) 입니다.')
            st.info(f"예측한 금액은 {format(round(y_pred[0]), ',')}($) 입니다.")