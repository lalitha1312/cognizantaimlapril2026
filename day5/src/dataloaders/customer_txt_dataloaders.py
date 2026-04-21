from src.dataloaders.customer_data_loaders import CustomerDataLoader
from src.stores.customerstore_imp import CustomerStoreImp
from src.models.customer import Customer
from src.models.full_name import FullName


class CustomerTXTDataLoader(CustomerDataLoader):

    def load_data(self, file_path, customer_store: CustomerStoreImp):
        with open(file_path, 'r') as f:
            content = f.read()

        # Split records by blank lines
        records = content.strip().split("\n\n")

        for record in records:
            lines = record.strip().split("\n")
            data = {}
            for line in lines:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()

            # Use the actual keys from the TXT file
            customer_id = int(data['CustID'])
            first_name = data['FirstName']
            last_name = data['LastName']
            email = data['Email']
            phone_number = data['PhoneNumber']

            full_name = FullName(first_name=first_name, last_name=last_name)
            customer = Customer(
                customer_id=customer_id,
                full_name=full_name,
                email=email,
                phone=phone_number
            )
            customer_store.add_customer(customer)

        return customer_store.get_all_customers()
