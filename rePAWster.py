import praw
import random

dog_subreddits = ["dogpictures",
    "DogsOnHardwoodFloors",
    "DogsWithEyebrows",
    "DogsWearingHats",
    "lookatmydog",
    "dogswearingglasses",
    "woof_irl",
    "BelgianMalinois",
    "bergerbelge",
    "germanshepard",
    "labrador",
    "beagle",
    "DobermanPinscher",
    "CorgiGifs"]

user_agent = "/r/top_dogs submission gathering (by /u/rePAWster)"
num_submissions_to_grab_from_each_dog_subreddit = 25 #use a max of 25 please
num_submissions_to_post_to_my_subreddit_per_iteration= 6 #use a max of 25 please

def check_subreddit_for_submissions(subreddit_name,reddit_obj):
    print(subreddit_name+" is being checked for submissions...")
    subreddit_submissions = subreddit_posts_to_list(reddit_obj,subreddit_name)

    median_karma,min_karma,max_karma = submissions_karma_stats(subreddit_submissions)

    approved_submissions = []

    for submission in subreddit_submissions:
        karma = submission.ups - submission.downs
        if(post_is_good_enough(median_karma,max_karma,min_karma,karma) and is_image_url(submission.url) ):
            approved_submissions.append(submission)

    return approved_submissions

def post_is_good_enough(median_karma,max_karma,min_karma,post_karma):
    return post_karma > median_karma and post_karma > max_karma * 0.7

def is_image_url(url):
    return True

def submit_to_my_subreddit(reddit_obj,submissions):
    print("Submitting links to /r/top_dogs subreddit")
    reddit_obj.login("rePAWster","Hundr3d",disable_warning=True)

    end_iteration = min( num_submissions_to_post_to_my_subreddit_per_iteration, len(submissions)-1 )
    for i in range(0,end_iteration):
        submission = submissions[i]
        posted_successfully = False
        try:
            #submit a cross posted dog picture link to top_dogs subreddit
            new_post = reddit_obj.submit(subreddit="top_dogs",resubmit=False,title=submission.title,url=submission.url)
            posted_successfully = True
            print("Submitted dog picture!")

            #comment the original source on the submission
            try:
                new_post.add_comment("Original: "+submission.permalink)
                print("Submitted comment on post!")
            except Exception as e:
                print("Commenting error")

        except praw.errors.AlreadySubmitted as e:
            print("Link already submitted")
        except Exception as e:
            print("Submission Error")

def subreddit_posts_to_list(reddit_obj,subreddit_name):
    subreddit = reddit_obj.get_subreddit(subreddit_name)
    subreddit_submissions = subreddit.get_hot(limit = num_submissions_to_grab_from_each_subreddit)
    submissions = []
    for submission in subreddit_submissions:
        submissions.append(submission)
    return submissions

def submissions_karma_stats(submissions):
    karma_values = []

    for submission in submissions:
        submission_karma = submission.ups - submission.downs
        karma_values.append(submission_karma)

    karma_values.sort()

    #returns median, min, and max karma values
    return karma_values[int(len(karma_values)/2)], karma_values[0], karma_values[len(karma_values)-1]

def main():
    r = praw.Reddit(user_agent=user_agent)

    all_approved_submissions = []

    for subreddit_name in dog_subreddits:
        approved_submissions = check_subreddit_for_submissions(subreddit_name, r )

        all_approved_submissions = all_approved_submissions + approved_submissions

    random.shuffle(all_approved_submissions)
    submit_to_my_subreddit(r,all_approved_submissions)

if __name__ == "__main__":
    main()
