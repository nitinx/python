import json
import csv

file_src = 'twitter_dump_trend.json'
file_tgt = 'twitter_dump_trend.csv'
cnt = 0
fieldnames = ['id', 'created_at', 'quote_count', 'reply_count', 'retweet_count', 'favorite_count', 'favorited',
              'retweeted', 'filter_level', 'geo', 'place', 'coordinates', 'lang', 'source', 'text']

# Open file to write
with open(file_tgt, 'w', newline='\n', encoding='utf-8') as line_write:
    writer = csv.DictWriter(line_write, delimiter="|", fieldnames=fieldnames, restval='NA', quoting=csv.QUOTE_ALL,
                            extrasaction='ignore')
    writer.writeheader()

    for line in open(file_src, 'r', encoding='utf-8'):
        tweet_read = json.loads(line)
        #print(tweet_read)

        cnt += 1
        if cnt > 10000:
            break
        elif cnt % 100 == 0:
            print(cnt)

        tweet_write = tweet_read
        tweet_write['text'] = str(tweet_write['text']).replace('\n', ' ')
        writer.writerow(tweet_write)
