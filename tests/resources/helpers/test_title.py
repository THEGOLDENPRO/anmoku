from ... import *

from anmoku import Anime

@pytest.mark.asyncio(scope = "session")
@wait_after(3, is_async = True) # so the second rate-limiter is clear before it gets to test_name.py
async def test_title_helper():
    anime = await async_client.get(Anime, 28851)

    title = anime.title

    assert str(title) == "Koe no Katachi"
    assert title.english == "A Silent Voice"
    assert title.japanese == "聲の形"
    assert "The Shape of Voice" in title.synonyms