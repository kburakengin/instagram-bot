# instagram-bot -v1
 Instagram Bot which is able to get the username and password and log in. It navigates to user's page and gets all the followers' URLs and puts them into a ﬁle. 
 It`s also able to take in a username and automatically follow the user associated with that username, if not already followed. If the proﬁle is followed, it can also automatically unfollow that page

## Install guide

##### Clone the repo

```bash
$ git clone https://github.com/Kburak/instagram-bot.git
$ cd instagram-bot
```
##### Create the virtualenv and activate it
```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

##### Or on Windows cmd::
```bash
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```

##### Install dependencies
```bash
$ pip install -r requirements.txt
```

#### Download the Chrome Webdriver and move it to project folder:
```bash
https://chromedriver.chromium.org/downloads
```

##### Run the app
```bash
$ python navigator.py
```
