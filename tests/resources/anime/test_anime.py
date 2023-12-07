from ... import *

from anmoku import Anime

@pytest.mark.asyncio
async def test_anime():
    anime_ids = [
        28851, # A Silent Voice
        9253, # Steins;Gate
    ]

    for id in anime_ids:
        anime = await client.get(Anime, id)

        print(anime)

@pytest.mark.asyncio
async def test_anime_rate_limit():
    ...