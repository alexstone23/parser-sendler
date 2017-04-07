#!/usr/bin/python3.4 -tt
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from spammer import spam
from selenium.common.exceptions import NoSuchElementException
import config


def main():

    def login():
        global driver
        driver = webdriver.PhantomJS()
        driver.get(config.zapchast_url)
        log = driver.find_element_by_name('email')
        log.send_keys(config.zapchast_login)
        password = driver.find_element_by_name('passgo')
        password.send_keys(config.zapchast_pass)
        submit = driver.find_element_by_class_name('button-grey')
        submit.click()
        print('Logged')
        order_all = driver.find_element_by_xpath("//*[@aria-describedby='list_lead']")
        order_all.click()
        print('Start grabbing')


    def nav():
        navigation = driver.find_element_by_class_name("dotarrow-right-icon")
        navigation.click()

    while True:
        get_info()
        spam()
        time.sleep(180)

if __name__ == '__main__':
    main()