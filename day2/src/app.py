# creatin entry point for application
import faker
from store.customerstore import CustomerStore
from view.customerview import CustomerView

"""
 creating entry point for application to display random name using faker library
"""


def check():
    """
    This function to display random name using faker library invoke customer store and view
    """
    customer_store = CustomerStore(num_customers=100)
    customer_store.generate_random_customers()
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()

if __name__ == "__main__":
    check()
