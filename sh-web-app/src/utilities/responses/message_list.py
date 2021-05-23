message_list = {
    "VENDOR" : {
        "ERROR": {
            "INCOMPLETE_DATA"               : "Missing required parameters.",
            "INVALID_DATA"                  : "data is invalid",
            "VENDOR_DOES_NOT_EXIST"         : "Vendor does not exists.",
            "PRODUCT_DOES_NOT_EXIST"        : "product type does not exists",
            "ITEM_TYPE_DOES_NOT_EXIST"      : "item_type does not exists",
            "VENDOR_TYPE_DOES_NOT_EXIST"    : "Vendor Type does not exists.",
            "INSERT_ERR"                    : "Something went wrong in inserting vendor. Error: {}",
            "UPDATE_ERR"                    : "Something went wrong in updating vendor. Error: {}",
            "VIEW_ERR"                      : "Something went wrong in viewing vendor. Error: {}",
            "LIST_ERR"                      : "Something went wrong in listing vendor. Error: {}",
            "DUPLICATE_ENTRY"               : "provided name already exists.",
            "VENDOR_SHIP_DOESNOT_EXISTS"    : "vendor_id or v_shipping_id is invalid",
            "CONTACT_DELETE_ERR"            : "Something went wrong in deleting vendor contact. Error: {}"
        },
        "SUCCESS": {
            "DATA_CREATE"   : "Data created successfully.",
            "DATA_UPDATE"   : "Data updated successfully",
            "CONTACT_DELETE": "Vendor contact deleted successfully",
            "DATA_SUCCESS"  : "success"
        }
    },
    "ITEM" : {
        "ERROR": {
            "PRODUCT_DOES_NOT_EXIST"        : "product type does not exists",
            "INCOMPLETE_DATA"               : "Missing required parameters.",
            "INVALID_DATA"                  : "Data is invalid",
            "VENDOR_DOES_NOT_EXIST"         : "Vendor does not exists.",
            "ITEM_DOES_NOT_EXIST"           : "Item does not exists.",
            "ITEM_TYPE_DOES_NOT_EXISTS"     : "item type does not exists",
            "ITEM_SUBTYPE_DOES_NOT_EXISTS"  : "item sub-type does not exists",
            "INSERT_ERR"                    : "Something went wrong in inserting item. Error: {}",
            "UPDATE_ERR"                    : "Something went wrong in updating item. Error: {}",
            "DELETE_ERR"                    : "Something went wrong in deleting item. Error: {}",
            "VIEW_ERR"                      : "Something went wrong in viewing item. Error: {}",
            "UPLOAD_IMG"                    : "Something went wrong in uploading item image. Error: {}",
            "DELETE_IMG_ERR"                : "Something went wrong in deleteing item image. Error: {}",
            "LIST_ERR"                      : "Something went wrong in listing item.",
            "DUPLICATE_ENTRY"               : "provided name already exists.",
            "VENDOR_MAP_DOSES_NOT_EXISTS"   : "No vendor mapped to this item."
        },
        "SUCCESS": {
            "DATA_CREATE"           : "Data created successfully.",
            "DATA_UPDATE"           : "Data updated successfully",
            "DATA_DELETION"         : "Data deleted successfully",
            "DATA_SUCCESS"          : "data retrieved successfully",
            "UPLOAD_IMG"            : "image uploaded successfully.",
            "DELETE_IMG"            : "image deleted successfully.",
            "VENDOR_MAPPING_ADD"    : "New Vendor mapped successfully"
        }
    },
    "USER" : {
        "ERROR": {
            "LOGIN_ERR"                 : "Something went wrong when logging in. Error: {}",
            "INSERT_ERR"                : "Something went wrong in creating user. Error: {}",
            "VIEW_ERR"                  : "Something went wrong in viewing user. Error: {}",
            "INCOMPLETE_DATA"           : "Missing required parameters.",            
            "INVALID_DATA"              : "data is invalid",
            "INVALID_EMAIL"             : "please provide valid email address.",
            "INVALID_PASSWORD"          : "provided password is very weak, min 8 characters required.",
            "LIST_ERR"                  : "Something went wrong in listing users. Error: {}",
            "TOKEN_MISSING_ERR"         : "Token is missing!",
            "TOKEN_INVALID_ERR"         : "Token is invalid!",
            "REFRESH_TOKEN_MISSING_ERR" : "Refresh Token is missing!",
            "REFRESH_TOKEN_INVALID_ERR" : "Refresh Token is invalid!",
            "REFRESH_TOKEN_ERR"         : "Something went wrong in generating Refresh token. Error: {}",
            "PERMISSION_DENIED"         : "Permission denied! User cannot perfrom this action.",
            "DUPLICATE_EMAIL_ID"        : "Username with provided email_id already exists.",
            "USER_DOES_NOT_EXISTS"      : "User with provided email_id doesnot exists."
        },
        "SUCCESS": {
            "DATA_INSERT"           : "user created successfully.",
            "DATA_SUCCESS"          : "data retrieved successfully"
        }
    },
    "CLEARLY_PRODUCT" : {
        "ERROR" : {
            "INSERT_ERR"                    : "Something went wrong in creating clearly product. Error: {}",
            "DUPLICATE_ENTRY"               : "provided clearly product name already exists.",
            "READ_ERROR"                    : "Provide product id is not present, please give a valid one.",
            "UPDATE_ERR"                    : "Something went wrong in updating clearly product. Error: {}",
            "DELETE_ERR"                    : "Something went wrong in deleting clearly product. Error: {}"
        },
        "SUCCESS":{
            "DATA_CREATE"                    : "New clearly product created successfully.",
            "READ_CLEARLY_PRODUCT"           : "Data retrieved successfully",
            "DATA_UPDATE"                    : "Updated data for clearly product successfully",
            "DELETE_SUCCESS"                 : "Deleted data for clearly product successfully"
        }
    },
    "COST_CLEARLY_PRODUCT" : {
            "ERROR" : {
                "INSERT_ERR"                    : "Something went wrong in creating clearly product. Error: {}",
                "DUPLICATE_ENTRY"               : "Provided clearly product name already exists.",
                "READ_ERROR"                    : "Provide product id is not present, please give a valid one.",
                "INVALID_INPUT_ERROR"           : "Please provide valid product_id.",
            },
            "SUCCESS":{
                "DATA_CREATE"                    : "Created Successfully.",
                "READ_CREARLY_PRODUCT"           : "Data Retrieved Successfully"
            }
    },
    "SEARCH" : {
            "ERROR" : {               
                "READ_ERROR"                    : "Please provide valid word for search."
               
            },
            "SUCCESS":{  
                "READ"                          : "Data Retrieved Successfully",
                "EMPTY_DATA_LIST"               : "Search result not found !"             
                
            }
    },
}