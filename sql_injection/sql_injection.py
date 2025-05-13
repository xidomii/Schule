from mysql.connector import connect, Error

try:
    connection = connect(
        host = "localhost",
        username = "domi",
        password = "0407",
        database = "mitarbeiter"
    )
    cursor = connection.cursor()

    cursor.execute("use mitarbeiter;")

    username = input("Benutzername: ")
    password = input("Passwort: ")
    """
    ACHTUNG: Vulnerable to SQL Injection!
    sql_query = f"SELECT * FROM mitarbeiter WHERE username = '{username}' AND password = '{password}';"
    cursor.execute(sql_query)
    """

    # Lösung: Parametrisierter Input (cursor.execute)
    parameters = (username, password)
    cursor.execute("SELECT * FROM mitarbeiter WHERE username = %s AND password = %s", parameters)

    record = cursor.fetchall()

    if record:
        for r in record:
            print(r)
    else:
        print("Fehler, Kein Zugriff!")

except Error as e:
    print(f"Fehler: {e}")