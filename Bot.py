
import sys
import random

from datetime import datetime, date

from Dataset import Dataset
from  Database import Database

data_set = Dataset()
xyz_data_base = Database()


class Bot:
    def get_current_date_time(self, type):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%m/%d/%Y")
        if type == "get_time":
            return current_time
        elif type == "get_date":
            return current_date

    def identify_input_name(self, splitted_question, response, question):
        random_respones = random.choice(response)
        if "is" in splitted_question:
            return random_respones + question.split("is", 1)[1]
        elif "am" in splitted_question:
            return random_respones + question.split("am", 1)[1]
        else:
            return "Hi how can i help you"


    def process_question(self, question):
        user_queston = question
        splitted_question = user_queston.split()
        search_result = data_set.process_dataset(splitted_question)
        if search_result["DATA_ROW"] == "sorry":
            print("|XYZ BOT : Sorry, i can't understand")
            print("|-------------------------------------------------------|")
        else:
            response = search_result["DATA_ROW"][1].split(":")
            tag = search_result["DATA_ROW"][2]
            if tag == "exit":
                print("|XYZ BOT : " + random.choice(response))
                sys.exit()
            elif tag == "greeting" or tag == "bye":
                print("|XYZ BOT : " + random.choice(response))
                print("|-------------------------------------------------------|")
            elif tag == "get_time" or tag == "get_date":
                date_time = self.get_current_date_time(tag)
                print("|XYZ BOT : " + random.choice(response) + " " + date_time)
                print("|-------------------------------------------------------|")
            elif tag == "show_car_brands":
                print("|XYZ BOT : " + response[0])
                car_brands = xyz_data_base.get_car_brands()
                for brand in car_brands:
                    print("|" + brand[0])
                print("|-------------------------------------------------------|")
            elif tag == "contact":
                print("|XYZ BOT : " + response[0])
                contact_details = xyz_data_base.get_xyz_company_details()
                print("|Address : " + contact_details[0][1])
                print("|Contact : " + contact_details[0][2])
                print("|Email : " + contact_details[0][3])
                print("|-------------------------------------------------------|")
            elif tag == "get_user_name":
                name_response = self.identify_input_name(splitted_question, response, question)
                print("|XYZ BOT : " + name_response)
            elif tag == "show_my_name":
                print("|XYZ BOT : " + response[0])
            elif tag == "show_cars":
                print("|XYZ BOT : " + response[0])
                cars_response = xyz_data_base.xyz_cars()
                for cars in cars_response:
                    print(
                        "|Name : " + cars[1] + "\t| Brand :" + cars[2] + "\t| Color :" + cars[3] + "\t| Speed :" + str(
                            cars[4]) + "KMph" + "\t| Price : USD " + str(cars[5]))
                print("|-------------------------------------------------------|")
            elif tag == "search_by_brand":
                print("|XYZ BOT : " + response[0] + " cars")
                cars_response = xyz_data_base.xyz_search_car_by_brand(response[0])
                for cars in cars_response:
                    print(
                        "|Name : " + cars[1] + "\t| Brand :" + cars[2] + "\t| Color :" + cars[3] + "\t| Speed :" + str(
                            cars[4]) + "KMph" + "\t| Price : USD " + str(cars[5]))
                print("|-------------------------------------------------------|")
            elif tag == "order_by_speed":
                print("|XYZ BOT : " + response[0] + " cars")
                cars_response = xyz_data_base.xyz_cars_by_speed()
                for cars in cars_response:
                    print(
                        "|Name : " + cars[1] + "\t| Brand :" + cars[2] + "\t| Color :" + cars[3] + "\t| Speed :" + str(
                            cars[4]) + "KMph" + "\t| Price : USD " + str(cars[5]))
                print("|-------------------------------------------------------|")
            elif tag == "car_price":
                response = response[0]
                price = [int(i) for i in question.split() if i.isdigit()]
                price_response = xyz_data_base.xyz_car_price(response, price)

                if len(price_response) >= 1:
                    print("|XYZ BOT : Here is the cars i found for your price")
                    for cars in price_response:
                        print("|Name : " + cars[1] + "\t| Brand :" + cars[2] + "\t| Color :" + cars[
                            3] + "\t| Speed :" + str(
                            cars[4]) + "KMph" + "\t| Price : USD " + str(cars[5]))
                else:
                    print("|XYZ BOT : Sorry we dont have any cars for your price")
                print("|-------------------------------------------------------|")
            else:
                print("|XYZ BOT : " + response[0])
                print(tag)
