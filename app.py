import streamlit as st

st.set_page_config(page_title="YouTube Sentiment Analysis", page_icon="🎬")

st.title("🎬 YouTube Comment Sentiment Analysis")

st.markdown("""

## 📌 **Project Introduction**

**Welcome to the YouTube Comment Sentiment Classifier App!** ✨

This project is an end-to-end machine learning pipeline that:

🎯 Extracts real-world YouTube comments using the **YouTube Data API v3**

🧹 Cleans and preprocesses the comment data

🧠 Trains a **Logistic Regression** model using **TF-IDF Vectorization**

🎯 Predicts Sentiment as **Positive, Negative, or Neutral**

🚀 Built with **Python** and **Streamlit**



---

### 👨‍💻 **Project by:**

**Srikanth Gunti**

A Postgraduate Data Science Student

Nizam College, Osmania University


---

""")

if st.button("Next"):
    st.switch_page("pages/1_Data_Overview.py")