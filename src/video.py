import json
import os
from googleapiclient.discovery import build
import isodate

class Video:

    api_key: str = os.getenv('APY_KEY')

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
        self.video_id = video_id
        self.title = self.video_response["items"][0]['snippet']['title']
        self.url = "https://www.youtube.com/watch?v=" + self.video_response["items"][0]["id"]
        self.view_count = int(self.video_response["items"][0]['statistics']['viewCount'])
        self.like_count = int(self.video_response["items"][0]['statistics']['likeCount'])

    def __str__(self):
        return f"{self.title}"

class PLVideo(Video):

    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id