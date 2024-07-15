from ... import *

from anmoku import FullAnime

@pytest.mark.asyncio(scope = "session")
async def test_full_anime():
    full_anime = await async_client.get(FullAnime, 55791)

    assert str(full_anime.name) == '"Oshi no Ko" 2nd Season'

# The other Anime resources have already been tested in test_client.py so no need to do so here.