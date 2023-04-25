import  streamlit as st
import subprocess

command = subprocess.run(['pip', 'list'] , capture_output=True, text=True)
st.write(command)

command = subprocess.run(['hostnamectl'] , capture_output=True, text=True)
st.write(command)


st.title("sentence_transformers")

         
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

#Our sentences we like to encode
sentences = ['This framework generates embeddings for each input sentence',
    'Sentences are passed as a list of string.', 
    'The quick brown fox jumps over the lazy dog.']

#Sentences are encoded by calling model.encode()
sentence_embeddings = model.encode(sentences)

#Print the embeddings
for sentence, embedding in zip(sentences, sentence_embeddings):
    st.write("Sentence:", sentence)
    st.write("Embedding:", embedding)
    st.write("")
