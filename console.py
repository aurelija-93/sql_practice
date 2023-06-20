import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("The Smashing Pumpkins")
artist_repository.save(artist_1)

artist_2 = Artist("Fleetwood Mac")
artist_repository.save(artist_2)

album_1 = Album("Siamese Dream", "Alternative rock", artist_1)
album_repository.save(album_1)

album_2 = Album("Mellon Collie and the Infinite Sadness", "Alternative rock", artist_1)
album_repository.save(album_2)
album_repository.delete(album_2.id)

album_3 = Album("Rumours", "Pop rock", artist_2)
album_repository.save(album_3)

all_albums = album_repository.select_all()
for album in all_albums:
    print(album.__dict__)

all_artists = artist_repository.select_all()
for artist in all_artists:
    print(artist.__dict__)

album = album_repository.select(album_1.id)
print(album.__dict__)

artist = artist_repository.select(artist_2.id)
print(artist.__dict__)

albums_by_artist = album_repository.select_by_artist(artist_2)
for album in albums_by_artist:
    print(album.__dict__)

pdb.set_trace()