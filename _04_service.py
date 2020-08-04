from _00_exception import DuplicateException, RecordNotFoundException
from _02_domain import ProductEntity
from _03_store import ProductStore

class ProductService:
    # ProductEntity 정보를 저장하는 클래스 변수
    db = ProductStore()

    # tag 존재여부
    def is_exist(self,tag):
        result = ProductService.db.select_by_tag(tag)
        return result
  
    # 제품 등록 : tag 존재여부 체크
    def register(self,ProductEntity):
        result = self.is_exist(ProductEntity.tag)
        if not bool(result):
            ProductService.db.insert(ProductEntity)
            return ProductEntity.name+"님 등록되었습니다."
        else:
            try:
                raise DuplicateException(ProductEntity.name)  
            except DuplicateException as error:
                return str(error)

    # 제품 목록
    def get_all_entity(self):
        return ProductService.db.select_all()

    # 제품 정보 수정
    def entity_update(self,ProductEntity):
        result = self.is_exist(ProductEntity.tag)
        if bool(result):
            ProductService.db.update(ProductEntity)
            return ProductEntity.name+"님 정보수정 되었습니다."
        else:
            try:
                raise RecordNotFoundException(ProductEntity.name)
            except RecordNotFoundException as updateError:
                return str(updateError)

    # 제품 정보 삭제
    def entity_remove(self,tag):
        result = self.is_exist(tag)
        if bool(result):
            ProductService.db.delete(tag)
            return tag+" 삭제 되었습니다."
        else:
            try:
                raise RecordNotFoundException(tag)
            except RecordNotFoundException as removeError:
                return str(removeError)
           
    # 제품 상세 정보
    def get_product_entity(self,tag):
        result = self.is_exist(tag)
        if (bool(result)):
            return ProductEntity(result["name"], result["volume"], result["location"], result["price"], result["tag"])
        else:
            try:
                raise RecordNotFoundException(tag)
            except RecordNotFoundException as searchError:
                return str(searchError)


    def close(self):
        ProductService.db.close()