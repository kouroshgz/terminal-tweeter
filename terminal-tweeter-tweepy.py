import tweepy
import sys


consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
print(api.me().name)


def intro():
    print("TERMINAL-TWEETER: A CLI TWITTER INTERFACE")
    print("FUNCTIONS: ")
    functions = ["(A) Tweet", "(B) Get Timeline", "(C) Get Someone Elses Tweets", "(Q) Exit"]
    for i in functions:
        print(i)
    command = input("What would you like to do?")
    if command.isalpha():
        return command.upper()
    else:
        print("Error: Input must match presented options")
        intro()


def pushTweet():
    tweet = input("Enter Tweet: ")
    tweetLength = len(tweet)
    if tweetLength > 280:
        print("ERROR! MAX CHAR COUNT IS 280!")
    else:
        try:
            if api.update_status(tweet):
                print("SUCCESS")
        except tweepy.error.TweepError as e:
            print(e)

def getTimeline():
     number_of_tweets = input("How many Tweets?")
     for status in tweepy.Cursor(api.home_timeline,tweet_mode="extended", exclude_replies= True).items(int(number_of_tweets)):
        print(status.user.screen_name)
        print(status.id)
        print(status.full_text)
        print("\n")

def getUserTimeline():
    username= input("Enter username: (ex: @twitter ) ")
    number_of_tweets = input("How many Tweets?")
    for status in tweepy.Cursor(api.user_timeline, screen_name = username, tweet_mode="extended", exclude_replies= True).items(int(number_of_tweets)):
        print(status.user.screen_name)
        print(status.id)
        print(status.full_text)
        print("\n")

def exit():
    sys.exit();

funcDict = {'A': pushTweet, 'B': getTimeline, 'C' : getUserTimeline, 'Q' : exit }


def main():
    repeat = True;
    while repeat:
        funcDict[intro()]()


main()
