import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt

#git add .
#git commit  -m ""
#git push
#git pull  - to make it up to date

# Importing libraries

##############################################################################################################################################################################################

#To read the csv file
df = pd.read_csv("datasets/out.csv")
#st.dataframe(df)

##############################################################################################################################################################################################

st.write("## 1. Legitimacy of a URL that starts with an IP.")

#To know the values when combining label and starts_with_ip data types before creating the Visual.
urlLegitimacy = df.groupby(['starts_with_ip', 'label']).size().unstack()
urlLegitimacy

##############################################################################################################################################################################################
#First graph

def bar_plot_legitimacy_basedOn_IP():
  plt.figure(figsize=(7, 7)) # define the width and height of the graph

  ax = sns.countplot(x='label', hue='starts_with_ip', data=df)
  plt.title('URL that starts with IP add. Is it Phishing or not?')

  plt.xlabel('Legitimacy of URLs (Legitimate or Phishing)')  # label for X-Axis
  plt.ylabel('Totalility of URLs')       # label for Y-Axis


  # You can use this to show the actual count of each bars
  for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')

  st.pyplot(plt)
  plt.clf()

bar_plot_legitimacy_basedOn_IP()

st.write("## Observations:")
st.write("""
- Using the bar graph, we identified that all of the Legitimate sites (1,250,000) do not contain a URL that starts with an IP address. 
- In contrast, out of the Phishing sites (1,223,282), **26,718** of them start with an IP address in their URL.
""")

##############################################################################################################################################################################################


