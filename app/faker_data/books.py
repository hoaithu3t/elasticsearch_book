import json
import random
import string

kind_of_books = ["Tiểu thuyết", "Truyện ngắn", "Sách giáo khoa", "Sách tham khảo", "Truyện kiếm hiệp",
                 "Truyện trinh thám", "Sách ngoại ngữ"]
publishers = ["Kim Đồng", "Giáo dục", "Sư phạm", "Nhã nam", "Cá chép", "Chim sẻ", "Chim cánh cụt"]


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def unique_name():
    return randomString()


def number_of_pages():
    return random.randint(20, 1000)


def name():
    title_book = "Sách " + random.choice(kind_of_books) + " " + unique_name()
    return title_book


def quantity_in_stock():
    return random.randint(0, 100) * random.randint(0, 100) * random.randint(0, 100)


def author():
    return {
        "id": str(random.randint(100000, 1000000 - 1)) + randomString(10),
        "name": randomString(6) + ' ' + randomString(4)
    }


def publisher():
    return random.choice(publishers)


def price_details():
    import_price = random.randint(10000, 1500000)
    final_price = import_price + random.randint(20000, 2000000)
    promotion_price = random.randint(import_price, final_price)
    type = random.randint(0, 1)
    if (type == 0):
        promotion_price = final_price
    discount = final_price - promotion_price
    discount_percent = round(discount / final_price, 2)
    return {
        "import_price": import_price,
        "final_price": final_price,
        "promotion_price": promotion_price,
        "discount": discount,
        "discount_percent": discount_percent
    }


class Faker():
    def __init__(self):
        with open('./app/faker_data/categories.json', encoding='utf-8') as categories_file:
            self.categories = json.load(categories_file)

        with open('./app/faker_data/attributes.json', encoding='utf-8') as attributes_file:
            self.attributes = json.load(attributes_file)
        with open('./app/faker_data/channels.json', encoding='utf-8') as channels_file:
            self.channels = json.load(channels_file)
        self.quantity_fields = ["last_1_week", "last_2_week", "last_3_week", "last_1_month",
                                "last_2_month", "last_3_month", "last_1_year"]

    def categories(self):
        return random.choice(self.categories)

    def attributes(self):
        new_attributes = [*self.attributes]
        # Bìa
        new_attributes[0]['values'][0]['value'] = random.choice(["Bìa cứng", "Bìa mềm"])
        # Kích thước
        new_attributes[1]['values'][0]['value'] = random.choice(["A3", "A4", "A5"])

        return new_attributes

    def channels(self):
        return random.choices(self.channels)

    def quantity(self):
        cur = 0
        quantity = {}
        for field in self.quantity_fields:
            cur += random.randint(0, 1000)
            quantity[field] = cur
        return quantity

    def book(self):
        return {
            "sku": str(random.randint(100000, 1000000 - 1)) + randomString(10),
            "name": name(),
            "attributes": self.attributes(),
            "categories": self.categories(),
            "description": randomString(30),
            "rating": round(random.random(), 2) + random.randint(0, 4),
            "quantity_in_stock": quantity_in_stock(),
            "number_of_pages": number_of_pages(),
            "publisher": publisher(),
            "author": author(),
            "channels": self.channels(),
            "quantity": self.quantity(),
            **price_details()
        }
