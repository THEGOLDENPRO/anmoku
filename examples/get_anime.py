from anmoku import Anime, Anmoku

client = Anmoku()

anime = client.get(Anime, id = 13759)

print(
    f"Got the anime '{anime.name}', it's english name is '{anime.name.english}' and it was aired in {anime.aired.from_.year}."
)

# Display it's image.
anime.image.get_image().show()