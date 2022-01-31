import pandas as pd
import mysql.connector


def get_data(filename):
    return pd.read_excel(filename)


def push_to_database(cursor, data, query, connection):
    for index, row in data.iterrows():
        datetime = row['datetime']
        close = row['close']
        high = row['high']
        low = row['low']
        open = row['open']
        volume = row['volume']
        instrument = row['instrument']

        data = (str(datetime), close, high, low, open, volume, instrument)

        cursor.execute(query, data)
    connection.commit()


# inserting rows from dataframe to sql


def create_connection(user, password, host, database):
    cnx = mysql.connector.connect(
        user=user, password=password, host=host, database=database)
    return cnx.cursor(), cnx


if __name__ == "__main__":

    cursor, cnx = create_connection(
        user="root", password="pass@mysql", host="localhost", database='stocks')

    sheet = get_data(filename="HINDALCO_1D.xlsx")
    query = """INSERT INTO hindalco (datetime, close, high, low, open, volume, instrument) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

    push_to_database(cursor=cursor, data=sheet, query=query, connection=cnx)
