# RePAWster

RePAWster is a Reddit bot utilizing [PRAW](https://praw.readthedocs.org/en/stable/) that reposts top rated pictures of dogs from various active dog subreddits to [/r/top_dogs](https://www.reddit.com/r/top_dogs).  Subreddits utilized are:

* [/r/dogpictures](https://www.reddit.com/r/dogpictures)
* [/r/DogsOnHardwoodFloors](https://www.reddit.com/r/DogsOnHardwoodFloors)
* [/r/DogsWithEyebrows](https://www.reddit.com/r/DogsWithEyebrows)
* [/r/DogsWearingHats](https://www.reddit.com/r/DogsWearingHats)
* [/r/lookatmydog](https://www.reddit.com/r/lookatmydog)
* [/r/dogswearingglasses](https://www.reddit.com/r/)
* [/r/woof_irl](https://www.reddit.com/r/woof_irl)
* [/r/BelgianMalinois](https://www.reddit.com/r/BelgianMalinois)
* [/r/bergerbelge](https://www.reddit.com/r/bergerbelge)
* [/r/germanshepard](https://www.reddit.com/r/germanshepard)
* [/r/labrador](https://www.reddit.com/r/labrador)
* [/r/beagle](https://www.reddit.com/r/beagle)
* [/r/DobermanPinscher](https://www.reddit.com/r/DobermanPinscher)
* [/r/CorgiGifs](https://www.reddit.com/r/CorgiGifs)

'Top-rated' pictures are manually defined for each subreddit. To find the karma cutoffs I guesstimated for each feeder subreddit such that approximately 1/4 of the best submissions should be cross-posted each run of the bot. PRAW/Reddit have a system for checking duplicate links, so if a link has been submitted to [/r/top_dogs](https://www.reddit.com/r/top_dogs) recently it will be auto filtered without completing.

The bot runs a on an Ubuntu virtual server with [Digital Ocean](https://www.digitalocean.com/). The script runs periodically every day using [Cron](https://en.wikipedia.org/wiki/Cron).
