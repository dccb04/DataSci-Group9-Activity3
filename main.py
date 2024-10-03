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

st.write("## 2. The Source of the URL of each and every phishing sites.")

# With the use of 'source and 'label' datatypes. We can know and picturize first what will be the graph be consist of.
urlLegitimacy = df.groupby(['source', 'label']).size().unstack() 
urlLegitimacy

def pie_chart_phishing_distribution():

    phishing_df = df[df['label'] == 'phishing'] # Filtering  the Data to include only which are considered as Phishing URLs

    # Count occurrences of each source in the filtered DataFrame
    source = phishing_df['source'].value_counts()

    # Setting the Color of each pie.
    colors = ['salmon', 'green', 'yellow'][:len(source)]

    # Create the pie chart with increased .00 decimal places
    plt.pie(source, labels=source.index, autopct='%.2f%%', colors=colors)
    plt.title('Source Distribution of Phishing URLs')
    
    st.pyplot(plt)
    plt.clf()

pie_chart_phishing_distribution()

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

urlLegitimacy = df.groupby(['label', 'has_punycode']).size().unstack()
urlLegitimacy


def pie_chart_Legitimacy_with_punycode():

    legitimacy_df = df[df['label'] == 'legitimate'] # Filters through the data to find the specific data needed

    # Check the occurances
    has_punycode = legitimacy_df['has_punycode'].value_counts()

    #  Color of the pies.
    colors = ['red', 'blue', 'green'][:len(has_punycode)]

    # Create the pie
    plt.pie(has_punycode, labels=has_punycode.index, autopct='%.2f%%', colors=colors)
    plt.gcf().set_facecolor('lightgreen')

    plt.title('Legitimate URLs with punycode')
    plt.show()

# Call the function
pie_chart_Legitimacy_with_punycode()

st.write("## Observations")
st.write("By sorting out the data the pie chart shows that majority of legitimate URLs or 99.88% to be exact actually has no punycode, while the other 0.12% does.")
##############################################################################################################################################################################################
#Fourth Graph
st.write("## 4. URLs with has_punycode")
urlLegitimacy = df.groupby(['label', 'has_punycode']).size().unstack()
urlLegitimacy

def bar_plot_legitimacy_has_punycode():

  plt.figure(figsize=(8, 8)).set_facecolor('lightblue') # define size of the graph

  ax = sns.countplot(x='label', hue='has_punycode', data=df)
  plt.title('URLs that has a punycode graph')

  plt.xlabel('Legitimacy of URLs')  # label for X-Axis
  plt.ylabel('Total of URLs')       # label for Y-Axis


  # shows the count of the graphs
  for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')

  plt.show()

bar_plot_legitimacy_has_punycode()

st.write("## Observations")
st.write("With the use of a bar graph we have noticed that a small number of legitimate and phishing URLs use a puny code. This means that majority of URLs though used but it is rare.")

##############################################################################################################################################################################################

st.write("## 5. Legitimacy of a URL that has digits.")

urlLegitimacy = df.groupby(['domain_has_digits', 'label']).size().unstack()
urlLegitimacy

##############################################################################################################################################################################################
#Fifth Graph

def bar_plot_legitimacy_digits():
    # Create a figure for the plot with a size of 8x8 inches, and set the background color to light blue.
    plt.figure(figsize=(8, 8)).set_facecolor('lightblue')

    # Use seaborn's countplot to create a bar plot.
    ax = sns.countplot(x='domain_has_digits', hue='label', data=df)
    plt.title('URLs with Digits in Domain and Legitimacy')

    plt.xlabel('Domain Has Digits')  # Label for the X-axis indicating whether the domain has digits.
    plt.ylabel('Total of URLs')      # Label for the Y-axis representing the total number of URLs.

    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}',
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center',
                    xytext=(0, 10), textcoords='offset points')

    st.pyplot(plt)
    plt.clf()

bar_plot_legitimacy_digits()

st.write("## Observations:")
st.write("""
- With 1,250,000 valid cases compared to 1,190,642 phishing ones, the graphic shows that domains without digits are primarily related with legitimate URLs. This suggests that both types of URLs frequently avoid using numbers to appear trustworthy.
- On the other hand, 59,358 occurrences of domains with digits are exclusively associated with phishing, none of which are authentic. This indicates that the presence of digits is a strong indicator of phishing activity.
- This distinction emphasizes how crucial it is to use domain features as a vital element in phishing detection, such as digit presence.
""")

##############################################################################################################################################################################################

st.write("## 6. Legitimacy of a URL that has internal links.")

urlLegitimacy = df.groupby(['has_internal_links', 'label']).size().unstack()
urlLegitimacy

##############################################################################################################################################################################################
#Sixth Graph

def pie_chart_phishing_distribution_based_on_internal_links():
    # Filter the dataset for phishing URLs 
    phishing_distribution = df[df['label'] == 'phishing'].groupby('has_internal_links').size()

    # Color of each pie section
    colors = ['#A3CFF9', '#F88C96'][:len(phishing_distribution)]

    # Create a pie chart using the phishing distribution data.
    # The labels are mapped based on the 'has_internal_links' column (True or False).
    plt.pie(phishing_distribution, labels=phishing_distribution.index.map({True: 'Has Internal Links', False: 'No Internal Links'}), autopct='%.2f%%', colors=colors)
    plt.title('Source Distribution of Phishing URLs Based on Internal Links')
    st.pyplot(plt)
    plt.clf()

pie_chart_phishing_distribution_based_on_internal_links()

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
###################################################################################################################################################################################################################
##8th Graph 
st.write("## 8. Length of URLs in Characters.")
###################################################################################################################################################################################################################
# Load the data from the CSV file
df = pd.read_csv('datasets/out.csv')  # Adjust encoding if necessary

# Clean column names
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names

# Debugging output to check column names
print("Columns in the dataset:", df.columns)  # Print column names

# Check if 'Base URL' exists before calculating lengths
if 'Base URL' in df.columns:
    # Calculate the length of each URL and add it as a new column
    df['url_length'] = df['Base URL'].apply(len)

    # Create a bar chart for URL lengths
    plt.figure(figsize=(10, 6))
    plt.bar(df['Base URL'], df['url_length'], color='skyblue')
    plt.title('URL Length in Characters')
    plt.xlabel('Base URL')
    plt.ylabel('Length (Characters)')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjusts plot to ensure everything fits without overlap

    # Show the plot
    plt.show()
    st.pyplot(plt)
    plt.clf()
else:
    print("The required column 'Base URL' is not found in the dataset.")
###################################################################################################################################################################################################################

