import gradio # pip install gradio
from anmoku import Anime, Anmoku, RatelimitError

client = Anmoku(debug = True)

def search_anime(query: str):
    anime_list = []

    try:
        anime_list = client.search(Anime, query)

    except RatelimitError as e: # NOTE: This is here because rate limiting hasn't been implemented yet in this version.
        raise gradio.Error(e.message)

    return [(x.image.get_image(), str(x.name)) for x in anime_list]

demo = gradio.Interface(
    search_anime, 
    inputs = "text", 
    outputs = gradio.Gallery(height = 600)
)

if __name__ == "__main__":
    demo.launch(show_api = False)