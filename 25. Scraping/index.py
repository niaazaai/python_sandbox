
# from facebook_scraper import *

# set_user_agent("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")


# print(get_profile("maseeh.niazai" ,  cookies="cookies.txt"))

# # print(get_profile("Abdul.Jabbar.Naseri"))


# # print(get_friends("maseeh.niazai"))





import facebook_scraper as fs

# get POST_ID from the URL of the post which can have the following structure:
# https://www.facebook.com/USER/posts/POST_ID
# https://www.facebook.com/groups/GROUP_ID/posts/POST_ID
POST_ID = "5444990395620770"
# number of comments to download -- set this to True to download all comments
MAX_COMMENTS = 4

# get the post (this gives a generator)
gen = fs.get_posts(
    post_urls=[POST_ID],
    options={"comments": MAX_COMMENTS, "progress": True}

)

# take 1st element of the generator which is the post we requested
post = next(gen)

# extract the comments part
comments = post['comments_full']

# process comments as you want...
for comment in comments:

    # e.g. ...print them
    print(comment)

    # e.g. ...get the replies for them
    for reply in comment['replies']:
        print(' ', reply)
