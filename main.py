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
df = pd.read_csv("datasets/out.csv")
#st.dataframe(df)

urlLegitimacy = df.groupby(['starts_with_ip', 'label']).size().unstack()
urlLegitimacy

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



