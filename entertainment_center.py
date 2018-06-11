import media
import fresh_tomatoes

# Up Movie
up = media.Movie("Up",
                 "Carl Fredricksen, a 78-year-old balloon salesman, is about to fulfill a lifelong dream. Tying thousands of balloons to his house, he flies away to the South American wilderness.",  # NOQA
                 "https://goo.gl/KWNW7B",
                 "https://youtu.be/pkqzFUhGPJg")

# Logan Movie
logan = media.Movie("Logan",
                    "In the near future, a weary Logan (Hugh Jackman) cares for an ailing Professor X (Patrick Stewart) at a remote outpost on the Mexican border.",  # NOQA
                    "https://goo.gl/11zfE6",
                    "https://youtu.be/Div0iP65aZo")

# Inception Movie
inception = media.Movie("inception",
                        "Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter people's dreams and steal their secrets from their subconscious",  # NOQA
                        "https://goo.gl/izwtpq",
                        "https://youtu.be/YoHD9XEInc0")


# Warrior Movie
warrior = media.Movie("Warrior",
                      "An estranged family finds redemption in the unlikeliest of places: the MMA ring. Tommy (Tom Hardy), an ex-Marine with a tragic past, returns home and enlists his father (Nick Nolte), a recovering alcoholic and former wrestling coach, to train him for Sparta, the biggest MMA tournament ever held",  # NOQA
                      "https://goo.gl/FNP4qc",
                      "https://youtu.be/I5kzcwcQA1Q")

# The Dark Night Rises Movie
the_dark_night_rises = media.Movie("The Dark Knight Rises",
                                   "It has been eight years since Batman (Christian Bale), in collusion with Commissioner Gordon (Gary Oldman), vanished into the night. Assuming responsibility for the death of Harvey Dent, Batman sacrificed everything for what he and Gordon hoped would be the greater good.",  # NOQA
                                   "https://goo.gl/TnCteP",
                                   "https://youtu.be/GokKUqLcvD8")

# Transcendence Movie
transcendence = media.Movie("Transcendence",
                            "Dr. Will Caster (Johnny Depp), the world's foremost authority on artificial intelligence, is conducting highly controversial experiments to create a sentient machine.",  # NOQA
                            "https://goo.gl/oB5KAD",
                            "https://youtu.be/VCTen3-B8GU")


# The Shawshank Redemption Movie
the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "Andy Dufresne (Tim Robbins) is sentenced to two consecutive life terms in prison for the murders of his wife and her lover and is sentenced to a tough prison.",  # NOQA
                                       "https://goo.gl/dt8gwL",
                                       "https://youtu.be/K_tLp7T6U1c")

# The Prestige Movie
the_prestige = media.Movie("The Prestige", "Period thriller set in Edwardian London where two rival magicians, partners until the tragic death of an assistant during a show, feud bitterly after one of them performs the ultimate magic trick - teleportation.",  # NOQA
                           "https://goo.gl/wAukx1",
                           "https://youtu.be/ijXruSzfGEc")

# Law Abiding Citizen Movie
law_abiding_citizen = media.Movie("Law Abiding Citizen",
                                  "Clyde Shelton (Gerard Butler) is an honorable family man, until the day his wife and daughter are murdered in a home invasion. He hopes for justice, but a rising prosecutor named Nick Rice (Jamie Foxx) cuts a deal with one of the killers in exchange for testimony.",  # NOQA
                                  "https://goo.gl/Kjh2yc",
                                  "https://youtu.be/LX6kVRsdXW4")

# List of all te movies
movies = [up, logan, inception,
          warrior, the_dark_night_rises, transcendence,
          the_shawshank_redemption, the_prestige, law_abiding_citizen]

# open web page with the movies list
fresh_tomatoes.open_movies_page(movies)
