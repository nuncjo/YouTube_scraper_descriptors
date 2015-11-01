# -*- coding:utf-8 -*-

from descriptors import YoutubePlaylists, YoutubeVideo
import requests


class YoutubeUserScraper(object):

    def __init__(self, user):
        self._user = user
        self._api_key = None

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, key):
        self._api_key = key

    def fetchall(self, **kwargs):

        vals = {'youtube_url': "https://www.googleapis.com/youtube/v3/",
                'user': self._user,
                'api_key': self._api_key,
                'max_results': kwargs.get('maxResults')}

        yt_channel_list_url = "{youtube_url}channels?part=contentDetails&forUsername={user}&key={api_key}".format(**vals)

        response = requests.get(yt_channel_list_url)
        json_response = response.json()
        playlists = YoutubePlaylists(json_response.get('items')[0])
        vals.update({'uploads': playlists.uploads})

        yt_uploaded_videos_url = "{youtube_url}playlistItems?part=snippet&playlistId={uploads}&key={api_key}&maxResults={max_results}".format(**vals)
        response = requests.get(yt_uploaded_videos_url)
        json_response = response.json()

        return [self.to_dict(YoutubeVideo(item)) for item in json_response.get('items')]

    def to_dict(self, row):

        result = {'id': row.id,
                  'content': row.description,
                  'permalink': "https://www.youtube.com/watch?v={}".format(row.video_id),
                  'title': row.title,
                  'created': row.published_at}

        return result


def run():
    from pprint import pprint
    youtubeuser_scrapper = YoutubeUserScraper('derekbanas')
    youtubeuser_scrapper.api_key = "" #<- API KEY HERE
    result = youtubeuser_scrapper.fetchall(maxResults=50)
    pprint(result)

run()