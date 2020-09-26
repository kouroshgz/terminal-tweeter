# terminal-tweeter
Twitter on your terminal.  

Python 3, Tweepy

# Requirements:
Usage of the twitter API requires a Twitter Developer account.

### Creating a Twitter Developer account:
1. [Create a Twitter Developer account](https://developer.twitter.com/en/apply)  
  You will need to explain who you are, why you are applying for a twitter developer account, and what you intend to do with the twitter API.

2. Wait for Twitter to review and confirm your Twitter Developer Account.

### Getting the required information:
Usage of this script requires certain sensitive information from your twitter developer account. It is reccomended to store this information somewhere private and secure.

**To access the required information:**  
    1. Log into your developer dashboard  
    2. Under projects and apps, create a new app.  
    3. Give your app __**Read and Write**__ Permissions  
    4. Navigate to the __**keys and tokens**__ page  
    5. View and copy your **API Key**, your **API Secret Key**, your **Acess Token** and your **Secret Access Token**  

You will need to edit the script and paste those keys into the required variables.  
In the script, the API keys will need to placed in the corresponding "consumer_key" and "consumer_secret" variables.

# Usage

When the script is ran, the user will be presented with an options menu.  
Input the key that corresponds to the function you wish to call.  

Currently, only the pushTweet function has been implemented, which will post a Tweet on your timeline.  
