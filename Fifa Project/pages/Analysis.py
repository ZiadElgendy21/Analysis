import numpy as np
import pandas as pd
import streamlit as st

import MEDA as md

tab_1 ,tab_2 =st.tabs(['tab_1','tab_2'])
with tab_1:
    st.title('tab_1 Hello')
    st.write('parag. tab 1')
    fact=st.radio('choose fact',['overall','wage','value'],horizontal=True)

    st.plotly_chart(md.best_10_players(fact))  
    col1 ,col2 ,col3 =st.columns(3)  
    col1.metric('Temp','40 C','2 C')
    col2.metric('Temp','40 C','2 C')
    col3.metric('Temp','40 C','-2 C')
    if st.button('click me'):
        st.write('clicked')

    
    if st.checkbox('I agree'):
        st.write('congratoulation')    