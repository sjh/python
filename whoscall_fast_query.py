#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from __future__ import print_function

import requests
import sys

from bs4 import BeautifulSoup

API_URL = "https://number.whoscall.com/zh-TW/tw/"


def query_whoscall(phone_number):
    u""" Query whoscall database by HTTP GET https://whoscall.com/zh-TW/ """

    response = requests.get("{}{}".format(API_URL, phone_number))

    if 200 == response.status_code:
        document = response.content
        soup = BeautifulSoup(document, 'html.parser')

        title_string = soup.title.string.strip().split(' ')
        print(u"title_string = {}".format(title_string))
        if len(title_string) == 12:
            owner_name = title_string[0]
            owner_phone = title_string[2]
            owner_city = title_string[6]

        elif len(title_string) == 14:
            owner_name = u"無資料"
            owner_phone = title_string[4]
            owner_city = title_string[8]

        print(u"\n電話號碼: {}\n擁有者: {}\n擁有者所在城市: {}".format(owner_phone, owner_name, owner_city))

        site_container = soup.body.div.contents[3]
        site_main_container = site_container.contents[1]
        ndp_container = site_main_container.contents[1]
        number_info = ndp_container.contents[3]

        if (number_info.p is None or u"這個號碼還沒有被回報" == number_info.p.string.strip()):
            print(u"這個號碼還沒有被回報")

        else:
            owner_name = number_info.h1.string.strip()
            number_info_hr_line = number_info.contents[3]
            business_hour = number_info_hr_line.h2.string.strip()

            try:
                address = number_info_hr_line.address.span.string.strip()
            except(AttributeError):
                address = u""

            print(u"營業狀況: {}".format(business_hour))
            print(u"地址: {}".format(address))


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        for number in sys.argv[1:]:
            query_whoscall(number)
