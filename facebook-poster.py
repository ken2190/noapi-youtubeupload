#!/usr/bin/env	python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys


def main(input_str = "testing"):
	driver = webdriver.Firefox()
	driver.get("https://www.facebook.com")
	action = webdriver.ActionChains(driver)

	# send email id.
	action.send_keys("")
	action.perform()
	action.send_keys(Keys.TAB)
	action.perform()
	
	# send password
	action.send_keys("")
	action.perform()
	action.send_keys(Keys.ENTER)
	action.perform()

	time.sleep(5)	# Lazy people use time.sleep rather using 
			# element loaded or not

	# select home button
	driver.execute_script("document.getElementsByClassName('oajrlxb2 g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb n00je7tq arfg74bv qs9ysxi8 k77z8yql btwxx1t3 abiwlrkh p8dawk7l lzcic4wl bp9cbjyn j83agx80 kj0jemqk d8o5xnl0 cxgpxx05 sj5x9vvc')[0].click()")
	time.sleep(3)

	# click post bar
	driver.execute_script('document.getElementsByClassName("oajrlxb2 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x i1ao9s8h esuyzwwr f1sip0of abiwlrkh p8dawk7l lzcic4wl bp9cbjyn b3i9ofy5 orhb3f3m czkt41v7 fmqxjp7s emzo65vh j83agx80 btwxx1t3 buofh1pr jifvfom9 l9j0dhe7 idiwt2bm kbf60n1y cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq")[0].click()')

	time.sleep(3)

	# send post string
	action.send_keys(input_str)
	action.perform()
	time.sleep(3)

	# post
	driver.execute_script('document.getElementsByClassName("rq0escxv l9j0dhe7 du4w35lb d2edcug0 hpfvmrgz bp9cbjyn j83agx80 pfnyh3mw j5wkysh0 hytbnt81")[4].click()')
	time.sleep(3)

	# exit
	driver.close()

if __name__ == "__main__":
	if len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		main()
