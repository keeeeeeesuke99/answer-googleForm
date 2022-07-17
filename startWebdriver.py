# webdriverの起動を確認するためのスクリプト

from selenium import webdriver

from time import sleep

def main():
    driver = webdriver.Chrome()

    url = "https://docs.google.com/forms/d/e/1FAIpQLSc5iF_pOHU2fKK4nxeH-63ZyvNYAIUyLmRU3RbljTlnSL_hTA/viewform"

    driver.get(url)
    
    sleep(5)

    driver.close()
    driver.quit()

if __name__ == "__main__":
    main()