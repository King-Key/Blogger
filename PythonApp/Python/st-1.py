#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-14 10:33:03
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io


import streamlit as st
import pandas
import numpy as np
import time


# 实时进度条
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_iteration.text("iteration {i+1}")
#     bar.progress(i+1)
#     time.sleep(0.1)


# 组件
x = st.slider("x")
st.write(x, "squares is", x*x)

y = st.button("y")
st.write(y)

# 添加标题
st.title("APP")

# 直接调用
df = pandas.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
df

# 绘制地图
st.title("map")
map_data = pandas.DataFrame(np.random.randn(
    1000, 2)/[50, 50]+[37.76, -122.4], columns=["lat", "lon"])
st.map(map_data)

# 复选框
if st.checkbox('Show dataframe'):
    chart_data = pandas.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.write(chart_data)

    st.line_chart(chart_data)

# 列表选择框
option = st.sidebar.selectbox("which", df["first column"])
st.write("selected", option)
if option == 1:
    st.write("你好")

dataframe = pandas.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
st.table(dataframe)

progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(100):
    # Update progress bar.
    progress_bar.progress(i)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)

status_text.text('Done!')
st.balloons()

code = "for i in range(100)"
st.code(code, language="python")


df = pandas.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.deck_gl_chart(
    viewport={
        'latitude': 37.76,
        'longitude': -122.4,
        'zoom': 11,
        'pitch': 50,
    },
    layers=[{
            'type': 'HexagonLayer',
            'data': df,
            'radius': 200,
            'elevationScale': 4,
            'elevationRange': [0, 1000],
            'pickable': True,
            'extruded': True,
            }, {
            'type': 'ScatterplotLayer',
            'data': df,
            }])

path="/home/king-key/视频/娜娜.mp4"
vedio=open(path,"rb")
st.video(vedio.read())
