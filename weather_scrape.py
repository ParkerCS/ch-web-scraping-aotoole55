
# Below is a link to a 10-day weather forecast at weather.com
# Use urllib and BeautifulSoup to scrape data from the weather table.
# Print a brief synopsis of the weather for the next 10 days.
# Include the day, date, high temp, low temp, and chance of rain.
# You can customize the text as you like, but it should be readable
# for the user.  You will need to target specific classes or other
# attributes to pull some parts of the data.
# (e.g.  Wednesday, March 22: the high temp will be 48 with a low of 35, and a 20% chance of rain). (25pts)

from bs4 import BeautifulSoup
import urllib.request

url = "https://weather.com/weather/tenday/l/USIL0225:1:US"

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page.read(), 'html.parser')

my_table= soup.find('table')
print(my_table)
headers = [x.text.strip() for x in my_table.findAll('th')]
print(headers)

data_list = [[y.text.strip() for y in x.findAll('td')] for x in soup.find('table').findAll('tr')][1:]

data_list = [x[1:] for x in data_list]

print(data_list)

today = data_list[0][0][0:5]
print(today)

#degree_sign = u'\N{DEGREE SIGN]'

print('The weather for', today +',', data_list[0][0][5:] , "is", data_list[0][1].lower()+ ". The high will be", data_list[0][2][0:2]+ "°F and the low will be", data_list[0][2][3:5] +'°F. The chance of rain is', data_list[0][3] +".")

for pos in range(1, len(data_list)):
    print('The weather for', data_list[pos][0][0:3] +',', data_list[pos][0][3:] , "is", data_list[pos][1].lower()+ ". The high will be", data_list[pos][2][0:2]+ "°F and the low will be", data_list[pos][2][3:5] +'°F. The chance of rain is', data_list[pos][3] +".")
