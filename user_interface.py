import streamlit
import logging
from  youtube_search import youtube_search


def log_info() -> None:
  logging.basicConfig(filename='./logs/logs.txt',format='%(asctime)s-%(module)s-%(message)s' ,level=logging.INFO)
  logging.info('starting programmme')

def main_page() -> None:
  streamlit.title('Search Results')
  streamlit.write('Find Youtube Videos ')

def sidebar_elements() -> None:
  sidebar = streamlit.sidebar
  sidebar.title('Search Dashboard')
  search_string = sidebar.text_input('Search String')
  sidebar.button(label='Go', on_click=on_search_entry(search_input=search_string))
  return search_string

def on_search_entry(search_input:str)->None:
  return youtube_search(search_input)
 
def draw_search_result(url_list:list) -> None:
  pass


log_info()
main_page()
sidebar_elements()


