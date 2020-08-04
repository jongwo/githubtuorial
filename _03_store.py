import pymysql.cursors
from _02_domain import ProductEntity

class ProductStore:
    connection = None

    # db 연결
    def __init__(self):
        ProductStore.connection = pymysql.connect(host = 'localhost',
        port = 3306,
        user = 'aiadmin',
        password = 'password',
        db = 'aidb',
        charset = 'utf8',
        cursorclass = pymysql.cursors.DictCursor)

    # db 종료
    def close(self):
        ProductStore.connection.close()

    def insert(self, ProductEntity):
        # conncection pool로부터 connection 객체 얻기
        try:
            with ProductStore.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `product` (`name`, `volume`, `location`, `price`, `tag`) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (ProductEntity.name, ProductEntity.volume, ProductEntity.location, ProductEntity.price, ProductEntity.tag))
                ProductStore.connection.commit()
        finally:
            # connection pool에 자원 반납하기
            pass

    def select_all(self):
        try:
            with ProductStore.connection.cursor() as cursor:
                sql = "SELECT * FROM `product`"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def update(self, ProductEntity):
        try:
            with ProductStore.connection.cursor() as cursor:
                # Create a new record
                sql = "UPDATE `product` SET `name`=%s, `volume`=%s, `location`=%s, `price`=%s WHERE `tag`=%s"
                cursor.execute(sql, (ProductEntity.name, ProductEntity.volume, ProductEntity.location, ProductEntity.price, ProductEntity.tag))
                ProductStore.connection.commit()
        finally:
            pass

    def delete(self, tag):
        try:
            with ProductStore.connection.cursor() as cursor:
                # Create a new record
                sql = "DELETE FROM `product` WHERE `tag`=%s"
                cursor.execute(sql, (tag))
                ProductStore.connection.commit()
        finally:
            pass
        

    def select_by_tag(self, tag):
        try:
            with ProductStore.connection.cursor() as cursor:
                sql = "SELECT * FROM `product` WHERE `tag`=%s"
                cursor.execute(sql, (tag))
                result=cursor.fetchone()
        finally:
            pass
        return result

# # 코드확인
# test = ProductStore()
# test.insert(ProductEntity("런닝머신",28,'서울',1000000,"sdfssdvsc"))
# result = test.select_by_tag("sdfssdvsc")
# print(result)