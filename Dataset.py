

import csv


class Dataset:
    def process_dataset(self, search_values):
        with open('resources/xyz_car_sale_chatbot.csv', newline='') as chat_bot_data_set:
            questions_set = csv.reader(chat_bot_data_set)
            response = {"MATCHING_COUNT": 0, "DATA_ROW": "sorry"}
            word_count_tag = []
            for questions in questions_set:
                found_word_count = 0
                inputs = questions[0].split(":")
                for search_inputs in inputs:
                    for value in search_values:
                        words_of_dataset = search_inputs.split()
                        for word in words_of_dataset:
                            if word.lower() == value.lower():
                                found_word_count = found_word_count + 1
                word_count_tag.append({"MATCHING_COUNT": found_word_count, "DATA_ROW": questions})

            for search_data in word_count_tag:
                if search_data["MATCHING_COUNT"] >= 1:
                    if response["MATCHING_COUNT"] <= search_data["MATCHING_COUNT"]:
                        response = search_data

            return response
