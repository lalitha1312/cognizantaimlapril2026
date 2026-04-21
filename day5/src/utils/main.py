import os
import sys
from faker import Faker

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from src.configurations.conf import Config
from src.dataloaders.customer_csv_dataloader import CustomerCSVDataLoader
from src.dataloaders.customer_json_dataloaders import CustomerJSONDataLoader
from src.dataloaders.customer_txt_dataloaders import CustomerTXTDataLoader
from src.stores.customerstore_imp import CustomerStoreImp
from src.utils.pipeline_runner import PipelineRunner


def load_customers(**kwargs):
    config=Config()
    customerstore= kwargs['customerstore']
    env=config.app_env

    if env == "production":
        data_loader = CustomerJSONDataLoader()
        data_loader.load_data(config.resource_path, customerstore)
    if env == "development":
        data_loader = CustomerCSVDataLoader()
        data_loader.load_data(config.resource_path, customerstore)
    if env == "testing":
        data_loader = CustomerTXTDataLoader()
        data_loader.load_data(config.resource_path, customerstore)
    return customerstore


def display_customers(**kwargs):
    customerstore= kwargs['customerstore']

    for customer in customerstore.get_all_customers():
        print(f"customer_id: {customer.customer_id}")
        print(f"name: {customer.full_name.first_name} {customer.full_name.last_name}")
        print(f"email: {customer.email}")
        print(f"phone_no: {customer.phone}")
        print("-------------")
    return customerstore


def update_customers(**kwargs):
    customerstore = kwargs['customerstore']
    customer_id = kwargs['customer_id']
    customer = customerstore.get_customer(customer_id)
    fake= Faker()
    customer.full_name.first_name= fake.first_name()
    customer.full_name.last_name=fake.last_name()
    customer.email=fake.email()
    customer.phone=fake.random_int(min=100000, max=1000000)
    customerstore.update_customer(customer_id,customer)
    return customerstore

def get_customer_id(**kwargs):
    customerstore = kwargs['customerstore']
    customer_id = kwargs['customer_id']
    customer=customerstore.get_customer(customer_id)
    print(f"customer_id:{customer.customer_id}")
    print(f"name: {customer.full_name.first_name} {customer.full_name.last_name}")
    print(f"email: {customer.email}")
    print(f"phone_no: {customer.phone}")
    print("-------------")
    return customerstore
    
def delete_customer(**kwargs):
    customerstore = kwargs['customerstore']
    customer_id = kwargs['customer_id']
    result=customerstore.delete_customer(customer_id)
    if result:
        print(f"Customer with id {customer_id} deleted successfully.")
    else:
        print(f"Customer with id {customer_id} not found.")
    return customerstore


if __name__ == "__main__":
    customer_store = CustomerStoreImp()
    pipeline_runner = PipelineRunner()
    pipeline_runner.add_stage(load_customers)
    pipeline_runner.add_stage(display_customers)
    pipeline_runner.add_stage(update_customers)
    pipeline_runner.add_stage(get_customer_id)
    pipeline_runner.run(customerstore=customer_store, customer_id=201)
