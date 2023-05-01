from models.category import Category
from models.customer_transaction import CustomerTransaction
from models.merchant import Merchant

import repositories.category_repository as category_repository
import repositories.customer_transaction_repository as customer_transaction_repository 
import repositories.merchant_repository as merchant_repository

customer_transaction_repository.delete_all()
category_repository.delete_all()
merchant_repository.delete_all()

merchant1 = Merchant("Starbucks")
merchant_repository.save(merchant1)
merchant2 = Merchant("Lothian Buses")
merchant_repository.save(merchant2)
merchant3 = Merchant("Tesco")
merchant_repository.save(merchant3)

category1 = Category("Food and drink")
category_repository.save(category1)
category2 = Category("Transport")
category_repository.save(category2)
category3 = Category("Groceries")
category_repository.save(category3)

customer_transaction_1 = CustomerTransaction("Coffee", 3.50, merchant1, category1)
customer_transaction_repository.save(customer_transaction_1)
customer_transaction_2 = CustomerTransaction("Day ticket", 5, merchant2, category2)
customer_transaction_repository.save(customer_transaction_2)
customer_transaction_3 = CustomerTransaction("Eggs", 2, merchant3, category3)
customer_transaction_repository.save(customer_transaction_3)