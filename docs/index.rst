:og:title: Anmoku Documentation

:og:description: 🌟 Learn to use our easy to use API wrapper.

.. image:: _static/logo.svg
  :width: 700
  :align: center

A peaceful and fully typed MAL_ / Jikan_ Python API wrapper with caching and proper rate limiting.

.. _MAL: https://myanimelist.net/
.. _Jikan: https://jikan.moe/

.. toctree::
   :maxdepth: 1

   clients
   resources
   typing

Examples ⚗️
==============
Anmoku is probably the simplest Jikan API wrapper you'll ever use. All you need is a client and a resource. 🌊

.. code-block:: python

   from anmoku import Anmoku, AnimeCharacters

   client = Anmoku(debug = True)

   anime_characters = client.get(AnimeCharacters, id = 28851) # ID for the anime film "A Silent Voice".

   for character in anime_characters:
      print(f"{character.name} ({character.url})")

   client.close()

We also have an async client:

.. code-block:: python

   import asyncio
   from anmoku import AsyncAnmoku, AnimeCharacters

   async def main():

      client = AsyncAnmoku(debug = True)

      anime_characters = await client.get(AnimeCharacters, id = 28851) # ID for the anime film "A Silent Voice".

      for character in anime_characters:
         print(f"{character.name} ({character.url})")

      await client.close()

   asyncio.run(main())

Output:

.. code-block:: sh

   [DEBUG] (anmoku) - [AsyncAnmoku] GET --> https://api.jikan.moe/v4/anime/28851/characters
   Ishida, Shouya (https://myanimelist.net/character/80491/Shouya_Ishida)
   Nishimiya, Shouko (https://myanimelist.net/character/80243/Shouko_Nishimiya)
   Headteacher (https://myanimelist.net/character/214351/Headteacher)
   Hirose, Keisuke (https://myanimelist.net/character/97569/Keisuke_Hirose)
   Ishida, Maria (https://myanimelist.net/character/97943/Maria_Ishida)
   Ishida, Sister (https://myanimelist.net/character/118723/Sister_Ishida)
   # ... more characters below but I cut them off for the convenience of this readme

Searching! 🤩
--------------
Here are some searching examples you can try:

.. code-block:: python

   from anmoku import Anmoku, Character

   client = Anmoku(debug = True)

   characters = client.search(Character, "anya forger")

   for character in characters:
      print(f"{character.name} ({character.image.url})")

   client.close()

Errors
-------
.. automodule:: anmoku.errors
   :members:
   :undoc-members:
   :show-inheritance:

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`