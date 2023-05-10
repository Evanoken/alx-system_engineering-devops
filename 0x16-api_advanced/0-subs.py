#!/usr/bin/python3
import requests
import argparse

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "myBot/0.0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the number of subscribers for a subreddit")
    parser.add_argument("subreddit", type=str, help="The name of the subreddit")
    args = parser.parse_args()

    subscribers = number_of_subscribers(args.subreddit)
    print("{} has {} subscribers".format(args.subreddit, subscribers))

