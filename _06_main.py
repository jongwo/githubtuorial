import _05_controller
from _02_domain import ProductEntity
from _01_view import input_tag,front_page,select_info,message_display, input_product_info, product_list_display, product_entity_display
import _04_service
from _00_exception import DuplicateException, RecordNotFoundException


controller = _05_controller.ProductController()

while True:
    
    front_page()

    menu = select_info()
    if menu == '1':
        tag =input_tag()
        name,volume,location,price = input_product_info()        
        controller.register_controller(ProductEntity(name, volume, location, price, tag))
        
    elif menu == '2':
        controller.get_all_entity_controller()

    elif menu == '3':
        tag = input_tag()
        name,volume,location,price = input_product_info()
        controller.update_controller(ProductEntity(name, volume, location, price, tag))
   
    elif menu == '4':
        tag = input_tag()
        controller.delete_controller(tag)

    elif menu == '5':
        tag = input_tag()
        controller.get_entity_controller(tag)
               
    elif menu =='0':
        controller.close()
        break
    else:
        message_display("메뉴는 1,2,3,4,5 중 하나를 선택하시고 종료를 원하시면 0번을 선택하세요")
    continue