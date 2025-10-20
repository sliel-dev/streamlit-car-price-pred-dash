import streamlit as st
from app_eda import run_eda
from app_home import run_home
from app_ml import run_ml

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Car Price Prediction App",
        page_icon="🚗",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS with dark/light mode support
    st.markdown("""
        <style>
        /* Global Styles */
        .main {
            padding: 2rem;
        }
        
        /* Input Fields */
        .stTextInput>div>div>input, 
        .stNumberInput>div>div>input,
        .stSelectbox>div>div>div {
            border-radius: 10px;
        }
        
        /* Buttons */
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            padding: 0.5rem 1rem;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        /* Dark mode styles */
        @media (prefers-color-scheme: dark) {
            .stButton>button {
                background-color: #4A4A4A;
                color: white;
                border: 1px solid #666;
            }
            .stButton>button:hover {
                background-color: #666;
            }
            .custom-card {
                background-color: #2C2C2C !important;
                border: 1px solid #404040;
            }
            .custom-title {
                color: #E0E0E0 !important;
            }
            .custom-text {
                color: #CCCCCC !important;
            }
            .metric-card {
                background-color: #363636 !important;
                border: 1px solid #404040;
            }
        }
        
        /* Light mode styles */
        @media (prefers-color-scheme: light) {
            .stButton>button {
                background-color: #ff4b4b;
                color: white;
                border: none;
            }
            .stButton>button:hover {
                background-color: #ff6b6b;
            }
            .custom-card {
                background-color: #FFFFFF !important;
                border: 1px solid #E0E0E0;
            }
            .custom-title {
                color: #1E88E5 !important;
            }
            .custom-text {
                color: #424242 !important;
            }
            .metric-card {
                background-color: #F5F5F5 !important;
                border: 1px solid #E0E0E0;
            }
        }
        
        /* Shared Card Styles */
        .custom-card {
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Data viewer styles */
        .dataframe {
            border-radius: 10px !important;
            overflow: hidden;
            border: none !important;
        }
        .dataframe th {
            background-color: #1E88E5 !important;
            color: white !important;
            font-weight: 500;
        }
        .dataframe td {
            text-align: right;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.image('./image/car_preview.jpg', width=200)
        st.title('🚗 내비게이션')
        menu = ['홈', '데이터 분석', '가격 예측']
        choice = st.selectbox('메뉴 선택', menu)

    # Main content
    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()

if __name__ == '__main__':
    main()
