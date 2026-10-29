
import psycopg2
from api_request import mock_fetch_data


def connect_to_db():
    print("Connecting to PostgreSQL database")

    conn = psycopg2.connect(
        host="db",
        port=5432,
        dbname="db",
        user="db_user",
        password="db_password"
    )

    return conn


def create_table(conn):
    print("Creating table if not exists")

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE SCHEMA IF NOT EXISTS dev;

                CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                    id SERIAL PRIMARY KEY,
                    city TEXT,
                    temperature FLOAT,
                    weather_descriptions TEXT,
                    wind_speed FLOAT,
                    time TIMESTAMP,
                    inserted_at TIMESTAMP DEFAULT NOW(),
                    utc_offset TEXT
                );
            """)

        # Nếu bảng đã tồn tại từ trước, bổ sung cột còn thiếu
        with conn.cursor() as cursor:
            cursor.execute("""
                ALTER TABLE dev.raw_weather_data
                ADD COLUMN IF NOT EXISTS weather_descriptions TEXT;
            """)

        conn.commit()
        print("Table was created successfully")

    except psycopg2.Error as e:
        conn.rollback()
        print(f"Failed to create table: {e}")
        raise


def insert_record(conn, data):
    print("Inserting weather data into the database")

    try:
        location = data["location"]
        weather = data["current"]

        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO dev.raw_weather_data (
                    city,
                    temperature,
                    weather_descriptions,
                    wind_speed,
                    time,
                    inserted_at,
                    utc_offset
                )
                VALUES (%s, %s, %s, %s, %s, NOW(), %s)
            """, (
                location["name"],
                weather["temperature"],
                weather["weather_descriptions"][0],
                weather["wind_speed"],
                location["localtime"],
                location["utc_offset"]
            ))

        conn.commit()
        print("Data successfully inserted")

    except (psycopg2.Error, KeyError, IndexError, TypeError) as e:
        conn.rollback()
        print(f"Error inserting data: {e}")
        raise


def main():
    conn = None

    try:
        data = mock_fetch_data()

        if not data:
            raise ValueError("No weather data returned from API")

        conn = connect_to_db()
        create_table(conn)
        insert_record(conn, data)

    except Exception as e:
        print(f"An error occurred during execution: {e}")

    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed")


if __name__ == "__main__":
    main()
