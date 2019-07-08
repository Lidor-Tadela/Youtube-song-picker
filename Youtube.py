import time
from selenium import webdriver

driver = webdriver.Chrome(r"link to chrome drive")
driver.minimize_window()
song = input("choose a song you would like to listen :")
driver.get('https://www.youtube.com/results?search_query=' + song)
time.sleep(10)

pick = input("Is this the song you were looking for?" + driver.find_element_by_xpath('//*[@id="video-title"]').get_attribute('innerHTML') +
             "   (Y/N)")

if pick == "Y" or "y":
    driver.find_element_by_xpath('//*[@id="video-title"]').click()
    driver.maximize_window()

elif pick == "N" or "n":
    time.sleep(3)
    lop = driver.find_elements_by_id('video-title')
    print("is it on of the videos below ?")
    for x in range(1, len(lop)):
        print(str(x) + ". " + x.text)
        
    val = int(input("\n \n is the video you wanted in this list?\n write the number of the video :\n")) - 1
    driver.find_elements_by_xpath('//*[@id="video-title"]')[val].click()

else:
    print("jeez you dumb..")
    driver.close()