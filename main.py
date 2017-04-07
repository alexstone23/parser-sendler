#!/usr/bin/python3.4 -tt
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import data_insert
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

    def get_info():
        login()
        for i in range(1, 15):
            try:
                email = driver.find_element_by_id('email_lbl').text
                car = driver.find_element_by_tag_name('strong').text
                detail = driver.find_element_by_class_name('list').text
                data_insert.connect(detail, car, email)
                nav()
                time.sleep(2)
            except NoSuchElementException:
                time.sleep(2)
                nav()
        driver.close()

    def nav():
        navigation = driver.find_element_by_class_name("dotarrow-right-icon")
        navigation.click()

    while True:
        get_info()
        spam()
        time.sleep(180)

if __name__ == '__main__':
    main()