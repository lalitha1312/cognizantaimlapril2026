import pandas as pd
from src.dataloaders.customer_data_loaders import CustomerDataLoader
from src.stores.customerstore_imp import CustomerStoreImp
from src.models.customer import Customer
from src.models.full_name import FullName


class CustomerJSONDataLoader(CustomerDataLoader):

    def load_data(self, file_path, customer_store: 'CustomerStoreImp'):
        # Read JSON file into a DataFrame
        df = pd.read_json(file_path)

        for _, row in df.iterrows():
            customer_id = int(row['CustID'])
            first_name = row['FirstName']
            last_name = row['LastName']
            email = row['Email']
            phone_number = row['PhoneNumber']

            # Create Customer object
            customer = Customer(
                customer_id=customer_id,
                full_name=FullName(first_name=first_name, last_name=last_name),
                email=email,
                phone=phone_number
            )

            # Add to store
            customer_store.add_customer(customer)

        # Return list of dicts for convenience
        return df.to_dict(orient='records')
