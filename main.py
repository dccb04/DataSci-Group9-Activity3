import streamlit as st

#git add .
#git commit  -m ""
#git push
#git pull  - to make it up to date

# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt

#To read the csv file
df = pd.read_csv("/datasets/out.csv")
st.dataframe(df)


