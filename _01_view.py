# Front page

def front_page():
    print("+++++++++++재고품목 관리 시스템+++++++++++")
    print("품목 관리 메뉴얼++++++++++++++++++++++++++")
    print("1번: 제품 등록")
    print("2번: 제품 목록")
    print("3번: 제품 수정")
    print("4번: 제품 삭제")
    print("5번: 제품 검색")
    print("0번: 시스템 종료")

# Message 출력
def message_display(message):
    print(message)

# product_list 출력
def product_list_display(product_list):
    print("******Product 목록 출력******")
    for value in product_list:
        print("{}".format(str(value)))

# Product_entity 출력
def product_entity_display(product_entity):
    print("{} 상세정보: {}".format(product_entity.tag, str(product_entity)))

# Product_entity 정보 입력
def input_product_info():
    name = input("product name: ")
    volume = input("product volume: ")
    location = input("product location: ")
    price = input("poduct price: ")
    return name, volume, location, price

# tag 정보 입력
def input_tag():
    tag = input("product tag: ")
    return tag

# select 정보 입력
def select_info():
    info = input("메뉴얼 선택")
    return info