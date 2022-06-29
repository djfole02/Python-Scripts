# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:04:28 2020

@author: Danny
"""
URL_Checkout = 'https://www.bestbuy.com/cart'
email = ''
password = ''
count = 0
import time
import find_xpath
import emailbot
from selenium import webdriver


def login(driver):
    find_xpath.inf_look1_click1(driver, '//span[@class = "flyBtn"]')
    find_xpath.inf_look1_click1(driver, '//button[@class = "lam-signIn__button btn btn-secondary"]')
    find_xpath.inf_look1_send1(driver, '//input[@type = "email"]', email)
    find_xpath.inf_look1_send1(driver, '//input[@type = "password"]', password)
    find_xpath.inf_look1_click1(driver, '//button[@type = "submit"]')
    time.sleep(2)
    
def checkout(driver, URL):
    while (1):
        find_xpath.inf_look1_refresh_click1(driver, '//button[@class = "btn btn-lg btn-block btn-primary"][text() = "Checkout"]', URL)
        emailbot.bot()
        find_xpath.inf_look1_click1(driver, '//button[@class = "btn btn-lg btn-block btn-primary button__fast-track"]')
        print('We did it boys, we got one')
        break

def BB_Checkout():
    driver_bb_checkout = webdriver.Edge(executable_path=r'C:\msedgedriver.exe')
    driver_bb_checkout.maximize_window()
    driver_bb_checkout.get(URL_Checkout)
    login(driver_bb_checkout)
    checkout(driver_bb_checkout, URL_Checkout)
    
BB_Checkout()