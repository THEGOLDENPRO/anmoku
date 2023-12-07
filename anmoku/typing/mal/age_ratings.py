from typing import Literal

__all__ = (
    "MALRatings",
)

MALRatings = Literal[
    "G - All Ages",
    "PG - Children",
    "PG-13 - Teens 13 or older",
    "R - 17+ recommended (violence & profanity)",
    "R+ - Mild Nudity (may also contain violence & profanity)",
    "Rx - Hentai (extreme sexual content/nudity)",
]
"""
MyAnimeList age ratings. 

Source: https://myanimelist.net/info.php?go=mpaa
"""