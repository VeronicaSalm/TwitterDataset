import argparse
import json
import os
import sys
import csv

# Argparse for input json file, must be unzipped!
parser = argparse.ArgumentParser(description="Generates tweet files for tweets matching the given criteria.")

# Note: it's expected that all tweets from start date to end date are in the given input folder
parser.add_argument("input_path",
                    help="The input folder containing the unzipped .jsonl tweet files",
                    type = str)

tweet_count = 0

def process_tweet_file(fpath):
    """
    Arguments: 
        fpath: path to .jsonl file to process

    Returns:
        None, but updates a global variable
    """
    global tweet_count
    with open(fpath, "r") as json_file:
        print("Processing '{}'...".format(fpath))
        line = json_file.readline()

        while line:
            tweet_count += 1 
            # read the next line of file
            line = json_file.readline()

if __name__ == "__main__":
    args = parser.parse_args()

    if os.path.isdir(args.input_path):
        for f in sorted(os.listdir(args.input_path)):
            fpath = os.path.join(args.input_path, f)
            process_tweet_file(fpath)
    else:
        print("The input path argument must be a valid directory.")

    print("Done processing all provided tweets.")

    print(f"Found {tweet_count} total tweets.")
