from ... import *

from typing import List
from anmoku import Character

@pytest.mark.asyncio(scope = "session")
async def test_search_result_helper():
    search_results = await async_client.search(Character, "Anya Forger")

    assert isinstance(search_results.data, dict)

    characters_found: List[int] = []

    for character in search_results:
        assert isinstance(character, Character)

        characters_found.append(character.id)

    assert 170256 in characters_found # Anya Forger