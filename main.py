from pyppeteer import launch
import asyncio
import re
from time import sleep



registerUrl = 'https://konto-pocztowe.interia.pl/#/nowe-konto/darmowe'
async def main():
    try:
        #entering the page
        browser = await launch(headless = False)
        page = await browser.newPage()
        await page.goto(registerUrl)
        #rodo pass
        rodoButton = await page.querySelector('.rodo-popup-agree')
        await rodoButton.click()
        #search and type name and surname
        elements = await page.querySelectorAll('.register-form__inputs > div > input')
        for index, element in enumerate(elements):
            _id = await page.evaluate('element => element.id',element)
            print(index)
            if index == 0:
                await page.type("input[id=" + _id + "]","maciek")
            if index == 1:
                await page.type("input[id=" + _id + "]", "mioduszewski")





        sleep(5)
        # await browser.close()



    except:
        print("Wystapil blad")
asyncio.get_event_loop().run_until_complete(main())