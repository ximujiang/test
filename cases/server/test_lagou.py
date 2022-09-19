# -*- coding: utf-8 -*-
import requests
import allure

@allure.epic("ccc")
class TestLaGou:
    def setup_class(self):
        self.s = requests.Session()
        self.url = "https://www.lagou.com/"

    @allure.story("xxxx")
    def test_visit_lagou(self):
        result = self.s.get(self.url)
        assert result.status_code==100

    def teardown_class(self):
        self.s.close()
