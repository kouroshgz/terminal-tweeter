import tweepy


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
    functions = ["(A) Tweet"]
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


funcDict = {'A': pushTweet, }


def main():
    funcDict[intro()]()


main()
