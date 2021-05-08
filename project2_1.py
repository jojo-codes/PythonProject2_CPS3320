import random
import tweepy
from random_words import RandomWords
from PyDictionary import PyDictionary

import credential

auth = tweepy.OAuthHandler(credential.CONSUMER_KEY, credential.CONSUMER_SECRET)
auth.set_access_token(credential.ACCESS_TOKEN, credential.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def random_word():
    dictionary = PyDictionary()
    rw = RandomWords()

    word = rw.random_word()
    definitions = dictionary.meaning(word)

    try:
        part_of_speech = random.choice(list(definitions.keys()))
        definition = random.choice(definitions[part_of_speech])
    except:
        return "NULL_DEFINITION"

    return {
        "word": word,
        "definition": definition,
        "part-of-speech": part_of_speech
    }


daily_word = random_word()

while daily_word == "NULL_DEFINITION":
    daily_word = random_word()

daily_word = f'Today\'s #dailyWord is \'{daily_word["word"]}\'. It means \'{daily_word["definition"]}\' as a {daily_word["part-of-speech"]}'

api.update_status("This tweet is using Tweepy API\n" + daily_word)
