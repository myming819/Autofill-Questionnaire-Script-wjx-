# -*- coding: utf-8 -*-
"""
______________________________
    Author: MY
    Time : 2024/6/5 22:16
    File: 自动填写问卷星脚本.py
    Software: PyCharm
______________________________
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import random
import time

# 使用JavaScript滚动页面到指定距离
def gundong(driver, distance):
    js = f"var q=document.documentElement.scrollTop={distance}"
    driver.execute_script(js)

# 填写问卷答案
def fill_answers(driver, start, end, fill_data):
    for i in range(start, end):
        gundong(driver, i * 100)  # 滚动页面到当前题目
        ans = driver.find_elements(By.XPATH, f'//*[@id="div{i}"]')
        if i in fill_data:
            for answer in ans:
                input_field = answer.find_elements(By.CSS_SELECTOR, "input")
                if input_field:
                    if input_field[0].get_attribute('type') == 'file':
                        input_field[0].send_keys(fill_data[i])  # 上传文件
                    else:
                        input_field[0].send_keys(fill_data[i])  # 填写输入框
                else:
                    options = answer.find_elements(By.CSS_SELECTOR, '.ui-radio, .ui-checkbox')
                    if options:
                        random.choice(options).click()  # 这是选择题选项，这里不考虑有选择题的情况，随机选择一个选项
                time.sleep(random.uniform(0.01, 0.1))  # 你想要快点填也行，自己设置每道题之间的间隔

def run(GoogleExe, GoogleDriver, fill_data):
    url_survey = 'https://www.wjx.cn/vm/tU8aXh0.aspx'  # 问卷地址,直接上问卷星网址
    option = webdriver.ChromeOptions()
    option.add_argument('--disable-automation')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    option.binary_location = GoogleExe
    service = Service(executable_path=GoogleDriver)
    driver = webdriver.Chrome(service=service, options=option)
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    driver.get(url_survey)
    fill_answers(driver, 1, 15, fill_data)  # 注意这里是前闭后开，14道题所以写15
    time.sleep(1)  # 我觉得这里需要改了，因为太快了的话，你懂的，不能光明正大的开挂呀

    # 点击“提交”按钮
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ctlNext"]'))
    )
    next_button.click()

    print('成功提交问卷！！！')
    time.sleep(6.6)
    driver.quit()

if __name__ == "__main__":
    # Chrome浏览器可执行文件路径，自己找，安装了Google的肯定有这个路径
    googleExe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    # ChromeDriver可执行文件路径，这个得自己下符合自己版本的，然后放在上面的文件夹里面
    googleDriver = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"

    # 需要填写的问卷答案数据
    fill_data = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: '10',
        11: '11',
        12: '12',
        13: '13',
        14: r"E:\main\1.jpg"  # 确保文件路径格式正确
        # 需要啥添加啥
    }

    # 执行自动填写问卷
    run(googleExe, googleDriver, fill_data)

