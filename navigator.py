from insta_user_info import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Instagram:
    def __init__(self, username, password):
        self.browserOptions = webdriver.ChromeOptions()
        self.browserOptions.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserOptions)
        self.username = username
        self.password = password
        self.followers = []

    def insta_login(self):
        """
        Logs in to the account with the your input information
        """
        self.browser.get('https://www.instagram.com/accounts/login')
        time.sleep(2)

        username_input = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
        password_input = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(2)

    def get_followers(self):
        """
        Gets the followers of your account or any account which logged in
        """
        self.browser.get(f'https://www.instagram.com/{self.username}')
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        follower_count = len(dialog.find_elements_by_css_selector("li"))

        print(f"first count: {follower_count}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.send_keys(Keys.SPACE).perform()
            action.send_keys(Keys.SPACE).perform()
            time.sleep(1)
            new_count = len(dialog.find_elements_by_css_selector("li"))

            if follower_count != new_count:
                follower_count = new_count
                print(f"Updated Count: {new_count}")
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")
        followers_list =[]
        for follower in followers:
            link = follower.find_element_by_css_selector("a").get_attribute("href")
            followers_list.append(link)

        with open('followers.txt', 'w') as file:
            for user in followers_list:
                file.write(user + "\n")

    def follow_user(self, username):
        """
        Takes the username of the page you want to follow.
        """
        self.browser.get('http://www.instagram.com/' + username)
        time.sleep(2)

        follower_button = self.browser.find_element_by_tag_name('button')
        if follower_button.text != 'Message':
            follower_button.click()
            time.sleep(2)
        else:
            print('You are already following')

    def unfollow_user(self, username):
        """
        Takes the username of the page you want to unfollow.
        """
        self.browser.get('http://www.instagram.com/' + username)
        time.sleep(2)

        following_button = self.browser.find_element_by_css_selector('.vBF20 button')
        if following_button:
            following_button.click()
            time.sleep(2)
            self.browser.find_element_by_xpath("//button[text()='Unfollow']").click()
        else:
            print('You are not following this user')


insta = Instagram(username, password)


if __name__ == '__main__':
    insta.insta_login()
    insta.get_followers()
    insta.follow_user('kod_evreni')  # this method should take the username of the page
    insta.unfollow_user('kod_evreni')  # this method should take the username of the page
