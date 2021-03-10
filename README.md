# TwitterDataset
Contains the tweets extracted from the Covid-19 twitter dataset for our CMPUT 466 project.

## Description of Dataset

The data is stored in the `data/` folder. Each week is stored separately:
* `data/Jan27-Feb02`: 235512 tweets from the week of January 27 - February 2, 2020.
* `data/Mar 16-Mar22`: 115625 tweets from the week of March 16 - 22, 2020.
* `data/Apr27-May03`: 119419 tweets from the week of April 27 - May 3, 2020.
* `data/Jul6-Jul12`: 543155 tweets from the week of July 6 - 12, 2020.

We appear to be missing five hours of data in the first week (Jan 27-Feb02), but these hours are missing in the original dataset from Chen et. al. too (this was the first week of data collection, during which they experienced power outages).            
       
Tweets from the given week are included only if they:      
1. are not a retweet of another tweet.
2. are not a reply to another tweet.
3. do not contain any media elements (images, URLs).
4. are in English (using a simple dictionary method with a threshold to eliminate likely non-English tweets).

## Tweets

Each `.jsonl` file contains selected fields from the original tweet objects in the following format:
```
 tweet = {"id": tweet_ID,
          "created_at": creation_date,
          "full_text": tweet_text}
```
Each tweet is stored on a separate line of the  file.
