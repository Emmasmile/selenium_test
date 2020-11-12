#!/usr/bin/env python
# encoding: utf-8
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo:
    def setup(self):
        self.driver = webdriver.Chrome('E:\selenium_chromedriver\chromedriver_win32\chromedriver.exe')
        self.driver.get('https://www.baidu.com/')

    def teardown(self):
        sleep(5)
        self.driver.quit()

    # @pytest.mark.skip
    @pytest.mark.parametrize('keyword', [
        '霍格沃兹',
        '货拉拉'
    ])
    def test_search(self, keyword):
        self.driver.find_element(By.ID, 'kw').send_keys(keyword)
        self.driver.find_element(By.ID, 'su').click()
        self.driver.back()
