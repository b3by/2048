import time

from random import choice

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def run(b, a):
    action = ActionChains(b)
    score = b.find_element_by_class_name('score-container').text

    action.send_keys(choice(a))
    action.perform()

    return score


url = 'https://play2048.co/'

browser = webdriver.Chrome()
actions = [Keys.LEFT, Keys.RIGHT, Keys.UP, Keys.DOWN]

browser.get(url)

while True:
    score = run(browser, actions)
    print(score)
    time.sleep(0.5)
