import streamlit as st

st.set_page_config(page_title="数据后处理过程演示", layout="wide")
config_file_path = st.text_input('输入配置文件路径', help='json', )
if st.button("读取配置文件"):
    st.write(config_file_path)
