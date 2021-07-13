from selenium import webdriver
import re

browser = webdriver.Firefox()
urlsWithPrices = {'https://www.x-kom.pl/p/440008-monitor-led-24-acer-nitro-vg240ybmiix-czarny.html': 600,
        'https://www.x-kom.pl/p/597339-karta-graficzna-nvidia-gigabyte-geforce-rtx-3070-gaming-oc-8gb-gddr6.html?snrai_campaign=YjYAzyhGQbDJ&snrai_id=123d6481-ac1a-4e61-b0ee-1bce414032f5': 4000,
        'https://www.x-kom.pl/p/363849-zasilacz-do-komputera-silentiumpc-supremo-fm2-750w-80-plus-gold.html': 300,
                  }


def is_price_lower(currentPrice, expectedPrice):
    if currentPrice <= expectedPrice:
        browser.find_element_by_css_selector('.sc-1smss4h-3').click()
        print(f'{currentPrice} is lower than {expectedPrice}, feel free to buy this product')
    else:
        print(f'{currentPrice} is higher than {expectedPrice}, wait till it get lower')


for url in urlsWithPrices:
    browser.get(url)
    nameSelector = '.sc-1bker4h-4'
    priceSelector = '.u7xnnm-4'

    itemName = browser.find_element_by_css_selector(nameSelector)
    itemPrice = re.search(r'(\d+\s?\d+)', browser.find_element_by_css_selector(priceSelector).text).group() # get numeric val from string
    itemPrice = float(re.sub(r'\s+', '', itemPrice))          # remove whitespaces

    print(itemName.text, ':', itemPrice)
    is_price_lower(itemPrice, urlsWithPrices[url])

