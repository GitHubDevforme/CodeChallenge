#!/usr/bin/python
# 
import sys


"""
This Script writes to a file the running median of total number of unique words in each tweets.
The number represents the median after each processed tweet.
You must supply location of the tweet file and the output file as arguments.
example: median_unique.py tweet.txt output.txt
"""

# Get the total number of args passed to the demo.py
total_arg = len(sys.argv)
if total_arg < 3:
    print (' You must supply 2 arguments to the words_tweeted.py.')
    print (' Please supply an input and output file name.')
 
while total_arg == 3:
    
    # Get the arguments list 
    cmdargs = sys.argv
    # Print it
    """print ("\n The total numbers of args passed to the script: %d " % total_arg)
    print ("Args list: %s " % cmdargs)
    print ("new args : %s " % cmdargs[0])
    #print ("Frist args: %s " % str(sys.argv[0]))
    #print ("Scond Args : %s " % indatafile)
    #print ("Third Args : %s " % outdatafile)"""
    total_arg = 2
     
    try:
        tweet_count = 0
        tot_words = 0
        # Open input and output file for process count unique words in tweets
        with open(cmdargs[1], 'r') as f_in, open(cmdargs[2], 'w') as f_out:
             for x in f_in:
                mylist1=[]
                tweet_count = tweet_count + 1
                mylist1 = x.split()
                mylist1.sort()
                x2 = mylist1[0]
                counter = 1
                for x in mylist1:
                    if x2 != x:
                        counter = counter + 1
                        x2 = x
                tot_words = tot_words + counter
                medi_tot = tot_words / float(tweet_count)
                s = '{:.2f}'.format(medi_tot) + "\n"
                f_out.write(s)
        f_in.close()
        f_out.close()
    except (IOError, NameError) as err:
        print ('Problem access your file: ' + str(err))
        f_in.close()
        f_out.close()
        break
