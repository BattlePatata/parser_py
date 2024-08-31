from LxmlSoup import LxmlSoup
import requests, os

user_site = input('Please enter your website: ')

try:
    html = requests.get(f'https://{user_site}').text
except:
    html = requests.get(f'http://{user_site}').text

soup = LxmlSoup(html)

# Finding all usefull text
sec_texts = soup.find_all('section')
container_texts = soup.find_all('container')
_texts = sec_texts + container_texts
# End of finding all usefull text

# Getting rid off all whitespaces and creating a log file for the results
res_file = os.path.exists(f"./{user_site}.txt")
if res_file == 0:
    with open(f'{user_site}.txt', 'w', encoding='utf-8') as write_file:
        print(f'{user_site}.txt created!')

for i, data in enumerate(_texts):
    res = data.text()
    name = ' '.join(res.split())

    with open(f'{user_site}.txt', 'a', encoding='utf-8') as write_file:
        write_file.write(f'{name}\n\n')

    print()
    print(name)
# The end of getting rid off all whitespaces and creating a log file for the results