import json
import os
from googleapiclient.discovery import build
import isodate

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('APY_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.channel_id = channel_id
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]['description']
        self.url = "https://www.youtube.com/" + self.channel["items"][0]["snippet"]["customUrl"]
        self.subscribers_count = int(self.channel["items"][0]["statistics"]["subscriberCount"])
        self.video_count = int(self.channel["items"][0]["statistics"]["videoCount"])
        self.view_count = int(self.channel["items"][0]["statistics"]["viewCount"])
        

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel)

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    def to_json(self, name):
        write_in_json = {
                         "id": self.channel_id,
                         "title": self.title,
                         "description": self.description,
                         "url": self.url,
                         "subscribersCount": self.subscribers_count,
                         "videoCount": self.video_count,
                         "viewCount": self.view_count
                        }
        with open(f"{name}", "w",     encoding="utf-8") as file:
            json.dump(write_in_json, file, indent=4, ensure_ascii=False)

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, objeckt_2):
        return self.subscribers_count+ objeckt_2.subscribers_count
    
    def __sub__(self, objeckt_2):
        return self.subscribers_count - objeckt_2.subscribers_count

    def __lt__(self, objeckt_2):
        return self.subscribers_count < objeckt_2.subscribers_count

    def __le__(self, objeckt_2):
        return self.subscribers_count <= objeckt_2.subscribers_count

    def __gt__(self, objeckt_2):
        return self.subscribers_count > objeckt_2.subscribers_count

    def __ge__(self, objeckt_2):
        return self.subscribers_count >= objeckt_2.subscribers_count

    def __eq__(self, objeckt_2):
        return self.subscribers_count == objeckt_2.subscribers_count


