from ... import *

from anmoku import AnimeCharacters

@pytest.mark.asyncio(scope = "session")
async def test_anime_characters():
    anime_characters = await async_client.get(AnimeCharacters, 55791)

    character_ids = [x.id for x in anime_characters]

    assert 188038 in character_ids # Arima, Kana
    assert 185313 in character_ids # Aquamarine "Aqua" Hoshino
    assert 195178 in character_ids # Akane "Genius Actress" Kurokawa
    assert 188037 in character_ids # Ai Hoshino
    assert 186921 in character_ids # Ruby Hoshino
    assert 199940 in character_ids # Mem-Cho

# The other Anime resources have already been tested in test_client.py so no need to do so here.