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
        for i in range(len(self.customers)):
            if self.customers[i].id == customer_id:
                self.customers[i] = customer
                return 
        raise CustomerNotFound(customer_id)


    def delete_customer(self, customer_id):
        for i in range(len(self.customers)):
            if self.customers[i].id == customer_id:
                del self.customers[i]
                return True
        return False