import tempfile
from selenium import webdriver
from time import sleep
from PIL import Image
dirpath = tempfile.mkdtemp()
#print(dirpath)
driver = webdriver.Chrome()
driver.get('https://github.com/dftmy/Tiny_learning_projects')
sleep(3)
driver.get_screenshot_as_file(f'{dirpath}/screenshot.png')
screen_file = Image.open(f'{dirpath}/screenshot.png', 'r').show()







