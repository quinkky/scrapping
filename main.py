from pyppeteer import launch
import asyncio
from time import sleep
from helperNames import randomName, randomSurname
from fileServis import saveUserToFile


registerUrl = 'https://konto-pocztowe.interia.pl/#/nowe-konto/darmowe'
async def main():
    generatedName = randomName()
    generatedSurname = randomSurname()
    #entering the page
    browser = await launch(headless = False)
    page = await browser.newPage()
    await page.goto(registerUrl)
    #rodo pass
    await page.waitForSelector('.rodo-popup-agree')
    rodoButton = await page.querySelector('.rodo-popup-agree')
    await rodoButton.click()
    #search and type name and surname
    await page.waitForSelector('.register-form__inputs > div > input')
    elements = await page.querySelectorAll('.register-form__inputs > div > input')
    for index, element in enumerate(elements):
        if index == 0:
            _id = await page.evaluate('element => element.id', element)
            await page.type("input[id=" + str(_id) + "]",generatedName)
        if index == 1:
            _id = await page.evaluate('element => element.id', element)
            await page.type("input[id=" + str(_id) + "]", generatedSurname)
    await page.waitForSelector("#birthdayDay")
    await page.type("#birthdayDay","10")
    await page.click('.icon-arrow-right-full')
    await page.click(".account-select__options__item")
    await page.type('#birthdayYear',"1990")
    sleep(1)
    await page.click('#mainApp > div > div > div > div > div.register-page-wrapper > div > form > div.register-form__inputs > div.account-input-container.account-select > div.icon-arrow-right-full')
    sleep(1)
    await page.click('.account-select__options__item')
    await page.waitForSelector('.register-form__inputs-mail > div > input')
    sleep(1)
    await page.click('.register-form__inputs-mail > div > input')
    parsedEmail = generatedName + '.' + generatedSurname + '3123'
    for x in range(20):
        await page.keyboard.press('Backspace')
    sleep(2)
    await page.type('.register-form__inputs-mail > div > input',parsedEmail)
    sleep(1)
    await page.type('#password',"Adfgkdfgad1232.")
    sleep(1)
    await page.type('#rePassword',"Adfgkdfgad1232.")
    await page.click("div.checkbox-label")
    sleep(3)
    await page.waitForSelector('div.register-form__information > button')
    await page.click('div.register-form__information > button')
    await page.click('div.register-form__information > button')
    sleep(5)
    await browser.close()
    saveUserToFile(generatedName,generatedSurname)
    sleep(10)


asyncio.get_event_loop().run_until_complete(main())