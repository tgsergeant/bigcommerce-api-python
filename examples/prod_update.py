from settings import *
import sys
import logging
from pprint import pprint
from Bigcommerce.api import ApiClient

logging.basicConfig(level=logging.DEBUG, 
                    stream=sys.stdout,
                    format='%(asctime)s %(levelname)-8s[%(name)s] %(message)s',
                    datefmt='%m/%d %H:%M:%S')
log = logging.getLogger("main")

if __name__ == "__main__":
    log.debug("HOST %s, USER: %s" % (STORE_HOST, STORE_USERID))
    api = ApiClient(STORE_HOST, STORE_TOKEN, STORE_USERID)
    
    product = api.Products.get(14)
    
    print product.id, product.sku, product.name
    product.name = "My New Product"
    
    print product.id, product.name
    product.save()
    
    print product.id, product.name
    product.save()
    
    