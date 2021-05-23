import psycopg2
import psycopg2.extras
from src.utilities.database.db_models import *

#check and create table if doesnot exists ->
# ActivityLogs.check_table()
# Product.check_table()
# VendorType.check_table()
# ItemType.check_table()
# ItemSubType.check_table()
# Item.check_table()
# Vendor.check_table()
# VendorShippingDetails.check_table()
# VendorContactDetails.check_table()