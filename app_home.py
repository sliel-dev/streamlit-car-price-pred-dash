import streamlit as st

def run_home():
    # Title with custom styling
    st.markdown("""
        <h1 style='text-align: center; color: #1E88E5; margin-bottom: 2rem;'>
            🚗 자동차 구매 금액 예측 시스템
        </h1>
    """, unsafe_allow_html=True)
    
    # Two-column layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
            <div class='custom-card'>
                <h2 class='custom-title'>주요 기능</h2>
                <ul style='list-style-type: none; padding: 0;' class='custom-text'>
                    <li style='margin: 10px 0;'>📊 데이터 분석 기능</li>
                    <li style='margin: 10px 0;'>💰 구매 금액 예측</li>
                    <li style='margin: 10px 0;'>📈 상관관계 분석</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class='custom-card'>
                <h3 class='custom-title'>데이터 소스</h3>
                <p class='custom-text'>Kaggle의 Car Purchasing Dataset을 활용하여 분석 및 예측을 수행합니다.</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image('./image/car_preview.jpg', use_container_width=True)
        
    # Info box at the bottom
    st.markdown("""
        <div class='custom-card'>
            <h3 class='custom-title'>💡 시작하기</h3>
            <p class='custom-text'>왼쪽 사이드바에서 원하는 메뉴를 선택하여 시작하세요:</p>
            <ul class='custom-text'>
                <li><strong>데이터 분석:</strong> 차량 데이터의 통계와 시각화를 확인할 수 있습니다.</li>
                <li><strong>가격 예측:</strong> 고객 정보를 입력하여 예상 구매 금액을 예측해볼 수 있습니다.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)