from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep
import urllib.parse
import random

# # 不要エラーメッセージを削除するオプション
# ChromeOptions = webdriver.ChromeOptions()
# # ChromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
# ChromeOptions.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

def main():
  """
  参考にした文献
  https://www.youtube.com/watch?v=92R8FTg56ik
  =====エラー解決情報（エラーが出たときの参考にしてください）=====
  「selenium.common.exceptions.WebDriverException: Message: unknown error: Element is not clickable at point」
  https://qiita.com/DNA1980/items/528ff6269986b262acdc#%E5%95%8F%E9%A1%8C%E8%A7%A3%E6%B1%BA
  「selenium.common.exceptions.WebDriverException: Message: unknown error: call function result missing 'value'」
  Python seleniumのsend_keysで出たエラーの対処方法 - Qiita
  https://qiita.com/orangeboy/items/6fdddebc1dc919f6d9e1
  seleniumを使用しようとしたら、「"chromedriver"は開発元を検証できないため開けません。」と言われた - Qiita
  https://qiita.com/apukasukabian/items/77832dd42e85ab7aa568
  =====crontabの参考コード=====
  * * * * * /bin/bash /Users/naoyashiga/youtube/naoya_tech/031_060/043_google_Form/reply_googleform.sh
  """
  driver = webdriver.Chrome()

  # TODO googleFormの項目によって要修正
  # entry.[質問ID]=[回答]
  student_number = 9999
  student_name = urllib.parse.quote("山田太郎")
  class_name = urllib.parse.quote("1年A組")
  club_name = urllib.parse.quote("野球部")
  station_a = urllib.parse.quote("池袋駅")
  station_b = urllib.parse.quote("上野駅")

  # TODO googleFormの項目によって要修正
  # 36度1分〜7分になる
  yesterday_taion = 36 + random.randint(1, 7) / 10
  today_taion = 36 + random.randint(1, 7) / 10

  parameter = "?usp=pp_url&entry.1718818793={}&entry.1486711776={}&entry.171685049={}&entry.1138618080={}&entry.309239632={}&entry.309239632={}&entry.426177823={}&entry.1537097308={}".format(
    student_number,
    student_name,
    class_name,
    club_name,
    station_a,
    station_b,
    yesterday_taion,
    today_taion
  )
  url = "https://docs.google.com/forms/d/e/1FAIpQLSc5iF_pOHU2fKK4nxeH-63ZyvNYAIUyLmRU3RbljTlnSL_hTA/viewform{}".format(parameter)

  try:
    driver.get(url)

    # ボタンが見える位置までスクロールしておく
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)

    # TODO googleFormの送信ボタンのclassNameによって要修正
    # 送信ボタンを押下
    e = driver.find_element(By.CLASS_NAME, "VkkpIf")
    print(e)
    e.click()

  finally:
    sleep(2)
    driver.close()
    driver.quit()

if __name__ == "__main__":
    main()