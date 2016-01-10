import praw

dog_subreddits = ["dogpictures"]

"""
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
"""

user_agent = "/r/top_dogs submission gathering (by /u/rePAWster)"

def check_subreddit_for_submissions(subreddit_name,reddit_obj):
    print(subreddit_name+" is being checked for submissions...")
    subreddit_submissions = subreddit_posts_to_list(reddit_obj,subreddit_name)

    median_karma,min_karma,max_karma = submissions_karma_stats(subreddit_submissions)

    approved_submissions = []

    for submission in subreddit_submissions:
        karma = submission.ups - submission.downs
        if(karma > median_karma and is_image_url(submission.url) ):
            approved_submissions.append(submission)

    return approved_submissions

def is_image_url(url):
    return True

def submit_to_my_subreddit(reddit_obj,submissions):
    print("Submitting links to /r/top_dogs subreddit")
    reddit_obj.login("rePAWster","Hundr3d",disable_warning=True)

    for submission in submissions:
        new_post = reddit_obj.submit(subreddit="top_dogs",resubmit=False,title=submission.title,url=submission.url)
        new_post.add_comment("Original: "+submission.permalink)
        print("submitted!")

def subreddit_posts_to_list(reddit_obj,subreddit_name):
    subreddit = reddit_obj.get_subreddit(subreddit_name)
    subreddit_submissions = subreddit.get_hot(limit=10)
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

    for subreddit_name in dog_subreddits:
        approved_submissions = check_subreddit_for_submissions(subreddit_name, r )

        submit_to_my_subreddit(r,approved_submissions)

if __name__ == "__main__":
    main()
