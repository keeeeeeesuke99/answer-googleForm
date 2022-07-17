# webdriverの起動を確認するためのスクリプト

from selenium import webdriver

from time import sleep

def main():
    driver = webdriver.Chrome()

    url = "https://docs.google.com/forms/d/e/1FAIpQLSc0QOFKz0DnOO9Wx9LPX3rs3mNghKRIftLC6SNgalsTJyAF7g/viewform"

    driver.get(url)
    
    sleep(5)

    driver.close()
    driver.quit()

if __name__ == "__main__":
    main()