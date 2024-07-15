from ... import *

from PIL.Image import Image
from anmoku import AnimeCharacters

@pytest.mark.asyncio(scope = "session")
async def test_image():
    anime_characters = await async_client.get(AnimeCharacters, 55791)

    for character in anime_characters:
        print(">>", character.image.url)

        if character.image.url is not None:
            assert isinstance(character.image.get_image(), Image)