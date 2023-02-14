from data.data import Person
from faker import Faker

faker_ru = Faker('ru-Ru')
Faker.seed()


def generated_person():
    yield Person(
        full_name=f"{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name()}",
        email=f"{faker_ru.email()}",
        current_address=f"{faker_ru.address()}",
        permanent_address=f"{faker_ru.address()}",
    )
