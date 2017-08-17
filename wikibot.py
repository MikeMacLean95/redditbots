#A reddit bot that posts Wikipedia Summary when called
#Created by Michael MacLean /u/krichaelsquad



import praw
import time
import re
import requests
import wikipedia


path = "/home/michael-maclean/workspace/python/redditbots/commented.txt"

footer = "\n | ^I'm ^a ^bot ^created ^by ^u/krichaelsquad |"

def authenitcate():
    print("Authenticating...\n")
    reddit = praw.Reddit('wikibot', user_agent = 'web:wikibot:v0.1 (by /u/krichaelsquad)')
    print("Authenticated as {}\n".format(reddit.user.me()))
    return reddit

def run_wikibot(reddit):
    header=1
    print("Getting 250 comments...\n")

    for comment in reddit.subreddit('test').comments(limit=250):
        match = re.findall("!wikibot [a-zA-Z].*", comment.body)
        if match:
            print("Found in comment with comment ID: " + comment.id)
            file_obj_r = open(path, 'r')

            if comment.id not in file_obj_r.read().splitlines():
                print("Unique link posting comment\n")
                comment.reply(wikipedia.summary(match[0][9:]) + "\n" + footer)
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
        run_wikibot(reddit)

if __name__ == '__main__':
    main()
