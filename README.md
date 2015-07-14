# Coding Challenge for Insight Data    Engineering

These codes are to read in a text file that contain tweets and produce two files. The frist one counts the total number of each unique word that receive from tweets. The second is to output a running median. The codes are written with python and tested on a mac. 

Here are the files used in this challenge:

 * tweets.txt - contain sample tweets.
 * run.sh - executable script that runs both python codes.
 * words_tweeted.py and median_unique.py are the two python code created by me.

And here's run.sh example

```javascript
#!/bin/bash
#
# This script is for running two python script to output word count and running median in tweets.
# The python scripts are in the src directory.
# Input file is in tweet_input directory and output files are in the tweet_output directory

python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt
```

# Tests

Each code first created and tested on Window, then tested on a Mac using a shell script "run.sh". Results were check and verify for accuracy.

note: run.sh might not run in all system.

# outputs

```javascript
first code output - count the total number each unique word in tweets:

 tweets from:          1 to          3

\#analytics                    	  1
\#bigdata                      	  3
\#kdn                          	  1
\#smb                          	  1
@cxotodayalerts               	  1
@lavanyarathnam               	  1
and                           	  1
answer                        	  1
astrazeneca                   	  1
being                         	  1
big                           	  2
business.                     	  1
businesses:                   	  1
data                          	  1
deployed                      	  1
effective                     	  1
end                           	  1
finally                       	  1
for                           	  2
healthcare                    	  1
how                           	  1
http://bddy.me/1bzukb3        	  1
http://ow.ly/o8gt3            	  1
http://ow.ly/ot2uj            	  1
interview:                    	  1
is                            	  3
just                          	  1
not                           	  1
of                            	  1
on                            	  2
poverty?                      	  1
promise                       	  1
small                         	  1
the                           	  2
to                            	  1
wang,                         	  1
xia                           	  1


scond code output - running median:

11.00
12.50
14.00
...
