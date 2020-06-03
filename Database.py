

import mysql.connector


class Database:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="xyz_car_sale")

    def get_car_brands(self):
        my_brands = self.mydb.cursor()
        query = "SELECT DISTINCT car_brand FROM cars"
        my_brands.execute(query)
        brand_result = my_brands.fetchall()
        return brand_result

    def get_xyz_company_details(self):
        cotact_details = self.mydb.cursor()
        query = "SELECT * FROM contact_details LIMIT 1"
        cotact_details.execute(query)
        contact_result = cotact_details.fetchall()
        return contact_result

    def xyz_cars(self):
        my_cars = self.mydb.cursor()
        query = "SELECT * FROM cars"
        my_cars.execute(query)
        cars_result = my_cars.fetchall()
        return cars_result

    def xyz_search_car_by_brand(self, brand):
        car_by_brands = self.mydb.cursor()
        query = "SELECT * FROM cars WHERE car_brand like '%" + brand + "%'"
        car_by_brands.execute(query)
        cars_by_brand_result = car_by_brands.fetchall()
        return cars_by_brand_result

    def xyz_cars_by_speed(self):
        my_cars_speed = self.mydb.cursor()
        query = "SELECT * FROM `cars` ORDER BY `cars`.`speed` DESC"
        my_cars_speed.execute(query)
        cars_result_by_speed = my_cars_speed.fetchall()
        return cars_result_by_speed

    def xyz_car_price(self, type, price):
        my_cars_price = self.mydb.cursor()
        if type == "grater":
            query = "SELECT * FROM `cars` WHERE price >= '" + str(price[0]) + "' ORDER BY `cars`.`speed` DESC"
        elif type == "lower":
            query = "SELECT * FROM `cars` WHERE price <= '" + str(price[0]) + "' ORDER BY `cars`.`speed` DESC"

        my_cars_price.execute(query)
        cars_result_by_speed = my_cars_price.fetchall()
        return cars_result_by_speed
