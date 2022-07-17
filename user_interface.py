import streamlit
import logging
from  youtube_search import youtube_search


def log_info() -> None:
  logging.basicConfig(filename='./logs/logs.txt',format='%(asctime)s-%(module)s-%(message)s' ,level=logging.INFO)
  logging.info('starting programmme')

def main_page() -> None:
  streamlit.title('Search Results')
  streamlit.write('Find Youtube Videos ')

def sidebar_elements() -> str:
  sidebar = streamlit.sidebar
  sidebar.title('Search Dashboard')
  search_string = sidebar.text_input('Search String')
  sidebar.button(label='Go', on_click=on_search_entry(search_input=search_string))
  return search_string

def on_search_entry(search_input:str)->list:
  return youtube_search(search_input)
 
def draw_search_result(thumb) -> None:
    for i in thumb:
        streamlit.image(i)
    

log_info()
main_page()
x = sidebar_elements()
thumb = on_search_entry(x)
draw_search_result(thumb)



