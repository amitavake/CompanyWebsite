import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("The Best Company")

content1 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc bibendum nunc in elit fringilla vehicula. Vestibulum bibendum sodales libero. Curabitur et eros ante. Phasellus vel laoreet nibh. Vivamus finibus sagittis molestie. Sed sodales auctor mattis. Vestibulum nulla enim, facilisis sed ante sed, euismod pretium diam. Donec vel eros augue. Quisque feugiat mi sed dolor tempus, et scelerisque lectus blandit. Suspendisse finibus auctor sapien, ac pretium eros egestas eu. Mauris ultrices risus et eros commodo pulvinar. Curabitur varius quis nunc gravida interdum. Phasellus in aliquet ante. Maecenas vel ligula a lacus pellentesque malesuada. Sed semper varius tellus, in semper leo congue et.
"""
st.write(content1)

st.subheader("Our Team")

df = pd.read_csv("data.csv")
col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.header(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])


with col2:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        st.header(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])

# content2 = """
# "Below you can find some of the apps I have built in Python. Feel free to contact me."
# """
# st.write(content2)
#
# df = pd.read_csv("data.csv", sep=";")
#
# col3, col4 = st.columns(2)
# with col3:
#     for index, row in df[:10].iterrows():
#         st.header(row["title"])
#         st.write(row["description"])
#         st.image("images/" + row["image"])
#         st.write(f"['Source code']({row['url']})")
# with col4:
#     for row in df[10:].iterrows():
#         st.header(row["title"])
#         st.write(row["description"])
#         st.image("images/" + row["image"])
#         st.write(f"['Source code']({row['url']})")




# if __name__ == '__main__':
#     print_hi('Hi there!')


