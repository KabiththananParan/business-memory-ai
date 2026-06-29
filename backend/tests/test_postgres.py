import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="business_memory_ai",
    user="business_user",
    password="business123"
)

print("Postgres Connected")
conn.close()