# Importing libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import streamlit as st
import seaborn as sns 
import plotly.express as px 

st.write("Hello, Streamlit World!")

# Displaying Text
st.text("Text")
st.write("Super Function")
st.header("Header")
st.subheader("Sub-Header")
st.title("Title")
st.markdown("***Markdown***")
st.code("print('Hello, World!')",language='python')



# Displaying Interactive widgets
btn = st.button("Submit")
# st.write(btn)
if btn:
    st.info("Info")

option = st.radio("Select",['A','B','C'])

if option == 'A':
    st.warning("Warning! 😑")
elif option=='B':
    st.error("Error! 🤯")
elif option == 'C':
    st.success("Success 🤩")     

chk = st.checkbox("I agree")
if chk :
    st.info("Agreement Accepted! :white_check_mark:")

option1 = st.selectbox("Select",['A','B','C'])    
if option1 == 'A':
    st.warning("Warning! 😐")
elif option1 =='B':
    st.error("Error! ❌")
elif option1 == 'C':
    st.success("Success ✅")  


choice = st.selectbox("قيم تجربتك:", ["ممتاز 🤩", "جيد 🙂", "سيء 😕"])

st.write(f"لقد اخترت: {choice}")  



if st.button("اضغط هنا للمفاجأة 🎉"):
    st.balloons() # حركة بالونات رائعة في Streamlit
    st.success("تهانينا! لقد نجحت الطريقة 😍")

age = st.slider("Select",0,100) 
st.select_slider("Select",['A','B','C'])
st.text_input("Enter a Text")
st.text_area("Enter a Paragraph")
st.file_uploader("Upload")
st.camera_input("Take a Photo")
st.date_input("Today")
st.time_input("Now")
st.number_input("numbers")
st.multiselect("Select",['A','B','C'])
st.color_picker("Coloers")


# DataFrame
#loading data

try:
    df = pd.read_csv('Titanic-Dataset.csv') # تأكد أن الاسم يطابق ملفك تماماً
    st.success("تم تحميل البيانات بنجاح من الملف المحلي! ✅")
except FileNotFoundError:
    st.error("لم يتم العثور على ملف CSV في المجلد. تأكد من وجوده بجانب الكود 📁")

# الآن يمكنك الرسم باستخدام Seaborn بشكل طبيعي
if 'df' in locals():
    st.write(df.head())

# df = sns.load_dataset('titanic')
# st.write(df)
# st.dataframe(df.head())
btn1= st.button("Show Data")
if btn1:
    st.dataframe(df.sample(5))

st.table(df.head( ))

#matplotlib
st.header("Matplotlib")
st.subheader("Line Plot")
fig = plt.figure(figsize=(15,8))
plt.plot(df['Sex'],df['Survived'], c='r', lw=5,marker='^',markersize=10,ls='--')
plt.title("Sex", fontsize=20)
plt.xlabel("Sex")
plt.ylabel("Survived")
st.pyplot(fig)
 
st.text("this is a text descripting the ....")

st.subheader("Scatter plot  ")
fig = plt.figure(figsize=(15,8))
plt.scatter(df['Sex'],df['Survived'])
plt.title("Sex", fontsize=20)
plt.xlabel("Sex")
plt.ylabel("Survived")
st.pyplot(fig)

#heatmap
st.subheader("Heatmap")
corr_matrix = df.corr(numeric_only=True)
fig, ax = plt.subplots()
sns.heatmap(corr_matrix, annot=True, ax=ax, cmap='coolwarm')
st.pyplot(fig)


#plotly  #plotly.com
st.header("Plotly")

st.subheader("Scatter plot  ")
option= st.selectbox("Select an option",['Sex','Age','Survived'],key='A')
fig = px.scatter(data_frame=df,x='Survived',y='Sex',color=option)
st.plotly_chart(fig, use_container_width=True)


st.subheader("Bar Chart")
fig = px.bar(df['Sex'])
st.plotly_chart(fig, use_container_width=True)
st.subheader("Histogram")
fig=px.histogram(df['Age'])
st.plotly_chart(fig, use_container_width=True)