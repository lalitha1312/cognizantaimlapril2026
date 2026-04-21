#create customer store implementation from customer store abstract class

from src.stores.customerstore import CustomerStore
class CustomerStoreImp(CustomerStore):
    
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer


    def get_all_customers(self):
        return list(self.customers.values())

    def get_customer(self, customer_id):
        for customer in self.customers.values():
            if customer.customer_id == customer_id:
                return customer
        raise CustomerNotFound(customer_id)


    def update_customer(self, customer_id, customer):
        if customer_id in self.customers:
            self.customers[customer_id] = customer
        else:
            raise CustomerNotFound(customer_id)


    def delete_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            return True
        return False