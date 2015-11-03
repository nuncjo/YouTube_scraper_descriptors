#-*- coding:utf-8 -*-

import dict_digger


class JsonResponseDescriptor(object):
    def __init__(self, *path):
        self.path = path

    def __get__(self, instance, owner):
        item = dict_digger.dig(instance.json_response, *self.path)
        return item

    def __set__(self, instance, value):
        pass


class YoutubePlaylists(object):
    def __init__(self, json_response):
        self.json_response = json_response

    favorites = JsonResponseDescriptor('contentDetails', 'relatedPlaylists', 'favorites')
    uploads = JsonResponseDescriptor('contentDetails', 'relatedPlaylists', 'uploads')


class YoutubeVideo(object):
    def __init__(self, json_response):
        self.json_response = json_response

    id = JsonResponseDescriptor('id')
    published_at = JsonResponseDescriptor('snippet', 'publishedAt')
    title = JsonResponseDescriptor('snippet', 'title')
    description = JsonResponseDescriptor('snippet', 'description')
    channel_title = JsonResponseDescriptor('contentDetails', 'relatedPlaylists', 'channelTitle')
    default_thumbnail = JsonResponseDescriptor('contentDetails', 'relatedPlaylists', 'thumbnails', 'default')
    video_id = JsonResponseDescriptor('snippet', 'resourceId', 'videoId')
