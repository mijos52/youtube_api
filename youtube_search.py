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


  videos = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      # videos.append('%s %s (%s)' % (search_result['snippet']['title'],search_result['snippet']['thumbnails']['high'],
      #                            search_result['id']['videoId']))
      videos.append('%s' % search_result['snippet']['thumbnails']['high']['url'])

  return(videos)



