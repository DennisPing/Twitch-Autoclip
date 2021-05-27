# twitch-autoclip
Analyze Twitch chat logs to extract Twitch hightlights. Uses ML prediction model and common sense emote tracking.

## Three Problems
1. **Twitch streams are very long and people don't have enough time to watch their favorite streamers.**
2. **Twitch streams are so long that streamers need to hire an editor or reduce their own streaming time to edit videos themselves.**
3. **If streamers do not edit their videos, someone else (usually within a week) will edit the videos and upload them onto their own YouTube channel.**

## The Audience's Perspective :tv:
**If I miss a stream, what are my options?**
  1. Randomly click through a 6 hour long VOD.
  2. Watch Twitch clips which (1) have no sorting algorithm, (2) are made by random people, (3) are often lacking substanial content, and (4) are given nonsensical titles.
  3. Wait until someone uploads a YouTube highlight video.

## The Streamer's Perspective :movie_camera:
**After I stream and entertain an audience for 6 hours straight, what are my options?**
  1. Grind more and edit videos because who needs rest.
  2. Hire a video editor for $50/hour.
  3. Go rest and stream tomorrow (and repeat).

## The chicken and the egg problem :hatching_chick:
Large streamers (over 5000 avg viewers) can afford to hire a full time video editor. They have an existing Twitch audience who craves content, the video editor produces content quickly, and the YouTube algorithm picks up on that interest and introduces new viewers to that streamer.

However, small to medium sized streamers (200 to 2000 avg viewers) cannot utilize the YouTube algorithm to compound any growth. Paying an editor $50/hour will bankrupt them if the YouTube algorithm does not pick them up. On the other hand, spending time to edit videos themselves will cut the amount of **available content** actually being produced.

Unfortunately, very small streamers have do not have a sizeable audience to warrant rapid video production. :sweat: They need to focus on gaining viewers on one platform first. There is an insufficient amount of chat messages.

## Why Autoclip is important :heavy_check_mark:
Many media platforms have already implemented some sort of highlighting feature:
1. [Soundcloud](https://soundcloud.com/discover/sets/charts-top:pop:us): Soundcloud graphs its user comments over time so you know how a song plays BEFORE you ever listen to it. You know when the verse occurs and when the chorus pops off.
![soundcloud-graph](https://i.imgur.com/CseTog0.png)
2. [YouTube chapters](https://www.youtube.com/watch?v=93M1l_nrhpQ): In 2020, YouTube introduced "chapters" which are marked timestamps on the video timeline bar. For over a decade, I'm sure you have seen people post timestamps to help others watch a long video.
![youtube-chapters](https://i.imgur.com/heqZcKw.png)
3. To-do
4. The YouTube algorithm is susceptible to being tricked, and will gladly promote clickbait and fake drama. Thus, whoever posts first on YouTube dictates the direction of the algorithm for a certain metagroup.

## Value Proposition :rocket:
* Streamers can funnel viewers into their channel rather than other "fan" channels.
* Streamers can upload videos faster and dictate the narrative of their brand.
* YouTube algorithm offers better discoverability than Twitch's recommendation algorithm.
* Eliminate potential loss of YouTube click through rate (CTR) and advertisement revenue.

## Resources and Credits :memo:
1. [Twitch Chat Downloader](https://github.com/PetterKraabol/Twitch-Chat-Downloader): For providing the Twitch chat downloader tool.
2. [Twitch-dl](https://github.com/ihabunek/twitch-dl): For providing the Twitch video downloader tool.
3. [Towards Extracting Highlights From Recorded Live Videos: An Implicit Crowdsourcing Approach. 2019](http://www.sfu.ca/~ruochenj/files/papers/Lightor_paper.pdf): Academic paper on identifying the start and end bounds of potential Twitch highlights using machine learning algorithms.
4. [Twitch Chat Sentiment Analysis. 2019](https://run.unl.pt/bitstream/10362/95285/1/TGI0288.pdf): Academic paper on contextualizing and predicting Twitch chat sentiment using popular Twitch, BTTV, and FFZ emotes.
5. [Visualizing Twitch Communities](https://github.com/KiranGershenfeld/VisualizingTwitchCommunities) For providing the data science visualization tool of grouping communities together by shared viewers.
6. [FFmpeg](https://www.ffmpeg.org/): CLI media framework to cut, merge, encode, and decode video.
