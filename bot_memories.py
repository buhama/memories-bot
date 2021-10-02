import tweepy
import time
from datetime import date
from datetime import datetime
import threading
import random

consumer_key = 'JmDnFKsVJw9LPccF3iqsEiStr'
consumer_secret = 'Zw0CzyVidhKOxUbR1WU66Z5U1neUYoKhCfug9GYM9asPexKeNJ'

key = '1398511905308807168-LVgxXvpZVMbQijEQTvyimc3b3mPqO6'
secret = 'D0NoJiDwlMOawqPKKnlOyeKPvnzPq4MsYXjd9QtFgXMx7'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

randomid = 123
counter = 0


#print ("we're running")

#hassan
hassan_id = '1014703295569514496'
#ibrahim
ibrahim_id = '912846179154743296'
#ashley
ashley_id = '598643573'
#monisah
monisah_id = '705457648'

#8 hours right now
secondsInADay = 28800

messages = ["Hey, here are your Twitter memories for today! Hopefully not too cringe. Message STOP to stop receiving these... jk that's not real, just message Hassan.",
            "FriEND, best friEND, grilfriEND, boyfriEND -- everything has an end -- except memories, memories are forever. Here are some of your worst from today: ",
            "What's up, hope you're having a great day and theses memories from today don't ruin it: ",
            "It's honestly a mircale that this bot is working, but here are your memories from today (hopefully): ",
            "Everytime you make a tweet, think about how embarassing it's going to be for you in the next 5 years, but for now here are some embarassing tweets from your past: ",
            "One day this bot will stop doing it's thing and no one will fix it, and that's a sad thought. Until then, here are your memories: ",
            "Imagine in the future I send you an actual pigeon, to your house, with real life memories that it transfers to your brain. For now here are your twitter memories: ",
            "Remember, nothing is important, we'll all die, there is no use dwelling in the past. BUT if you want to, here's some tweets to help you out: ", 
            "The past can hurt. But the way I see it, you can either run from it, or learn from it - Rafiki", 
            "Remember, everything you tweet, every single thought you put on the internet can be traced back to you and ruin your life forever. For example here are your twitter memories: ",
            "We live in world where telling people your every thought, accomplishment, life event, sad moments is normal. Like your tweets here: ",
            "Tweet less, consume less, chill more. Look at these memories and then log off: ",
            "In a perfect world, Twitter doesn't exist. But still it would be sad to lose all your memories on here. Like these tweets: ",
            "Social media is a vault of all the things we've thought worthy of sharing with the world. Which is kinda cool, kinda sad. Here is something from that vault: ",
            "Cowabunga, here are your twitter memories: ",
            "One day if the robot overlords take over, Cher Ami, I believe, will be one of the good ones. Still giving you your twitter memories, like the following: ",
            "We all know that being on social media is bad, yet here we are. Anyways, here are your twitter memories"]


# def set_interval(runBot, secondsInADay):
#     def func_wrapper():
#         set_interval(runBot, secondsInADay)
#         runBot()
#     t = threading.Timer(secondsInADay, func_wrapper)
#     t.start()
#     return t

def sendStatus():
    randomMessageForHassan = random.randint (0,16)
    api.send_direct_message(hassan_id, messages[randomMessageForHassan])
    api.send_direct_message(hassan_id, counter)


def runBot():
    print ("started run")

    global counter
    global hassan_id
    global ibrahim_id
    global ashley_id
    global monisah_id

    counter+=1
    print (counter)
    time.sleep(60)

    if (counter == 1440):
        randomMessageForHassan = random.randint (0,16)
        api.send_direct_message(hassan_id, messages[randomMessageForHassan])
        sendMemories (hassan_id)
        sendMemories (ibrahim_id)
        sendMemories (ashley_id)
        sendMemories (monisah_id)
        counter = 0
    return


def sendMemories (userID):
    #Get User
    user = api.get_user(userID)
    totalStatuses = user.statuses_count

    #Get today's date with and without the year and convert to string
    today = date.today()
    today = today.strftime("%m-%d")

    today_with_year = date.today()
    today_with_year = today_with_year.strftime("%Y-%m-%d")

    #Used to alter date for testing
    #today = "06-20"
    #today_with_year = '2021-06-20'

    match = 0
    #counter = 0

    tweets = tweepy.Cursor(api.user_timeline, userID).items(totalStatuses)
    for tweet in tweets:
            try:

                #counter = counter + 1
                #print (counter)

                #Get tweet URL
                #url = f"https://twitter.com/user/status/{tweet.id}"
                url = "https://twitter.com/user/status/" + str(tweet.id)

                #Get tweet date with and without year and convert to string
                tweetDate = tweet.created_at.strftime("%m-%d")
                tweetDate_with_year = tweet.created_at.strftime("%Y-%m-%d")

                #If todays date is equal to todays date
                if today == tweetDate:

                    #If the year is not also the same , then we have a match
                    if today_with_year != tweetDate_with_year:

                        #We haven't had a match yet so give the initial message
                        if match == 0:
                            randomMessage = random.randint (0,16)
                            api.send_direct_message(userID, messages[randomMessage])
                            match = 1

                        api.send_direct_message(userID, url)

            except tweepy.TweepError as e:
                print(e.reason)
                #time.sleep(15)

#set_interval(runBot, secondsInADay)


sendMemories (hassan_id)
sendMemories (ashley_id)
sendMemories (ibrahim_id)
sendMemories (monisah_id)


while True:
    try:
        runBot()
    except:
        print ("bot crashed")


