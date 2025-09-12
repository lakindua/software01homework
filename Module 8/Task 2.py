import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='12345',
    port=3306,
    database='flight_game',
    autocommit=True
)

def code(areacode):
    sql = f"""
        SELECT airport.name, airport.type
        FROM airport
        WHERE airport.iso_country = '{areacode}'
        ORDER BY airport.type asc, airport.name ;
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for name, type in result:
            print(f"Airport name: {name}  | Type: {type}")
    else:
        print("Invalid areacode")

user_area = input("Enter your area code : ").upper()
code(user_area)
