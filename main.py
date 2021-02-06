import os
from selenium import webdriver
from time import sleep, gmtime

from russian_names import RussianNames
import pytils.translit

from random import randint

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=640x480')
chrome_options.add_argument("--disable-extensions")


def phoneCreator():
    return '89' + str(randint(100000000, 999999999))


url = 'https://студенческийлидер.рф/video'
loopLen = int(input('Введите количество лайков: '))
counter = 0
chromeBrowser = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'), chrome_options=chrome_options)
chromeBrowser.get(url)


def likeIncrimination():
    likeButton = chromeBrowser.find_element_by_id('like-4983e4426918150342349d2f8dbc5de7')
    likeButton.click()

    sleep(0.5)

    name = chromeBrowser.find_element_by_name('name')
    company = chromeBrowser.find_element_by_name('company')
    phone = chromeBrowser.find_element_by_name('phone')
    email = chromeBrowser.find_element_by_name('email')

    person = RussianNames(patronymic=False).get_person()
    personSurname = person.split()[1]
    personSurnameEng = pytils.translit.translify(personSurname.replace('\'', '').lower())


    samplePhone = phoneCreator()
    name.send_keys(person)
    company.send_keys('РГУПС')
    phone.send_keys(samplePhone)
    email.send_keys(personSurnameEng + '@mail.ru')

    submit = chromeBrowser.find_element_by_css_selector('button.button')
    submit.click()

    sleep(0.5)

    likeButton = chromeBrowser.find_element_by_id('like-4983e4426918150342349d2f8dbc5de7')
    likeButton.click()
    print(f'Лайкнул: {person}, РГУПС, {samplePhone}, {personSurnameEng}@mail.ru')
    chromeBrowser.delete_all_cookies()
    chromeBrowser.refresh()

if __name__ == "__main__":
    for i in range(loopLen):
        try:
            likeIncrimination()
            counter += 1
        except:
            print('слишком быстро, один лайк потерялся...')
            chromeBrowser.get(url)

        print(f'Добавлено лайков: {counter}, {gmtime().tm_hour}:{gmtime().tm_min}:{gmtime().tm_sec}')

