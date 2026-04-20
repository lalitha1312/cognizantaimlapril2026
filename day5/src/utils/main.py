import os
import random
import sys
 
# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from src.configurations.conf import Config
from src.dataloaders.customer_csv_dataloader import CustomerCSVDataLoader
from src.stores.customerstore_imp import CustomerStoreImp

def display_customers(customer_store):
   config = Config()
   env=config.app_env
   if env== "development":
      data_loader = CustomerCSVDataLoader()
      data_loader.load_data(config.resource_path,customer_store)
      for customer in customer_store.get_all_customers():
          print(customer)

if __name__ == "__main__":
    customer_store = CustomerStoreImp()
    display_customers(customer_store)

