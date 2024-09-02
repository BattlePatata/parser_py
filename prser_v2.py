from bs4 import BeautifulSoup as bs
import requests, os

user_site = input('Please enter your website: ')
headers = {'User-Agent': 'Mozilla/55.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.46'}

try:
    html = requests.get(f'https://{user_site}', headers=headers).text
except:
    html = requests.get(f'http://{user_site}', headers=headers).text

soup = bs(html)

for data in soup(['style', 'script', 'header', 'footer']):
    data.decompose()

mid_res = ' '.join(soup.stripped_strings)
prev_chars = ''
if len(mid_res) > 0:
    five_chars = ''
    for chars in mid_res[:6]:
        five_chars += chars
    
    new_line = '\n'
    nth_char = 120

    res = ''
    for idx, ele in enumerate(mid_res):
        if idx % nth_char == 0 and idx != 0:
            res = res + new_line + ele
        else:
            res = res + ele
    
    if five_chars not in prev_chars:
        with open(f'{user_site}.txt', 'a', encoding='utf-8') as write_file:
            write_file.write(f'{res}\n\n')
    
    prev_chars = five_chars

print(res)

