FROM python:3.9

COPY bot.py ./
COPY tweet_test.py ./
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR ./
CMD ["python3", "bot.py"]