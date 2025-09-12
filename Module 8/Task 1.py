import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='12345',
    autocommit=True
)

def search_icao(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            name, municipality = row
            print(f"Your airport '{name}' is located in {municipality}")
    else:
        print("No airport found with that ICAO code.")

user_input = input("Enter the ICAO code: ")
search_icao(user_input)