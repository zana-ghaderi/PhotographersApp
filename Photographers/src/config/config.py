import os
POSTGRES_CONFIG = {
    "dbname": "intuit_db",
    "user": "zana",
    "password": "intuit_password",
    "host": "localhost",
    "port": "5432"
}

CASSANDRA_CONFIG = {
    "contact_points": os.getenv("CASSANDRA_CONTACT_POINTS", "localhost").split(','),
    "port": int(os.getenv("CASSANDRA_PORT", 9042)),
    "keyspace": os.getenv("CASSANDRA_KEYSPACE", "intuit_db")
}


KAFKA_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'intuit-producer'
}

KAFKA_CONFIG_CONSUMER = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'book_exchange_group',
    'auto.offset.reset': 'earliest',
    'session.timeout.ms': 6000,
    'heartbeat.interval.ms': 3000
}

REDIS_CONFIG = {
    'host': 'localhost',
    'port': '6379',
    'db': '0'
}
