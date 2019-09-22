# AwkwardAlertBot v0.1
# Written by yisoonshin
# Purpose is to create a post when the AwkwardSinceBirth Twitch channel enters a stream.
# Future functionality might check for new videos on the AwkwardSinceBirth Youtube channel and create a post

import praw
from twitch import TwitchClient


def main():
    # initialize the Reddit instance
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit("AwkwardSinceBirth")

    # get the status of AwkwardSinceBirth stream
    client = TwitchClient(client_id='x1vq30gh1w0pxqearh5l741m6p8ns2')
    stream = client.streams.get_live_streams(channel='130594176')  # Channel is fixed to AwkwardSinceBirth's ID
    currently_streaming = len(stream) > 0

    post_title = 'Alex is currently streaming on Twitch!'

    # Search the subreddit (by new) for a post with the above title. If it exists, save the ID and exit the loop.
    for submission in subreddit.new():
        post_exists = submission.title == post_title
        if post_exists:
            post_id = submission.id
            break

    # If the post exists and he is not streaming, delete the post.
    # If it doesn't exist and he is streaming, create the post. Pass over in all other cases.
    if post_exists:
        if currently_streaming:
            pass
        else:
            reddit.submission(post_id).delete()
            print("Deleted a post")
    else:
        if currently_streaming:
            submission = subreddit.submit(title=post_title, url='twitch.tv/AwkwardSinceBirth')
            # submission.mod.distinguish(how='yes', sticky=True)
            print("made a post")
        else:
            pass


if __name__ == "__main__":
    main()