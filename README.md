# RePAWster

Reddit bot to repost top rated pictures of dogs from various active subreddits to a custom subreddit. Subreddits utilized are:

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

'Top-rated' pictures are manually defined for each subreddit. Essentially I looked at the subreddits, guesstimated what the cutoff would need to be for each subreddit, and manually defined it. PRAW/Reddit have a system for checking duplicate links, so if links are caught twice they will be auto filtered without completing submission.

The bot runs a on an Ubuntu virtual server with [Digital Ocean](https://www.digitalocean.com/). The script runs periodically every day using [Cron](https://en.wikipedia.org/wiki/Cron).
