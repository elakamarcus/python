#!/bin/python3

import requests
from bs4 import BeautifulSoup

cnt = "action=200&the_alldata=district_select_multiple%3D107%26district_select_multiple%3D108%26s_order%3D0%26s_order_direction%3D0%26s_type%3D0%26s_sellrent%3D2%26s_sellrange%3D0%26s_sellrange_l%3D0%26s_sellrange_h%3D0%26s_rentrange%3D0%26s_rentrange_l%3D0%26s_rentrange_h%3D0%26s_source%3D0%26s_roomno%3D0%26s_area%3D6%26s_area_l%3D680%26s_area_h%3D1700%26s_cached_fav%3D0%26s_stored_fav%3D0%26s_page%3D0%26s_myrelated%3D0%26s_cat_child%3D0%26s_restore_search_codition%3D0%26s_global_tag%3D0%26s_viewmode%3D0%26s_age%3D0%26s_age_l%3D0%26s_age_h%3D0%26s_rent%3D0%26stypeg_1_mode%3D1%26stypeg_1_18%3D1%26stypeg_1_17%3D1%26stypeg_1_10%3D1%26stypeg_1_11%3D1%26stypeg_1_5%3D1%26stypeg_1_7%3D1%26stypeg_1_6%3D1%26stypeg_1_19%3D1%26stypeg_8_16%3D0%26s_keywords%3D%26input_low%3D%26input_high%3D%26s_area_buildact%3D1%26input_low%3D680%26input_high%3D1700%26input_low%3D%26input_high%3D"
referer = "https://www.28hse.com/rent/district-g47"
url = "https://www.28hse.com/utf8/search3_ajax.php"

bh = {"User-agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0"}

build = {"User-agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0", "Referer" : "https://www.28hse.com/rent/district-g47"}

ra = requests.get(url, data=post, headers=build)
print(ra.data)

mydivs = soup.findAll("div", {"class": "stylelistrow"})
