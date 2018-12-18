import json
import csv

file_src = 'twitter_dump_trend.json'
file_tgt = 'twitter_dump_trend.csv'
tweet_write = []

# Open file
for line in open(file_src, 'r', encoding='utf-8'):
    tweet_read = json.loads(line)
    #print(tweet_read)

    with open(file_tgt, 'w', newline='', encoding='utf-8') as line_write:
        writer = csv.writer(line_write, delimiter="|", quoting=csv.QUOTE_ALL)

        tweet_write.append(tweet_read['created_at'])
        tweet_write.append(tweet_read['id'])
        tweet_write.append(tweet_read['retweet_count'])
        tweet_write.append(tweet_read['favorite_count'])
        tweet_write.append(tweet_read['filter_level'])
        tweet_write.append(tweet_read['geo'])
        tweet_write.append(tweet_read['place'])
        tweet_write.append(tweet_read['coordinates'])
        tweet_write.append(str(tweet_read['lang']).encode('utf-8'))
        tweet_write.append(str(tweet_read['text']).encode('utf-8'))
        print(tweet_write)
        writer.writerow(tweet_write)

        '''try:
            tweet_write.append(str(tweet_read['lang']).encode('utf-8'))
            tweet_write.append(str(tweet_read['text']).encode('utf-8'))
            print(tweet_write)
            writer.writerow(tweet_write)
        except:
            print("exception occurred!!")'''
