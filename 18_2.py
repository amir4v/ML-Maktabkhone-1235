import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn


"""
st.code('This is st.code...')
st.text('this is text')
st.markdown('# this is markdown')
st.title('this title')
st.header('this is header')
st.subheader('this is subheader')
st.latex(r'''a+x r^B stg''')
st.write('this is write')

df = pd.read_csv('./Iris.csv')
st.dataframe(df)
st.table(df)

from PIL import Image
photo = Image.open('./18.png')
st.image(photo)

st.button('click')
st.checkbox('checkbox')
st.radio('radio', [1,2,3])
st.selectbox('selectbox', [1,2,3])
st.multiselect('multipleselect', [1,23,4,5,6,7])
st.slider('slider', min_value=10, max_value=100)
st.select_slider('select slider', ['A', 'sdsd', 234])
st.text_input('text input')
st.text_area('text area')

date = st.date_input('date')
print(date)

st.file_uploader('file')
st.color_picker('color picker')
"""

import time
my_bar = st.progress(0)
for percent in range(0, 101):
    time.sleep(0.01)
    my_bar.progress(percent)
st.spinner()

st.balloons()
st.error('error')
st.warning('warn')
st.info('info')
st.success('success')

fig = plt.figure(figsize=(12, 5))
st.pyplot(fig)
