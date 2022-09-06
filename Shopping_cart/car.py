class Car:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        car = self.session.get("car")
        if not car:
            car=self.session["car"]={}
            
        self.car=car

    def saveCar(self):
        self.session["car"]=self.car
        self.session.modified=True
        
    def addProduct(self, product):
        if (str(product.id) not in self.car.keys()):
            self.car[product.id]={
                "product_id": product.id,
                "name": product.productName,
                "price": product.price,
                "amount": 1,
                "image": product.image.url
            }
            self.saveCar()

        else: 
            for key, value in self.car.items():
                if key==str(product.id):
                    value["amount"] = value["amount"] + 1
                    value["price"] =  value["price"] + product.price
                    break
            self.saveCar()


        
    def delete(self, product):
        product.id= str(product.id)
        if product.id  in self.car:
            del self.car[product.id]
            self.saveCar()

    def restProduct(self, product):
        if(str(product.id)  not in self.car.keys()):

            self.car[product.id]={
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "amount": 1,
                "image": product.image.url
                 }
            self.saveCar()

        else: 
            for key, value in self.car.items():
                if key==str(product.id):
                    value["amount"] = value["amount"] - 1
                    value["price"] =  value["price"] - product.price
                    if value["amount"] < 1:
                        self.delete(product)
                    break
            self.saveCar()

    def cleanCar(self):
        self.session["car"]={}
        self.session.modified=True
        #self.saveCar()


        