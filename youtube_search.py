import config
from googleapiclient.discovery import build
from pprint import pprint


def youtube_search(search: int) -> list:

    youtube = build(
        config.YOUTUBE_API_SERVICE_NAME,
        config.YOUTUBE_API_VERSION,
        developerKey=config.API_KEY,
    )

    r = (
        youtube.search()
        .list(
            part="snippet",
            q=search,
            channelType="any",
            order="relevance",
            safeSearch="none",
            videoCaption="any",
            videoDefinition="any",
            videoDimension="any",
            videoDuration="any",
            videoEmbeddable="any",
            videoLicense="any",
            videoSyndicated="any",
            videoType="any",
        )
        .execute()
    )

    r = r["items"]

    " r is the search reponse dict"

    data_list = []
    for i in r:
        if i["id"]["kind"] == "youtube#video":
            list_ = [
                i["id"]["videoId"],
                i["snippet"]["thumbnails"]["medium"]["url"],
                i["snippet"]["title"],
            ]
            data_list.append(list_)
    return data_list
