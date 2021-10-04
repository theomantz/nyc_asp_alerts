# New York City Alternate Side Parking Twitter Bot

## Description:
There is a whole lot of things to keep track of when living in New York. One of them is the various holidays which (fortunately) suspend street sweeping. This project aims to take away at least one concern for street parking drivers in New York. 

This project is a simple Twitter bot written in Python which uses the Tweepy package to interact with the Twitter API. The bot then runs twice daily in a Docker container image on an AWS EC2 instance. Each time it runs it pulls all of the recent tweets of the @NYCASP twitter account from the Twitter API, iterates over the recent tweets, and if the tweet was tweeted today, contains the word "suspended", and has not been retweeted by our bot already, the bot will retweet it. This allows Twitter users to follow the bot, turn on tweet notifications and only get alerts for @NYCASP tweets which impact them.

## Getting Started:

First things first you will want to clone the project locally.

```sh
git clone git@github.com:theomantz/nyc_asp_alerts.git
```

Once the project has been cloned `cd` into the project directory and ensure you have `venv` set up.

```sh
python -m pip install --user virtualenv
```
Set up the virtual environment.

```sh
python -m venv venv
```

Activate the virtual environment.

```sh
. venv/bin/activate
```

Install dependencies.

```sh
pip install -r requirements.txt
```

At this point you will need a Twitter developer account to continue. Go to https://developer.twitter.com/en/apply-for-access 

Once you have a Twitter developer account you will need to populate a `.env` file in the root of the project directory with the following information.

```py
twitter_api_key=<your_api_key>
twitter_api_secret=<your_api_secret>
twitter_access_token=<your_access_token>
twitter_access_token_secret=<your_access_token_secret>
```

Once that information is provided in your `.env` file you can run the bot

```py
python bot.py
```

If you would like to create a Docker container image to run on a server.

```sh
docker build . -t nyc_asp_alerts
```

Then you can `ssh` to a remote server, upload and extract the image, and set it to run with a `cronjob` or continuously.