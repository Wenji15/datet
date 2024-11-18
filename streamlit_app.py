import streamlit as st
# from chardet import detect
import json

def read_json(file_path):
    # try:
    with open(file_path, 'rb') as file:
        file_content = file.read()
        data = json.loads(content)
        return data

st.set_page_config(page_title="数据后处理过程演示", layout="wide")
config_file_path = st.text_input('输入配置文件路径', help='json', )
if st.button("读取配置文件"):
    json_file = read_json(config_file_path)
    st.write(json_file)
