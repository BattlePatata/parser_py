from LxmlSoup import LxmlSoup
import requests, os

user_site = input('Please enter your website: ')
headers = {'User-Agent': 'Mozilla/55.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.46'}

try:
    html = requests.get(f'https://{user_site}', headers=headers).text
except:
    html = requests.get(f'http://{user_site}', headers=headers).text

soup = LxmlSoup(html)

# Finding all usefull text
sec_texts = soup.find_all('section')
_texts = sec_texts

if len(_texts) == 0:
    container_texts = soup.find_all('container')
    _texts = container_texts

if len(_texts) == 0:
    main_texts = soup.find_all('main')
    _texts = main_texts

if len(_texts) == 0:
    div_texts = soup.find_all('div')
    _texts = div_texts

# End of finding all usefull text

# Getting rid off all whitespaces and creating a log file for the results
res_file = os.path.exists(f"./{user_site}.txt")
if res_file == 0:
    with open(f'{user_site}.txt', 'w', encoding='utf-8') as write_file:
        print(f'{user_site}.txt created!')

prev_name = ''
for i, data in enumerate(_texts):
    res = data.text()
    if len(res) > 0:
        name = ' '.join(res.split())
        five_chars = ''
        for chars in name[:6]:
            five_chars += chars
        
        if five_chars not in prev_name:
            with open(f'{user_site}.txt', 'a', encoding='utf-8') as write_file:
                write_file.write(f'{name}\n\n')

        print()
        print(name)
# The end of getting rid off all whitespaces and creating a log file for the results
