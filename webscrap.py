import requests
from bs4 import BeautifulSoup
import csv

product = input("Enter a product name : ")

try:
    result = requests.get(f"https://www.flipkart.com/search?q={product}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off").text
except Exception as e:
    print("Sorry, something went wrong : ",e)

#create a csv file to write data
csv_file = open(f'csv_files/{product}_data.csv', 'w') 
write_csv = csv.writer(csv_file)
#column names
write_csv.writerow(['Title', 'Rating','Rated by no. of people','Price','Product Link'])

soup = BeautifulSoup(result, 'lxml')

for product in soup.find_all('div', class_='_1UoZlX'):

    prod_title = product.find('div', class_='_3wU53n').text
    print("Product Title : ", prod_title)
    try:
        prod_rating = product.find('div', class_='hGSR34').text
        print("Rating : ",prod_rating)

        prod_rated_by_people = product.find('span', class_='_38sUEc')
        prod_rated_by_people = prod_rated_by_people.span.span.text
        print("Rated by no. of People :",prod_rated_by_people)

    except Exception as e:
        prod_rating = None
        prod_rated_by_people = None

    prod_price = product.find('div', class_='_1vC4OE _2rQ-NK').text
    prod_price = prod_price.split('₹')[1]
    print("Price : ",prod_price)
    
    prod_link = product.find('a', class_='_31qSD5')['href']
    prod_link = 'https://www.flipkart.com'+prod_link
    print("Link : ",prod_link)
    print()

    #write actual data in csv
    try:
        write_csv.writerow([prod_title, prod_rating, prod_rated_by_people, prod_price, prod_link])
    except Exception as e:
        print(e)


csv_file.close()
