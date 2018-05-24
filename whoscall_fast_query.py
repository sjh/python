#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from __future__ import print_function

import requests
import sys

from bs4 import BeautifulSoup

API_URL = "https://number.whoscall.com/zh-TW/tw/"


def query_whoscall(phone_number):
    """ Query whoscall database by HTTP GET https://whoscall.com/zh-TW/ """

    response = requests.get("{}{}".format(API_URL, phone_number))

    if 200 == response.status_code:
        document = response.content
        soup = BeautifulSoup(document, 'html.parser')

        title_string = soup.title.string.strip().split(' ')
        if len(title_string) == 12:
            owner_name = title_string[0]
            owner_phone = title_string[2]
            owner_city = title_string[6]

        elif len(title_string) == 14:
            owner_name = "無資料"
            owner_phone = title_string[4]
            owner_city = title_string[8]

        print("\n電話號碼: {}\n擁有者: {}\n擁有者所在城市: {}".format(owner_phone, owner_name, owner_city))

        site_container = soup.body.div.contents[3]
        site_main_container = site_container.contents[1]
        ndp_container = site_main_container.contents[1]
        number_info = ndp_container.contents[3]

        if number_info.p is None:
            pass

        elif "這個號碼還沒有被回報" == number_info.p.string.strip():
            print("這個號碼還沒有被回報")

        else:
            owner_name = number_info.h1.string.strip()
            number_info_ohours_addr = number_info.contents[5]
            all_spans = number_info_ohours_addr.findAll("span")
            if all_spans:
                business_hour = all_spans[1].span.string
            else:
                business_hour = None

            try:
                if all_spans:
                    address = all_spans[-1].string
                else:
                    address = None

            except(AttributeError):
                address = u""

            if business_hour:
                print("營業狀況: {}".format(business_hour))

            if address:
                print("地址: {}".format(address))

    return True


def test_query_whoscall():
    """ Test function for whoscall. """

    assert query_whoscall("0227208889") is True
    assert query_whoscall("0286651720") is True
    assert query_whoscall("0286651719") is True


if __name__ == "__main__":
    """
    if len(sys.argv) >= 2:
        for number in sys.argv[1:]:
            query_whoscall(number)
    """
    print("Whoscall web page has implemented Google ReCaptcha and cannot be used for command \
            line interface now.")
