from mysql.connector import connect, Error

try:
    connection = connect(
        host = "localhost",
        username = "domi",
        password = "0407",
        database ="mitarbeiter"
    )
    cursor = connection.cursor()

    username = input("Benutzername: ")
    password = input("Passwort: ")

    sql_query = f"SELECT * FROM mitarbeiter WHERE username = '{username}' AND password = '{password}'"

    cursor.execute(sql_query)

    record = cursor.fetchall()

    if record:
        for r in record:
            print(r)
    else:
        print("Fehler")

except Error as e:
    print(f"Fehler: {e}")