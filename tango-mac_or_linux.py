while True:
    try:
        from selenium import webdriver
        import chromedriver_binary
        import time
        from selenium.webdriver.chrome.options import Options
        response_url = "https://student.espire.jp/"
        def click(xpath):
            driver.find_element_by_xpath(xpath).click()
        def insert_pw(xpath, str):
            driver.find_element_by_xpath(xpath).send_keys(str)

        options = Options()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(1)
        driver.get(response_url)

        login_id = "id入れろ"
        login_id_xpath = '//*[@id="student_login_name"]'
        insert_pw(login_id_xpath, login_id)

        login_pw = "パス入れろ"
        login_pw_xpath = '//*[@id="student_password"]'
        login_pw_button = '//*[@id="new_student"]/p[4]/input'
        insert_pw(login_pw_xpath, login_pw)
        time.sleep(1)
        click(login_pw_button)
        time.sleep(2)
        try:
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul/li[1]/a').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul/li[2]/a').click()
            furuderika == 1
            furuderika += 1
            while True:
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="vocabulary_main"]/div/a[1]').click()
                time.sleep(2)
                driver.execute_script('$(`article#step0 li[data-answer="${$("#step0").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step1 li[data-answer="${$("#step1").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step2 li[data-answer="${$("#step2").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step3 li[data-answer="${$("#step3").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step4 li[data-answer="${$("#step4").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step5 li[data-answer="${$("#step5").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step6 li[data-answer="${$("#step6").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step7 li[data-answer="${$("#step7").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step8 li[data-answer="${$("#step8").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step9 li[data-answer="${$("#step9").attr("data-correct") }"]`).click();');time.sleep(3)
                driver.find_element_by_xpath('//*[@id="vocabulary_main"]/div[2]/a[2]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="vocabulary_main"]/div/a[2]').click()
                time.sleep(2)
                driver.execute_script('$(`article#step0 li[data-answer="${$("#step0").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step1 li[data-answer="${$("#step1").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step2 li[data-answer="${$("#step2").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step3 li[data-answer="${$("#step3").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step4 li[data-answer="${$("#step4").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step5 li[data-answer="${$("#step5").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step6 li[data-answer="${$("#step6").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step7 li[data-answer="${$("#step7").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step8 li[data-answer="${$("#step8").attr("data-correct") }"]`).click();');time.sleep(1.5)
                driver.execute_script('$(`article#step9 li[data-answer="${$("#step9").attr("data-correct") }"]`).click();');time.sleep(3)
                driver.find_element_by_xpath('//*[@id="vocabulary_main"]/div[2]/a[2]').click()
        except Exception as e:
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="start-vocabulary-daily-test"]/span').click()
            time.sleep(2)
            driver.execute_script('$(`article#step0 li[data-answer="${$("#step0").attr("data-correct") }"]`).click();');time.sleep(1.5)
            driver.execute_script('$(`article#step1 li[data-answer="${$("#step1").attr("data-correct") }"]`).click();');time.sleep(1.5)
            driver.execute_script('$(`article#step2 li[data-answer="${$("#step2").attr("data-correct") }"]`).click();');time.sleep(1.5)
            driver.execute_script('$(`article#step3 li[data-answer="${$("#step3").attr("data-correct") }"]`).click();');time.sleep(1.5)
            driver.execute_script('$(`article#step4 li[data-answer="${$("#step4").attr("data-correct") }"]`).click();');time.sleep(1.5)
            driver.execute_script('$(`article#step5 li[data-answer="${$("#step5").attr("data-correct") }"]`).click();');time.sleep(1.5)
            driver.execute_script('$(`article#step6 li[data-answer="${$("#step6").attr("data-correct") }"]`).click();');time.sleep(1.5)
            driver.execute_script('$(`article#step7 li[data-answer="${$("#step7").attr("data-correct") }"]`).click();');time.sleep(1.5)
            driver.execute_script('$(`article#step8 li[data-answer="${$("#step8").attr("data-correct") }"]`).click();');time.sleep(1.5)
            driver.execute_script('$(`article#step9 li[data-answer="${$("#step9").attr("data-correct") }"]`).click();');time.sleep(3)
            driver.find_element_by_xpath('//*[@id="vocabulary_main"]/div[2]/a').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul/li[1]/a').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul/li[2]/a').click()
    except Exception as e:
        driver.close()
        driver.quit()
        if furuderika == 5:
            break
import os
os.system('shutdown -h')
