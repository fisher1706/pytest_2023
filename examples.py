from db import session
import tables
from sqlalchemy.sql.expression import desc


result_1 = session.query(tables.Films.film_id, tables.Films.title).first()
print(f"result_1: {result_1}")

result_2 = session.query(tables.Films.film_id, tables.Films.title).all()
print(f"result_2: {result_2}")

result_3 = session.query(
    tables.Films.film_id, tables.Films.title
).filter(tables.Films.film_id == 5).one_or_none()
print(f"result_3: {result_3}")

result_4 = session.query(
    tables.Films.film_id, tables.Films.title
).filter(
    tables.Films.film_id > 1,
    tables.Films.film_id < 100
).limit(1).offset(1).all()
print(f"result_4: {result_4}")

films_ids = session.query(tables.Films.film_id).filter(tables.Films.film_id > 0).subquery()
print(f"films_ids: {films_ids}")

result_5 = session.query(tables.Films.title).filter(tables.Films.film_id.in_(films_ids)).all()
print(f"result_5: {result_5}")

result_6 = session.query(
    tables.Films.film_id,
    tables.Films.title
).order_by(desc(tables.Films.title)).all()
print(f"result_6: {result_6}")


"""
Пример объекта на котором вы можете потренироваться, используя pydantic схемы.
Example of object for training with pydantic schemas.
"""

computer = {
    "id": 21,
    "status": "active",
    "activated_at": "2013-06-01",
    "expiration_at": "2040-06-01",
    "host_v4": "91.192.222.17",
    "host_v6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "detailed_info": {
        "physical": {
            "color": 'green',
            "photo": 'https://images.unsplash.com/photo-1587831990711-23ca6441447b?ixlib=rb-'
                     '1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZGVza3RvcCUyMGNvbXB1dGVyfGVufDB8fDB8fA%3D%3D&w=1000&q=80',
            "uuid": "73860f46-5606-4912-95d3-4abaa6e1fd2c"
        },
        "owners": [{
            "name": "Stephan Nollan",
            "card_number": "4000000000000002",
            "email": "shtephan.nollan@gmail.com",
        }]
    }
}
