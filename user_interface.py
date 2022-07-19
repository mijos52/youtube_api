import streamlit
import logging
from youtube_search import youtube_search


def log_info() -> None:
    logging.basicConfig(
        filename="./logs/logs.txt",
        format="%(asctime)s-%(module)s-%(message)s",
        level=logging.INFO,
    )
    logging.info("starting programmme")


def main_page() -> None:
    streamlit.subheader("Advanced Search")


def sidebar_elements() -> str:
    sidebar = streamlit.sidebar
    sidebar.title("Search Dashboard")
    search_string = sidebar.text_input("Search String")
    sidebar.text_input("Channel type")
    sidebar.text_input("Safe search")
    sidebar.text_input("Video caption")
    sidebar.text_input("Video duration")
    sidebar.text_input("Video type")

    sidebar.button(
        label="Go", on_click=streamlit.write("Showing results for ", search_string)
    )
    return search_string


def on_search_entry(search_input: str) -> list:
    return youtube_search(search_input)


def draw_search_result(lists: list) -> None:
    for item in lists:
        streamlit.image(item[1])
        streamlit.write(item[2])


def play_video(video_id: str, video_title: str, video_description: str) -> None:
    streamlit.video(f"https://www.youtube.com/watch?v={video_id}", format="video/MP4")
    streamlit.subheader(video_title)
    streamlit.write(video_description)


main_player_ui, videos_ui = streamlit.columns(2)

with videos_ui:

    log_info()
    main_page()
    x = sidebar_elements()
    lists = on_search_entry(x)
    draw_search_result(lists)


with main_player_ui:
    streamlit.header("Youtube Player")
    play_video(
        video_id="HzpgGPdorP8",
        video_title="2022 Lamborghini Aventador Ultimae review - The last hurrah | Drive | Autocar India",
        video_description="The Lamborghini Aventador is a legend and bows it in great style in limited-run Ultimae form. Hormazd Sorabjee heads to Italy to drive what will be the last of the pure naturally-aspirated V12 Lamborghinis.",
    )
