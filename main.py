import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
from PIL import Image

#git add .
#git commit  -m ""
#git push
#git pull  - to make it up to date

# Importing libraries

#############################################################################################################################################################################################

st.title("Phishing URL Detection")
st.write("""
The fraudulent URL Detection dataset classifies URLs as legitimate or fraudulent based on a range of factors that characterize a URL's structure and content. The dataset's phishing identification relies heavily on the length of URLs, the number of unusual characters in them, and domain attributes.
""")

st.write("Dataset: [Phishing URL Detection](https://www.kaggle.com/datasets/sergioagudelo/phishing-url-detection)")

##############################################################################################################################################################################################
imageInfo = Image.open('assets/info.png')
st.image(imageInfo)

##############################################################################################################################################################################################
#Show the null values of each data types.
imageNull = Image.open('assets/nullValues.png')
st.image(imageNull)

##############################################################################################################################################################################################
#This will generate Descriptive Statistics
describe = Image.open('assets/describe.png')
st.image(describe)

##############################################################################################################################################################################################

st.write("### Row Descriptions:")
st.write("""
- `count`: Number of non-null or non-missing values in a column.
- `mean`: The calculated mean or average of the column.
- `std (Standard Deviation)`: Values in this row shows how much the values in their respective columns deviate from the mean (average value).
- `min`: Smallest (minimum) number in the column.
- `25% (1st Quartile)`: The data points in this row implies that 25% of it are less than our equal.
- `50% (Median)`: This is the 50th percentile. The values represented in this row are below (<) its value and half (50%) are above (>).
- `75% (3rd Quartile)`: This is the 75th percentile. The values represented in this row are less than or equal (<=) to its value.
- `max`: Largest (maximum) number in the column.
""")

##############################################################################################################################################################################################

st.write("### Column Descriptions")
st.write("""
- `url_length`: URL length in characters.
- `url_entropy`: Randomness in the URL indicating complexity.
- `digit_letter_ratio`: Ratio of digits to letters in the URL.
- `dot_count`: Number of dots in the URL.
- `at_count`: Number of @ symbols in the URL.
- `dash_count`: Number of - symbols in the URL.
- `tld_count`: This defines the count of Top-Level Domains in the URL.
- `subdomain_count`: This defines the count of subdomains in the URL.
- `nan_char_entropy`: This defines the non-alphanumeric chars in the URL.
- `domain_age_days`: Age of domain.
""")

##############################################################################################################################################################################################

st.write("## 1. Legitimacy of a URL that starts with an IP.")

image1 = Image.open('assets/FirstGraph.png')
st.image(image1)

st.write("## Observations:")
st.write("""
- Using the bar graph, we identified that all of the Legitimate sites (1,250,000) do not contain a URL that starts with an IP address. 
- In contrast, out of the Phishing sites (1,223,282), **26,718** of them start with an IP address in their URL.
""")

##############################################################################################################################################################################################
#Second graph

st.write("## 2. The Source of the URL of each and every phishing sites.")

image2 = Image.open('assets/Second Graph.png')
st.image(image2)

st.write("## Observations on Phishing Sources:")
st.write("""
By sorting out the Source of the URL solely based on phishing URLs, we now know that:
- **93%** (1,116,870) comes from **Phishing.Database**.
- **6.47%** (80,821) comes from **PhishTank**.
- **0.04%** (479) comes from **OpenPhish-Community**.
- **Majestic** and **Cisco-Umbrella** are not included in the chart since both of these sources do not have any Phishing sites.
""")


##############################################################################################################################################################################################
#Third Graph
st.write("## 3. Legitimate URLs that has a punycode")

st.write("## Observations")
st.write("By sorting out the data the pie chart shows that majority of legitimate URLs or 99.88% to be exact actually has no punycode, while the other 0.12% does.")
##############################################################################################################################################################################################
#Fourth Graph
st.write("## 4. URLs with has_punycode")


st.write("## Observations")
st.write("With the use of a bar graph we have noticed that a small number of legitimate and phishing URLs use a puny code. This means that majority of URLs though used but it is rare.")

##############################################################################################################################################################################################

st.write("## 5. Legitimacy of a URL that has digits.")

##############################################################################################################################################################################################
#Fifth Graph

image5 = Image.open('assets/FifthGraph.png')
st.image(image5)

st.write("## Observations:")
st.write("""
- With 1,250,000 valid cases compared to 1,190,642 phishing ones, the graphic shows that domains without digits are primarily related with legitimate URLs. This suggests that both types of URLs frequently avoid using numbers to appear trustworthy.
- On the other hand, 59,358 occurrences of domains with digits are exclusively associated with phishing, none of which are authentic. This indicates that the presence of digits is a strong indicator of phishing activity.
- This distinction emphasizes how crucial it is to use domain features as a vital element in phishing detection, such as digit presence.
""")

##############################################################################################################################################################################################

st.write("## 6. Legitimacy of a URL that has internal links.")

##############################################################################################################################################################################################
#Sixth Graph

image6 = Image.open('assets/SixthGraph.png')
st.image(image6)

st.write("## Observations:")
st.write("""
- According to the pie chart, a significant 95.25% of phishing URLs have no internal links, indicating that the majority of phishing sites do not use the internal navigation that is common on trustworthy websites.
""")

##############################################################################################################################################################################################
##7th Graph 
st.write("## 7. Category of URLs either phishing or legitimate.")
##############################################################################################################################################################################################

def pie_chart_url_distribution():
    # Load the dataset from 'out.csv'
    try:
        df = pd.read_csv('datasets/out.csv')  # Ensure 'out.csv' is in the correct directory or provide full path

        # Ensure the 'label' column exists
        if 'label' not in df.columns:
            print("Error: 'label' column not found in the CSV file.")
            return

    except FileNotFoundError:
        print("Error: 'out.csv' file not found.")
        return
    except pd.errors.ParserError as e:
        print(f"Error parsing the CSV file: {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Count occurrences of each label ('phishing' and 'legitimate')
    label_counts = df['label'].value_counts()

    # Define colors for each category (Phishing and Legitimate)
    colors = ['salmon', 'lightgreen']  # Phishing: salmon, Legitimate: lightgreen

    # Create the pie chart with percentage labels
    plt.pie(label_counts, labels=label_counts.index, autopct='%.2f%%', colors=colors)
    plt.title('Distribution of Phishing vs Legitimate URLs')
    

    st.pyplot(plt)
    plt.clf()

# Call the function to display the pie chart
pie_chart_url_distribution()
st.write("## Observations:")
st.write("""
- According to the results of the Pie Chart for Category of URLs if either phishing or legitimate, it gave us a balanced outcome where the both percentage was 50%.
- Although all URLs are not noticeable for phishing the chart represents equal findings for both.
""")
###################################################################################################################################################################################################################

#8th graph

