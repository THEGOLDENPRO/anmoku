from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Dict, Type, Tuple
    from anmoku.clients.base import ResourceGenericT

from .. import *

import dataclasses
from anmoku import Anime, FullAnime, AnimeCharacters

test_list: Dict[Type[ResourceGenericT], Tuple[int]] = {
    resource_class: (1,) for resource_class in get_all_resource_classes()
}

test_list.update(
    {
        # TODO: Add more uniquely defined content for other resources.
        Anime: (
            1, # Cowboy Bebop
            52480, # Tantei wa Mou, Shindeiru. Season 2 (UNRELEASED)
            18, # Initial D Fourth Stage
            60108, # One Piece: Gyojin Tou-hen
            57433, # Seishun Buta Yarou wa Santa Claus no Yume wo Minai
            4454, # Macross F: Close Encounter - Deculture Edition
            43534, # Xiao Song Shu Li Fa Shi (SCORE IS N/A),
            5842, # Kotatsu Neko (SOME RANDOM ONA)
        )
    }
)

resources_to_in_depth_test: Dict[Type[ResourceGenericT], List[Tuple[ResourceGenericT, int]]] = {}

@pytest.mark.asyncio(scope = "session")
async def test_get_all_resources():
    for resource, anime_ids_to_test in test_list.items():

        for anime_id in anime_ids_to_test:
            resource_object = await async_client.get(resource, anime_id)

            if resource not in resources_to_in_depth_test:
                resources_to_in_depth_test[resource] = []

            resources_to_in_depth_test[resource].append((resource_object, anime_id))

@pytest.mark.asyncio(scope = "session")
async def test_resource_attributes():
    for resource_class in resources_to_in_depth_test:

        for (resource, id) in resources_to_in_depth_test[resource_class]:
            fields = dataclasses.fields(resource_class)

            for attribute in [field.name for field in fields]:
                if attribute.startswith("_"):
                    continue

                try:
                    getattr(resource, attribute)
                except AttributeError as e:
                    assert False, f"The '{attribute}' dataclass field is undefined in " \
                        f"{resource_class.__name__} for resource ID '{id}'! That field might " \
                        f"be missing a default value.\n Error: {e}"

@pytest.mark.asyncio(scope = "session")
async def test_full_anime():
    full_anime: FullAnime = resources_to_in_depth_test[FullAnime][0][0]

    assert str(full_anime.name) == "Cowboy Bebop"

@pytest.mark.asyncio(scope = "session")
@wait_after(3, is_async = True) # so the second rate-limiter is clear before it gets to test_client.py
async def test_anime_characters():
    anime_characters: AnimeCharacters = resources_to_in_depth_test[AnimeCharacters][0][0]

    character_ids = [x.id for x in anime_characters]

    assert 1 in character_ids # Spiegel, Spike
    assert 2 in character_ids # Faye Valentine
    assert 16 in character_ids # Edward Wong Hau Pepelu Tivrusky IV
    assert 3 in character_ids # Jet Black
    assert 4 in character_ids # Ein
    assert 2734 in character_ids # Vicious
    assert 2736 in character_ids # Grencia Mars Elijah Guo Eckener

# TODO: Test more resources