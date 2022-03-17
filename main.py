import undetected_chromedriver
import time

if __name__ == '__main__':
    try:
        driver = undetected_chromedriver.Chrome()
        # driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
        q = driver.get("https://pikabu.ru")
        time.sleep(10)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
