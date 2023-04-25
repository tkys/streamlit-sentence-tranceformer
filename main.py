import  streamlit as st
import subprocess

st.write("hoge")
st.write(subprocess.run('pip', 'list', capture_output=True, text=True))
