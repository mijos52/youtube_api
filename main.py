import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pprint import pprint


def youtube_search():

  youtube = build(config.YOUTUBE_API_SERVICE_NAME, config.YOUTUBE_API_VERSION,developerKey=config.API_KEY)

  search_response = youtube.search().list(
    part="snippet",
    q="lamborghini",
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


  pprint(search_response)

  videos = []


  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s (%s)' % (search_result['snippet']['title'],
                                 search_result['id']['videoId']))


  print ('Videos:\n', '\n'.join(videos), '\n')

def main():
    youtube_search()


if __name__ == '__main__':
    main()