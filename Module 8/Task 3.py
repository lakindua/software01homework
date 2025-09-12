import mysql.connector
from geopy.distance import geodesic
loop = 0
location_list = []

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="12345",
    database="flight_game",
    port=3306,
    autocommit=True
)

while loop != 2:
    def distance(icao01):
        sql = f"""
                  select longitude_deg, latitude_deg
                  from airport
                  Where airport.ident = '{icao01}';
    """
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        if cursor.rowcount > 0:
            for longitude_deg, latitude_deg in result:
                location_list.append(latitude_deg)
                location_list.append(longitude_deg)


    user_input = input("Please enter the icao code of the airport : ").upper()
    distance(user_input)
    loop += 1


distance_km = geodesic(location_list[0:2], location_list[2:4])
print(f"Distance between the airports is {distance_km}")