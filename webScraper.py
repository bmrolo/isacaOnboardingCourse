import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.scrapethissite.com/pages/simple/"

website = requests.get(url)

soup = BeautifulSoup(website.text, "html.parser")

countries = soup.findAll("h3", attrs={"class":"country-name"})
populations = soup.findAll("span", attrs={"class":"country-population"})

# Create an empty list to store data
data = []

# Iterate over the extracted elements and store data in the list
for country, population in zip(countries, populations):
    country_name = country.text.strip()
    population_value = int(population.text.strip())
    data.append({"Country": country_name, "Population": population_value})

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Print the first few rows of the DataFrame
print(df.head())