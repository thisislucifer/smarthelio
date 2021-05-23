from src.utilities.responses.message_list import message_list
import json
import re

class ValidateVendorInputs:
    def __init__(self, input_json):
        self.vendor_input_fields = (
            "name",
            "status","description",
            "address_1", "address_2",
            "city", "state", "website",
            "phone", "fax", "email_id",
            "vendor_discount", "contact_details"
        )
        self.vendor_contact_fields =(
            "name","title","phone_office",
            "phone_mobile","email_id","notes"
        )
        self.vendor_shipping_fields =(
            "note","description","price_per_item",
            "min_quantity","shipping","total_price"
        )
        self.input_json = json.loads(input_json)
        # self.input_json = input_json  #..(for testing)
    
    def validate(self):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        regex_2 = '^(0|[1-9]\d*)$'
        input_payload = self.input_json
        if not all (each_key in input_payload for each_key in self.vendor_input_fields):
            raise Exception(message_list['VENDOR']["ERROR"]["INCOMPLETE_DATA"])
        #check if vales are empty
        for each_key in self.vendor_input_fields:
            print(each_key)
            if not input_payload.get(each_key): 
                raise Exception(message_list['ITEM']["ERROR"]["INVALID_DATA"])
            else:
                pass

        if not all (each_key in input_payload['contact_details'][0] for each_key in self.vendor_contact_fields):
            raise Exception(message_list['VENDOR']["ERROR"]["INCOMPLETE_DATA"])
        #check if vales are empty
        for each_key in self.vendor_contact_fields:
            if not input_payload['contact_details'][0].get(each_key): 
                raise Exception(message_list['ITEM']["ERROR"]["INVALID_DATA"])
        
        #check the regex of vendor->
        if re.search(regex,input_payload['contact_details'][0]['email_id']):
            pass
        else:
            raise Exception(message_list['USER']["ERROR"]["INVALID_EMAIL"])
        # --
        if re.search(regex,input_payload['email_id']):
            pass
        else:
            raise Exception(message_list['USER']["ERROR"]["INVALID_EMAIL"])
        
        

        if not all (each_key in input_payload['shipping_details'][0] for each_key in self.vendor_shipping_fields):
            raise Exception(message_list['VENDOR']["ERROR"]["INCOMPLETE_DATA"])
        #check if vales are empty
        for each_key in self.vendor_shipping_fields:
            print(each_key)
            if not input_payload['shipping_details'][0].get(each_key): 
                raise Exception(message_list['ITEM']["ERROR"]["INVALID_DATA"])
            else:
                pass

    def validate_view_payload(self):
        regex = '^(0|[1-9]\d*)$'
        input_payload = self.input_json
        if not ( "vendor_id" in input_payload):
            raise Exception(message_list['VENDOR']["ERROR"]["INCOMPLETE_DATA"])
        if not input_payload.get('vendor_id').replace(" ",""):
            raise Exception(message_list['VENDOR']["ERROR"]["INVALID_DATA"])
        if re.search(regex,input_payload['vendor_id']):
            pass
        else:
            raise Exception(message_list['VENDOR']["ERROR"]["INVALID_DATA"])

    def validate_vendor_type_payload(self):
        input_payload = self.input_json
        if not ("product_type_id" and "name") in input_payload:
            raise Exception(message_list['VENDOR']["ERROR"]["INCOMPLETE_DATA"])
        #check if vales are empty-->
        for each_key in ("product_type_id","name"):
            if not input_payload.get(each_key): 
                raise Exception(message_list['VENDOR']["ERROR"]["INVALID_DATA"])
            else:
                pass
        
    def get_input_payload(self):
        return self.input_json
