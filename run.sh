#!/bin/bash
#
# This script is for running two python script to output word count and running median in tweets.
# The python scripts are in the src directory.
# Input file is in tweet_input directory and output files are in the tweet_output directory

python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt

