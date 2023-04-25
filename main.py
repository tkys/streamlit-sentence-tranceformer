import  streamlit as st
import subprocess


pip_list = subprocess.run(['pip', 'list'] , capture_output=True, text=True)
st.write(pip_list)
