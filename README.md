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

Then activate the virtual environment.

```sh
. venv/bin/activate
```

Then install dependencies.

```sh
pip install -r requirements.txt
```


