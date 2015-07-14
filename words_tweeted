#!/usr/bin/python
# 
import sys

"""
This Script writes to a file the total count of unique words in the tweets file.
The output contains each unique word with its total count.
You must supply location of the tweet file and the output file as arguments.
example: median_unique.py tweet.txt output.txt
"""

mylist1=[]
mylist2=[]
tweets_counter = 0
max_tweets = 20000 # set this number to procees at group of tweets and out put to report. the group will stop at 1 less than this number.
running_counter = 0
start_from = 1
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
    # Open input file and process tweets
    try:
        with open(cmdargs[1], 'r') as f_in, open(cmdargs[2], 'w') as f_out:
            for x in f_in:
                running_counter = running_counter + 1
                tweets_counter = tweets_counter + 1
                if tweets_counter < max_tweets:
                    mylist2 = x.split()
                    mylist1 = mylist1 + mylist2
                else:
                    s = "\n\n tweets from: " + '{:10d}'.format(start_from) + " to " + '{:10d}'.format(running_counter - 1) + "\n\n"
                    f_out.write(s)
                    mylist1.sort()
                    x2 = mylist1[0]
                    counter = 0
                    for x3 in mylist1:
                        if x2 != x3:
                            s = '{:<30}'.format(x2) + "\t" + '{:3d}'.format(counter) + "\n"
                            f_out.write(s)
                            x2 = x3
                            counter = 1
                        else:
                            counter = counter + 1
                    s = '{:<30}'.format(x2) + "\t" + '{:3d}'.format(counter) + "\n"
                    f_out.write(s)
                    start_from = running_counter
                    mylist1 = []
                    mylist2 = x.split()
                    mylist1 = mylist1 + mylist2
            s = "\n\n tweets from: " + '{:10d}'.format(start_from) + " to " + '{:10d}'.format(running_counter) + "\n\n"
            f_out.write(s)
            mylist1.sort()
            x2 = mylist1[0]
            counter = 0
            for x3 in mylist1:
                if x2 != x3:
                    s = '{:<30}'.format(x2) + "\t" + '{:3d}'.format(counter) + "\n"
                    f_out.write(s)
                    x2 = x3
                    counter = 1
                else:
                    counter = counter + 1
            s = '{:<30}'.format(x2) + "\t" + '{:3d}'.format(counter) + "\n"
            f_out.write(s)
        f_in.close()
        f_out.close()
    except (IOError, NameError) as err:
        print ('Problem access your file: ' + str(err))
        f_in.close()
        f_out.close()
        break
        
