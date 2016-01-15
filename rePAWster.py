import praw
import random
import time
import sched
from datetime import datetime, timedelta

dog_subreddits = {"dogpictures":100,
    "DogsOnHardwoodFloors":20,
    "DogsWithEyebrows":50,
    "DogsWearingHats":50,
    "lookatmydog":75,
    "dogswearingglasses":7,
    "woof_irl":80,
    "BelgianMalinois":20,
    "bergerbelge":25,
    "germanshepard":15,
    "labrador":50,
    "beagle":40,
    "DobermanPinscher":30,
    "CorgiGifs":100}

user_agent = "/r/top_dogs submission gathering (by /u/rePAWster)"
num_submissions_to_grab_from_each_dog_subreddit = 25 #use a max of 25 please

def check_subreddit_for_submissions(subreddit_name,reddit_obj):
    print("/r/"+subreddit_name+" is being checked for submissions...")
    subreddit_submissions = subreddit_posts_to_list(reddit_obj,subreddit_name)

    approved_submissions = []

    for submission in subreddit_submissions:
        karma = submission.ups - submission.downs
        if(post_is_new_enough(submission.created) and post_is_good_enough(subreddit_name,karma) and is_image_url(submission.url) ):
            approved_submissions.append(submission)

    return approved_submissions

def post_is_new_enough(creation_time):
    submission_creation_datetime = datetime.fromtimestamp(creation_time)
    cutoff = datetime.now() - timedelta(days=7)
    return submission_creation_datetime > cutoff

def post_is_good_enough(subreddit_name,post_karma):
    return post_karma > dog_subreddits[subreddit_name]
"""
def post_is_good_enough(median_karma,max_karma,min_karma,post_karma):
    return post_karma > median_karma and post_karma > max_karma * 0.7

def karma_stats(submissions):
    karma_values = []

    for submission in submissions:
        submission_karma = submission.ups - submission.downs
        karma_values.append(submission_karma)

    karma_values.sort()

    #returns median, min, and max karma values
    return karma_values[int(len(karma_values)/2)], karma_values[0], karma_values[len(karma_values)-1]

"""
def is_image_url(url):
    return True

def submit_to_my_subreddit(reddit_obj,submissions):
    print("Submitting "+str(len(submissions))+" links to /r/top_dogs subreddit")
    reddit_obj.login("rePAWster","Hundr3d",disable_warning=True)

    while(len(submissions)>0 ):
        submission = submissions[0]

        try:
            #submit a cross posted dog picture link to top_dogs subreddit
            new_post = reddit_obj.submit(subreddit="top_dogs",resubmit=False,title=submission.title,url=submission.url)
            print("Submitted dog picture!")

            #comment the original source on the submission
            try:
                new_post.add_comment("Original: "+submission.permalink)
                print("Submitted comment on post!")
            except Exception as e:
                print(str(e))

        except Exception as e:
            print(str(e))

        del submissions[0]

    return

def subreddit_posts_to_list(reddit_obj,subreddit_name):
    subreddit = reddit_obj.get_subreddit(subreddit_name)
    subreddit_submissions = subreddit.get_hot(limit = num_submissions_to_grab_from_each_dog_subreddit)
    submissions = []
    for submission in subreddit_submissions:
        submissions.append(submission)
    return submissions

def find_and_submit_posts():
    r = praw.Reddit(user_agent=user_agent)

    all_approved_submissions = []
    try:
        for subreddit_name in dog_subreddits:
            approved_submissions = check_subreddit_for_submissions(subreddit_name, r )

            all_approved_submissions = all_approved_submissions + approved_submissions

        random.shuffle(all_approved_submissions)
        submit_to_my_subreddit(r,all_approved_submissions)
    except Exception as e:
        print("Exception! ")
        print("")
        print(str(e))
        print("")
        print("Will retry after short rest")

        time.sleep(60)#1 min
        find_and_submit_posts()

def main():
    #while(True):
    find_and_submit_posts()

    print("Finished! Entering rest period...")
    #time.sleep(60 * 60 * 3) #3hrs


if __name__ == "__main__":
    main()
