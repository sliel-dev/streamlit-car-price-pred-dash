import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda():
    st.markdown("""
        <h2 style='color: #1E88E5; text-align: center; margin-bottom: 2rem;'>
            📊 데이터 분석 대시보드
        </h2>
    """, unsafe_allow_html=True)

    # 데이터를 불러오기
    df = pd.read_csv('./data/Car_Purchasing_Data.csv')

    # 데이터 선택 섹션
    st.markdown("""
        <div class='custom-card'>
            <h4 class='custom-title' style='margin-top: 0; font-size: 1.5rem;'>
                📈 데이터 뷰어
            </h4>
            <p class='custom-text'>원하는 데이터 보기 방식을 선택하세요.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
            <div class='custom-card' style='height: 300px; display: flex; flex-direction: column; justify-content: center;'>
        """, unsafe_allow_html=True)
        radio_menu = ['데이터프레임', '기본통계', '요약 정보']
        radio_choice = st.radio('데이터 보기 방식', radio_menu)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        if radio_choice == radio_menu[0]:
            st.dataframe(
                df.style.background_gradient(cmap='Blues', subset=['Age', 'Annual Salary', 'Net Worth'])
                .format({'Annual Salary': '${:,.0f}', 'Net Worth': '${:,.0f}', 'Car Purchase Amount': '${:,.0f}'}),
                height=300
            )
        elif radio_choice == radio_menu[1]:
            st.dataframe(
                df.describe().style.background_gradient(cmap='Oranges', axis=1)
                .format('{:,.2f}'),
                height=300
            )
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("데이터 수", f"{len(df):,}건")
            with col2:
                st.metric("평균 구매가", f"${df['Car Purchase Amount'].mean():,.0f}")
            with col3:
                st.metric("평균 연봉", f"${df['Annual Salary'].mean():,.0f}")
        st.markdown("</div>", unsafe_allow_html=True)

    # 최대/최소값 섹션
    st.markdown("""
        <div style='background-color: #f3e5f5; padding: 20px; border-radius: 10px; margin: 2rem 0;'>
            <h4 style='color: #7b1fa2; margin-top: 0;'>🔍 변수별 범위 확인</h4>
        </div>
    """, unsafe_allow_html=True)

    min_max_menu = df.columns[4:]
    select_col = st.selectbox('분석할 변수를 선택하세요', min_max_menu)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("최소값", f"{int(df[select_col].min()):,}")
    with col2:
        st.metric("최대값", f"{int(df[select_col].max()):,}")

    # 상관관계 분석 섹션
    st.markdown("""
        <div style='background-color: #fff3e0; padding: 20px; border-radius: 10px; margin: 2rem 0;'>
            <h4 style='color: #e65100; margin-top: 0;'>🔗 상관관계 분석</h4>
            <p>변수들 간의 관계를 시각화하여 확인해보세요.</p>
        </div>
    """, unsafe_allow_html=True)

    multi_menu = df.columns[4:]
    select_menu_list = st.multiselect('분석할 변수들을 선택하세요 (2개 이상)', multi_menu)
    
    if len(select_menu_list) > 1:
        # 상관관계 행렬
        st.markdown("#### 상관계수 행렬")
        st.dataframe(df[select_menu_list].corr(numeric_only=True).style.background_gradient(cmap='coolwarm'))
        
        # 히트맵
        fig1 = plt.figure(figsize=(10, 6))
        sb.heatmap(data=df[select_menu_list].corr(numeric_only=True), 
                  vmin=-1, vmax=1, 
                  annot=True, 
                  cmap='coolwarm', 
                  linewidths=0.8, 
                  fmt='.2f')
        plt.title('상관관계 히트맵', pad=20)
        st.pyplot(fig1)

        # Pair Plot
        st.markdown("#### 변수간 산점도 매트릭스")
        with st.spinner('그래프를 생성하는 중입니다...'):
            pair = sb.pairplot(data=df, 
                             vars=select_menu_list,
                             diag_kind='kde',
                             plot_kws={'alpha': 0.6})
            st.pyplot(pair)
    