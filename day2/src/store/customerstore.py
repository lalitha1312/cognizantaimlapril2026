#customers 100 random customers

import faker
import typing

from store.customer import Customer
class CustomerStore:
    def __init__(self, num_customers: int):
        self.num_customers = num_customers
        self.customers = []
        self.faker = faker.Faker()

    def generate_random_customers(self):
        for _ in range(self.num_customers):
            name = self.faker.name()
            email = self.faker.email()
            dob = self.faker.date_of_birth()
            customer = Customer(name, email, dob)
            self.customers.append(customer)

    def get_customers(self) -> typing.List[Customer]:
        return self.customers