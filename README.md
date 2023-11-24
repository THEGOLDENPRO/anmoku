<div align="center">

  # Anmoku 安黙

  <sub>A peaceful and fully typed [MyAnimeList](https://myanimelist.net/) / [Jikan](https://jikan.moe/) Python API wrapper with caching and proper rate limiting.</sub>

  <br>

</div>

> [!NOTE]
> 
> Anmoku is currently a work in progress so the features below may not be complete yet.

## Features ✨
- [ ] Fully type hinted. 🌌 ~~*yes you heard me*~~
- [ ] Rate limiting 🎀 (with actual waiting).
- [ ] Supports caching. ⚡

## It's eassssssy! 😄
```python
import asyncio
from anmoku import AnimeCharacters

async def main():

    client = AsyncAnmoku(debug = True)

    anime_id = 28851 # ID for the anime film "A Silent Voice"

    anime_characters = await client.get(AnimeCharacters, anime_id)

    for character in anime_characters:
        print(f"{character.name} ({character.url})")

    await client.close()

asyncio.run(main())
```

### Output:
```sh
[DEBUG] (anmoku) - [AsyncAnmoku] GET --> https://api.jikan.moe/v4/anime/28851/characters
Ishida, Shouya (https://myanimelist.net/character/80491/Shouya_Ishida)
Nishimiya, Shouko (https://myanimelist.net/character/80243/Shouko_Nishimiya)
Headteacher (https://myanimelist.net/character/214351/Headteacher)
Hirose, Keisuke (https://myanimelist.net/character/97569/Keisuke_Hirose)
Ishida, Maria (https://myanimelist.net/character/97943/Maria_Ishida)
Ishida, Sister (https://myanimelist.net/character/118723/Sister_Ishida)
# ... more characters below but I cut them off for the convenience of this readme
```

## Type hinting support! 🌌
Our library is strongly typed.
<img src="./assets/type_hints_1.png" width="100%">
On top of that we even provide class interfaces if you wish for stability and easy of use.
<img src="./assets/type_hints_2.png" width="100%">