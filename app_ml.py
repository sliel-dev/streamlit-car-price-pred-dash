import streamlit as st
import joblib
import pandas as pd
from koreanize_matplotlib import koreanize
koreanize()

def run_ml():
    st.markdown("""
        <h2 style='color: #1E88E5; text-align: center; margin-bottom: 2rem;'>
            🚘 자동차 구매 금액 예측
        </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class='custom-card'>
            <h4 class='custom-title' style='margin-top: 0;'>📝 고객 정보 입력</h4>
            <p class='custom-text'>아래 정보를 입력하시면 AI가 예상 구매 금액을 분석해드립니다.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input('나이', 
                            min_value=20, 
                            max_value=90,
                            help="20세 이상 90세 이하로 입력해주세요")
        
        salary = st.number_input('연봉 ($)', 
                               min_value=10000,
                               help="연간 수입을 달러로 입력해주세요")
    
    with col2:
        card_debt = st.number_input('신용카드 부채 ($)', 
                                  min_value=0,
                                  help="현재 신용카드 부채 금액을 입력해주세요")
        
        net_worth = st.number_input('총자산 ($)', 
                                  min_value=10000, 
                                  step=100,
                                  help="부동산, 예금 등 모든 자산의 합계를 입력해주세요")

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button('💫 AI 예측 시작하기', key='predict'):
        with st.spinner('AI가 분석중입니다...'):
            regressor = joblib.load('./model/regressor.pkl')
            new_data = [{'Age': age, 'Annual Salary': salary, 
                        'Credit Card Debt': card_debt, 'Net Worth': net_worth}]
            new_data = pd.DataFrame(data=new_data)
            y_pred = regressor.predict(new_data)
            
            if y_pred < 0:
                st.error('⚠️ 입력하신 정보로는 정확한 예측이 어렵습니다. 다른 값을 입력해보세요.')
            else:
                st.markdown(f"""
                    <div class='custom-card' style='text-align: center;'>
                        <h3 class='custom-title' style='margin-top: 0;'>예측 완료! 🎉</h3>
                        <p style='font-size: 24px; margin-bottom: 0;' class='custom-text'>
                            예상 구매 금액: <strong>${format(round(y_pred[0]), ',')}</strong>
                        </p>
                    </div>
                """, unsafe_allow_html=True)