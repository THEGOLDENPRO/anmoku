from . import *

from anmoku import Anime

ANIME_IDS_COMMON = [
    28851, # A Silent Voice
    9253, # Steins;Gate
]

ANIME_IDS_RATE_LIMIT = [
    28851, # A Silent Voice
    9253, # Steins;Gate
    55791, # "Oshi no Ko" 2nd Season
    54789, # Boku no Hero Academia 7th Season
    57810, # Shoushimin Series
    53887, # Spy x Family Season 2
]

def test_common_usage_sync():

    for id in ANIME_IDS_COMMON:
        anime = client.get(Anime, id)

        print(anime)

@wait_after(3) # wait for the seconds rate-limiter to be clear before we move onto the async tests.
def test_rate_limit_sync():

    for id in ANIME_IDS_RATE_LIMIT:
        anime = client.get(Anime, id)

        print(anime)

@pytest.mark.asyncio(scope = "session")
async def test_common_usage_async():

    for id in ANIME_IDS_COMMON:
        anime = await async_client.get(Anime, id)

        print(anime)

@pytest.mark.asyncio(scope = "session")
async def test_rate_limit_async():

    for id in ANIME_IDS_RATE_LIMIT:
        anime = await async_client.get(Anime, id)

        print(anime)