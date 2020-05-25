from django.shortcuts import render
import selenium
from selenium import webdriver
import time


def WebTest(request,queryset):
    
    url = queryset.web_test_url
    elem = queryset.web_test_elem
    method = queryset.web_test_method
    singular_or_plural = queryset.web_test_plural
    inputs = queryset.web_test_input

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(url)


    if method == "ID":
        result = By_ID(driver,elem,inputs)
    if method == "classname":
        result = By_Classname(driver,elem,singular_or_plural)
    if method == "Xpath":
        result = By_Xpath(driver,elem,singular_or_plural)
    if method == "css_seletor":
        result = By_Css_seleter(driver,elem,singular_or_plural)    
    
    time.sleep(5)

    return result




def By_ID(driver,elem,input):
    
    f_elem = driver.find_element_by_id(elem)
    f_elem.send_keys(input)
    return "演示完毕"


def By_Classname(driver,elem,singular_or_plural):
    if singular_or_plural == "singular":
        f_elem = driver.find_element_by_class_name(elem)
        result = f_elem.text
    if singular_or_plural == "plural":
        f_elem = driver.find_elements_by_class_name(elem)
        result = []
        for i in f_elem:
            result.append(i.text)
    return result
            

def By_Xpath(driver,elem,singular_or_plural):
    if singular_or_plural == "singular":
        f_elem = driver.find_element_by_xpath(elem)
        result = f_elem.text
    if singular_or_plural == "plural":
        f_elem = driver.find_elements_by_xpath(elem)
        result = []
        for i in f_elem:
            result.append(i.text)
    return result

def By_Css_seleter(driver,elem,singular_or_plural):
    if singular_or_plural == "singular":
        f_elem = driver.find_element_by_css_selector(elem)
        result = f_elem.text
    if singular_or_plural == "plural":
        f_elem = driver.find_elements_by_css_selector(elem)
        result = []
        for i in f_elem:
            result.append(i.text)
    return result
    

# Create your views here.
