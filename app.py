import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Customer Segmentation Dashboard")

rfm = pd.read_csv("rfm_output.csv")

segment_filter = st.selectbox("Select Segment", rfm["segment"].unique())

filtered = rfm[rfm["segment"] == segment_filter]

st.write("Number of Customers:", len(filtered))
st.dataframe(filtered.head(20))

fig, ax = plt.subplots()
sns.histplot(filtered["monetary"], bins=20, ax=ax)
st.pyplot(fig)
