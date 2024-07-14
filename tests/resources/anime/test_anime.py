from ... import *

from anmoku import Anime

def test_anime_common_sync():
    anime_ids = [
        28851, # A Silent Voice
        9253, # Steins;Gate
    ]

    for id in anime_ids:
        anime = client.get(Anime, id)

        print(anime)

@wait_after(3) # wait for the seconds rate-limiter to be clear before we move onto the async tests.
def test_anime_rate_limit_sync():
    anime_ids = [
        28851, # A Silent Voice
        9253, # Steins;Gate
        55791, # "Oshi no Ko" 2nd Season
        54789, # Boku no Hero Academia 7th Season
    ]

    for id in anime_ids:
        anime = client.get(Anime, id)

        print(anime)

@pytest.mark.asyncio(scope = "session")
async def test_anime_common_async():
    anime_ids = [
        28851, # A Silent Voice
        9253, # Steins;Gate
    ]

    for id in anime_ids:
        anime = await async_client.get(Anime, id)

        print(anime)

@pytest.mark.asyncio(scope = "session")
async def test_anime_rate_limit_async():
    anime_ids = [
        28851, # A Silent Voice
        9253, # Steins;Gate
        55791, # "Oshi no Ko" 2nd Season
        54789, # Boku no Hero Academia 7th Season
    ]

    for id in anime_ids:
        anime = await async_client.get(Anime, id)

        print(anime)