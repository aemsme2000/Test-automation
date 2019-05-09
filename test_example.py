from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.

browser = webdriver.Chrome('Chromedriver.exe')
wait = WebDriverWait(browser, 10)
browser.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin%26_encoding%3DUTF8&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

wait.until(EC.presence_of_element_located((By.ID, 'ap_email'))).send_keys('user***@gmail.com')
wait.until(EC.presence_of_element_located((By.ID, 'ap_password'))).send_keys('*********')
wait.until(EC.presence_of_element_located((By.ID, 'signInSubmit'))).click()
wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))).send_keys('Samsung')
#send_keys(Keys.ENTER)
#wait.until.find_element_by_css_selector("input[tabindex='20']").click()            Nasıl kullanabiliriz???
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'nav-input'))).click()
""" send_keys(Keys.ENTER)   
"""
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[data-image-index='2']"))).click()
#wait.until(EC.presence_of_element_located((By.CLASS_NAME,"submit.add-to-registry.wishlist"))).click()
wait.until(EC.presence_of_element_located((By.ID, "add-to-wishlist-button-submit"))).click()

wait.until(EC.presence_of_element_located((By.ID, "WLHUC_continue"))).click()
#wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))).send_keys('apple watch')
"""
#wait.until(EC.presence_of_element_located((By.VALUE, "GO"))).click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "nav-input"))).click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[data-image-index="4"]'))).click()

"""

