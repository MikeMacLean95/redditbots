#A reddit bot that tells Todd to clean up his shit
#Created by Michael MacLean /u/krichaelsquad



import praw
import time
import re
import requests


path = "/home/michael-maclean/workspace/python/redditbots/commented.txt"

headera = "***Clean up Your Shit***\n"
headerb = "***Shut up Todd***\n"

header = 1
footer = "\n | ^I'm ^a ^bot ^created ^by ^u/krichaelsquad |"

def authenitcate():
    print("Authenticating...\n")
    reddit = praw.Reddit('bojackbot', user_agent = 'web:bojackbot:v0.1 (by /u/krichaelsquad)')
    print("Authenticated as {}\n".format(reddit.user.me()))
    return reddit

def run_bojackbot(reddit):
    header=1
    print("Getting 250 comments...\n")

    for comment in reddit.subreddit('bojackhorseman').comments(limit=250):
        if "Hey Todd!" in comment.body:
            print("Found in comment with comment ID: " + comment.id)
            file_obj_r = open(path, 'r')

            if comment.id not in file_obj_r.read().splitlines():
                print("Unique link posting comment\n")
                if (header == 1):
                        comment.reply(headera + footer)
                        header= 2
                else:
                        comment.reply(headerb + footer)
                        header = 1
                file_obj_r.close()

                file_obj_w = (open(path, 'a+'))
                file_obj_w.write(comment.id + "\n")
                file_obj_w.close()
            else:
                print("Already visited link...No reply needed\n")
        time.sleep(0)
    print("Waiting 60 seconds...\n")
    time.sleep(60)

def main():
    reddit = authenitcate()
    while True:
        run_bojackbot(reddit)

if __name__ == '__main__':
    main()
