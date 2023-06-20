import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# album_repository.delete_all()
# artist_repository.delete_all()

artist_1 = Artist("The Smashing Pumpkins")
artist_repository.save(artist_1)

artist_2 = Artist("Fleetwood Mac")
artist_repository.save(artist_2)

album_1 = Album("Siamese Dream", "Alternative rock", artist_1)
album_repository.save(album_1)

album_2 = Album("Mellon Collie and the Infinite Sadness", "Alternative rock", artist_1)
album_repository.save(album_2)

album_3 = Album("Rumours", "Pop rock", artist_2)
album_repository.save(album_3)

# album_repository.find(album_1.id)

# artist_repository.find(artist_2.id)

# album_repository.select_all()

# artist_repository.select_all()

pdb.set_trace()