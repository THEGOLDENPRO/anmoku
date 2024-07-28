from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Dict, Type
    from anmoku.clients.base import ResourceGenericT

from .. import *

import inspect
from anmoku import *

resources_to_in_depth_test: Dict[Type[ResourceGenericT], ResourceGenericT] = {}

@pytest.mark.asyncio(scope = "session")
async def test_get_all_resources():
    for _, _object in globals().items():

        if not inspect.isclass(_object):
            continue

        if issubclass(_object, JikanResource):
            resource = _object

            if resource._get_endpoint is None:
                continue

            print(">", _object)

            resource_object = await async_client.get(resource, 1)

            resources_to_in_depth_test[resource] = resource_object


@pytest.mark.asyncio(scope = "session")
async def test_full_anime():
    full_anime: FullAnime = resources_to_in_depth_test[FullAnime]

    assert str(full_anime.name) == "Cowboy Bebop"

@pytest.mark.asyncio(scope = "session")
@wait_after(3, is_async = True)
async def test_anime_characters():
    anime_characters: AnimeCharacters = resources_to_in_depth_test[AnimeCharacters]

    character_ids = [x.id for x in anime_characters]

    assert 1 in character_ids # Spiegel, Spike
    assert 2 in character_ids # Faye Valentine
    assert 16 in character_ids # Edward Wong Hau Pepelu Tivrusky IV
    assert 3 in character_ids # Jet Black
    assert 4 in character_ids # Ein
    assert 2734 in character_ids # Vicious
    assert 2736 in character_ids # Grencia Mars Elijah Guo Eckener