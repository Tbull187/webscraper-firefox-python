import requests
import time
from selenium import webdriver
from PIL import Image
from io import BytesIO

url = "http://www.unsplash.com"

driver = webdriver.Firefox(executable_path=r'geckodriver')
# navigate to page
driver.get(url)

# scroll page and wait 5 seconds
driver.execute_script("window.scrollTo(0,1000);")
time.sleep(5)

# select img elements and print their URLs
image_elements = driver.find_elements_by_css_selector("#gridMulti img")

i = 0
for elem in image_elements:
    image_url = elem.get_attribute("src")
    # send HTTP GET, get and save img from the response
    image_object = requests.get(image_url)
    print(image_object)
    image = Image.open(BytesIO(image_object.content))
    image.save("./images/image" + str(i) + "." + image.format, image.format)
    i += 1
