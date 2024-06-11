import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門!')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.09)

'完了'

left_column, right_column = st.columns(2)
button=left_column.button('右カラムにボタンを表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# option=st.sidebar.text_input(
#     'あなたの趣味を教えてください。'
# )

# 'あなたの趣味は',option,'です。'

# condition=st.sidebar.slider(
#     'あなたの今の調子は？',0,100,50
#     )

# 'あなたの調子は',condition,'です。'


# if st.checkbox('show Image'):
#     img = Image.open('スクリーンショット 2024-05-29 132449.png')
#     st.image(img, caption='yoshitome', use_column_width=True)