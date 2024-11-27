import json

from src.database.cassandra import get_cassandra_session
from src.models.photographer import Photographer


class DataLoader:

    @staticmethod
    def load_photographers():
        with open("/Users/zana/PycharmProjects/InterviewIntuit/pythonProject1/src/photographers.json", 'r') as file:
            data = json.load(file)

        if data:
            cassandra = get_cassandra_session()
            try:
                for p_dict in data:
                    p = Photographer(**p_dict)
                    query = """
                                INSERT INTO photographers (id, uid, first_name, last_name, address, event_type)
                                VALUES (%s, %s, %s, %s, %s, %s)
                            """
                    cassandra.execute(query, (
                        p.id,
                        p.uid,
                        p.first_name,
                        p.last_name,
                        json.dumps(p.address.dict()),
                        json.dumps(p.event_type.type)
                    ))
            except Exception as e:
                raise ValueError("Data is not valid", e)
            finally:
                return [Photographer(**p) for p in data]
