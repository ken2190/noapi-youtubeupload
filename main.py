#!/usr/bin/env  python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # keys
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebElement     # send_keys
import time

def drag_and_drop_file(drop_target, path):
    driver = drop_target.parent
    file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
    file_input.send_keys(path)


def google_login(driver):
    driver.get("https://accounts.google.com/signin")
    time.sleep(4)

    JS_DROP_FILE = """
        var target = arguments[0],
            offsetX = arguments[1],
            offsetY = arguments[2],
            document = target.ownerDocument || document,
            window = document.defaultView || window;

        var input = document.createElement('INPUT');
        input.type = 'file';
        input.onchange = function () {
          var rect = target.getBoundingClientRect(),
              x = rect.left + (offsetX || (rect.width >> 1)),
              y = rect.top + (offsetY || (rect.height >> 1)),
              dataTransfer = { files: this.files };

          ['dragenter', 'dragover', 'drop'].forEach(function (name) {
            var evt = document.createEvent('MouseEvent');
            evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
            evt.dataTransfer = dataTransfer;
            target.dispatchEvent(evt);
          });

          setTimeout(function () { document.body.removeChild(input); }, 25);
        };
        document.body.appendChild(input);
        return input;
    """

    drag_and_drop_file(JS_DROP_FILE, "/home/logger69/.bashrc")
    

    action = webdriver.ActionChains(driver)

    # find input bar and enter the email address
    input_bar = driver.find_element(By.CSS_SELECTOR, ".whsOnd.zHQkBf")
    action.move_to_element(input_bar)
    action.send_keys('keysworld')
    action.send_keys(Keys.ENTER)
    action.perform()

    time.sleep(3)

    pass


def main():
    # add options for incognito
    options = webdriver.FirefoxOptions()
    options.add_argument("--private-window")

    driver = webdriver.Firefox(options=options)

    # login to google account
    google_login(driver)

    time.sleep(5)
    driver.close()

if __name__ == "__main__":
    main()
