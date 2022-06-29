# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 13:23:35 2020

@author: mathe
"""
#xpath should look like this '//button[@class = "btn"]'

def inf_look1_click1(driver, xpath):#looks for the element by xpath that you enter, will continue looking until found, when found: element found by xpath is clicked
    while(1):
        if len(driver.find_elements_by_xpath(xpath))>0:
            driver.find_element_by_xpath(xpath).click()
            break 
        
def inf_look1_click2(driver, xpath1, xpath2):#looks for the element by xpath1, will continue looking until found, when found: element found by xpath2 is clicked
    while(1):
        if len(driver.find_elements_by_xpath(xpath1))>0:
            driver.find_element_by_xpath(xpath2).click()
            break
        
def inf_no1_click2(driver, xpath1, xpath2): #looks for when there is no element by xpath1, will continue looking until not found, when not found: will click element found by xpath2
    while(1):
        if len(driver.find_elements_by_xpath(xpath1))==0:
            driver.find_element_by_xpath(xpath2).click()
            break
        
def inf_look1_send1(driver, xpath, keys): #looks for the element by xpath, will continue looking until found, when found: element found will be sent keys
    while(1):
        if len(driver.find_elements_by_xpath(xpath))>0:
            driver.find_element_by_xpath(xpath).send_keys(keys)
            break
        
def inf_look1_refresh_click1(driver, xpath, url): #looks for the element by xpath, if not found it will refresh the page, when found: element will be clicked
    while(1):
        if len(driver.find_elements_by_xpath(xpath))>0:
            driver.find_element_by_xpath(xpath).click()
            break
        else:
            driver.get(url)
            
def once_look1_click1(driver, xpath):#looks for the element by xpath that you enter, will look once, when found: element found by xpath is clicked
    if len(driver.find_elements_by_xpath(xpath))>0:
        driver.find_element_by_xpath(xpath).click()