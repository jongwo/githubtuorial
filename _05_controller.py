from _01_view import message_display, input_product_info, product_list_display, product_entity_display
from _00_exception import DuplicateException, RecordNotFoundException
import _04_service

class ProductController:

    def register_controller(self, ProductEntity):
        if ProductEntity.tag == "" or len(ProductEntity.tag) ==0 :
            message_display("tag error")
        else:
            #business method delegation
            bm = _04_service.ProductService()
            message = bm.register(ProductEntity)
            #view select
            message_display(message)

    def get_all_entity_controller(self):
        bm = _04_service.ProductService()
        ai_list = bm.get_all_entity()
        product_list_display(ai_list)

    def update_controller(self,ProductEntity):
        #email valid check - regular express사용  email형식 체크
        if ProductEntity.tag == "" or len(ProductEntity.tag) ==0 :
            #error view select
            message_display("tag error")
        else:
            #business method delegation
            bm = _04_service.ProductService()
            message = bm.entity_update(ProductEntity)
            #view select
            message_display(message)
    
    def delete_controller(self, tag):
        if tag == "" or len(tag) == 0 :
            message_display("tag error") 
        else:
            bm =_04_service.ProductService()
            message = bm.entity_remove(tag)
            message_display(message)

    def get_entity_controller(self,tag):
        if tag == "" or len(tag) == 0 :
            message_display("tag error")        
        else:
            bm =_04_service.ProductService()
            ProductEntity = bm.get_product_entity(tag)
            if (type(ProductEntity)) == 'str':
                product_entity_display(ProductEntity)
            else:
                print("no info")
#            if ProductEntity != None:
#               product_entity_display(ProductEntity)
#            else:
#               print("no info") 
    
    def close(self):
        bm=_04_service.ProductService()
        bm.close()
    


            