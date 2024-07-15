from ... import *

from anmoku import Character

@pytest.mark.asyncio(scope = "session")
async def test_title_helper():
    character = await async_client.get(Character, 65865)

    name = character.name

    assert str(name) == "Rikka Takanashi"
    assert name.kanji == "小鳥遊 六花"