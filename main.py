import streamlit as st
import pandas

col1, col2= st.columns(2)

with col1:
    st.image("imageshai/myimage.png",width=280)

with col2:
    st.title("Meghna Mandawra")
    content="""
    Passionate About Learning:
     I'm a first-year enthusiast who loves learning 
     new things. I enjoy taking on challenges and 
     growing through them. Whether it's exploring 
     new technologies or staying updated on trends, 
     I'm always eager to expand my skills and knowledge. 
     """
    cont="Below you can find some of the apps i have built in python,Feel free to contact me."
    st.info(content)
st.write(cont)

col3,empty_col, col4= st.columns([1.5, 0.5, 1.5])

df=pandas.read_csv("data.csv", sep=";")
with col3:
    for index,row in df[:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("imageshai/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index,row in df[3:6].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("imageshai/"+row["image"])
        st.write(f"[Source Code]({row['url']})")


