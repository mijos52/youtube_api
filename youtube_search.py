import config
from googleapiclient.discovery import build


def youtube_search(search:int) -> list:

  youtube = build(config.YOUTUBE_API_SERVICE_NAME, config.YOUTUBE_API_VERSION,developerKey=config.API_KEY)

  search_response = youtube.search().list(
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
    videoType="any"
  ).execute()

  video_title = []
  video_id = []
  video_thumb = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      video_id.append(search_result['id']['videoId'])
      video_thumb.append(search_result['snippet']['thumbnails']['high']['url'])
      video_title.append(search_result['snippet']['title'])
  

  return(video_thumb)


