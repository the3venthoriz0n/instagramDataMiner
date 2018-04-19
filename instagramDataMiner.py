# instagramDataMine by Andrew Kaplan 4/18
# For more information check the below links
# https://instagram.com/developer/authentication/
# https://github.com/facebookarchive/python-instagram
# https://docs.google.com/spreadsheets/d/1aS9YY56SEjlvJtIxA_3A7-g2pvI9sjFRwVxbthgr14A/edit#gid=385574993
# https://www.instagram.com/explore/tags/fender/?__a=1&max_id=10000

import auth
from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError


api = InstagramAPI(access_token=auth.accessToken, client_secret=auth.clientSecret)


def getPictures():
    try:
        recent_media, next_ = api.user_recent_media(client_id=auth.clientId, count=100)
        photos = []
        for media in recent_media:
            photos.append('<img src="%s"/>' % media.images['thumbnail'].url)
        for picture in photos:
            print(picture)

    except InstagramAPIError as e:
        if (e.status_code == 400):
            print("\nUser is set to private.")
    return

getPictures()

def getFollowers():
    try:
        follows, next_ = api.user_follows()
        while next_:
            more_follows, next_ = api.user_follows(with_next_url=next_)
            follows.extend(more_follows)
    except InstagramAPIError as e:
        if (e.status_code == 400):
            print("\nUser is set to private.")
    return

#getFollowers()
