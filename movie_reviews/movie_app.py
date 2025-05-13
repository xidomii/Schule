import mysql.connector

# Funktion, um die Verbindung zur MySQL-Datenbank herzustellen
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="domi",
        password="0407",
        database="movie_reviews"
    )

# Funktion, um alle Filme eines bestimmten Jahres anzuzeigen
def search_movies_by_year(year):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT title FROM movies WHERE release_year = %s"
    cursor.execute(query, (year,))
    movies = cursor.fetchall()
    db.close()

    if movies:
        print(f"Filme aus dem Jahr {year}:")
        for movie in movies:
            print(movie[0])
    else:
        print(f"Keine Filme aus dem Jahr {year} gefunden.")

# Funktion, um alle Bewertungen eines bestimmten Films anzuzeigen
def show_reviews_for_movie(movie_title):
    db = connect_db()
    cursor = db.cursor()
    query = """
    SELECT CONCAT(r.first_name, ' ', r.last_name) AS reviewer_name, rt.rating
    FROM ratings rt
    JOIN reviewers r ON rt.reviewer_id = r.id
    JOIN movies m ON rt.movie_id = m.id
    WHERE m.title = %s
    """
    cursor.execute(query, (movie_title,))
    reviews = cursor.fetchall()
    db.close()

    if reviews:
        print(f"Bewertungen für den Film '{movie_title}':")
        for review in reviews:
            print(f"Reviewer: {review[0]}, Bewertung: {review[1]}")
    else:
        print(f"Keine Bewertungen für den Film '{movie_title}' gefunden.")

# Funktion, um alle Bewertungen eines bestimmten Reviewers anzuzeigen
def show_reviews_for_reviewer(reviewer_first_name, reviewer_last_name):
    db = connect_db()
    cursor = db.cursor()
    query = """
    SELECT m.title, rt.rating
    FROM ratings rt
    JOIN reviewers r ON rt.reviewer_id = r.id
    JOIN movies m ON rt.movie_id = m.id
    WHERE r.first_name = %s AND r.last_name = %s
    """
    cursor.execute(query, (reviewer_first_name, reviewer_last_name))
    reviews = cursor.fetchall()
    db.close()

    if reviews:
        print(f"Bewertungen von {reviewer_first_name} {reviewer_last_name}:")
        for review in reviews:
            print(f"Film: {review[0]}, Bewertung: {review[1]}")
    else:
        print(f"Keine Bewertungen von {reviewer_first_name} {reviewer_last_name} gefunden.")

# Funktion, um die durchschnittliche Bewertung eines Films anzuzeigen
def average_rating_for_movie(movie_title):
    db = connect_db()
    cursor = db.cursor()
    query = """
    SELECT AVG(rt.rating)
    FROM ratings rt
    JOIN movies m ON rt.movie_id = m.id
    WHERE m.title = %s
    """
    cursor.execute(query, (movie_title,))
    avg_rating = cursor.fetchone()[0]
    db.close()

    if avg_rating is not None:
        print(f"Durchschnittliche Bewertung für '{movie_title}': {avg_rating:.2f}")
    else:
        print(f"Keine Bewertungen für den Film '{movie_title}' gefunden.")

# Benutzeroberfläche für die Eingabe der Abfragen
def main():
    while True:
        print("\nWählen Sie eine Option:")
        print("1. Filme nach Jahr suchen")
        print("2. Bewertungen eines Films anzeigen")
        print("3. Bewertungen eines Reviewers anzeigen")
        print("4. Durchschnittliche Bewertung eines Films anzeigen")
        print("5. Beenden")
        
        choice = input("Ihre Wahl: ")

        if choice == "1":
            year = input("Geben Sie das Jahr ein: ")
            search_movies_by_year(year)
        elif choice == "2":
            movie_title = input("Geben Sie den Titel des Films ein: ")
            show_reviews_for_movie(movie_title)
        elif choice == "3":
            first_name = input("Geben Sie den Vornamen des Reviewers ein: ")
            last_name = input("Geben Sie den Nachnamen des Reviewers ein: ")
            show_reviews_for_reviewer(first_name, last_name)
        elif choice == "4":
            movie_title = input("Geben Sie den Titel des Films ein: ")
            average_rating_for_movie(movie_title)
        elif choice == "5":
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl, bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()