class ProductEntity:
    # 생성자 정의: member variable: name, volume, location, price, tag  초기화
    def __init__(self, name, volume, location, price, tag):
        self.name=name
        self.volume=volume
        self.location=location
        self.price=price
        self.tag=tag

    # tag 정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, tag):
        if (self.tag == tag):
            return True
        else:
            return False

    def __str__(self):
        return "{}:{}:{}:{}:{}".format(self.name, self.volume, self.location, self.price, self.tag)

    