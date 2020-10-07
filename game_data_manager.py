# ================================================================================================
# |------------------------------------={ Entropy Engine }=--------------------------------------|
# ================================================================================================
#
#                                   Programmers : Joseph Coppin
#
#                                     File Name : game_data_manager.py
#
#                                       Created : September 06, 2020
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
import pickle
import os
#
# ------------------------------------------------------------------------------------------------
#
#                           Controls saving and loading data to files.
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================

game_data = []


def new_file(name):
    file = File(str(name))
    game_data.append(file)
    return file


def get_file(file):
    if type(file) == int:
        return game_data[file]
    else:
        for file in game_data:
            if file.name == str(file):
                return file


class File:
    def __init__(self, name):
        self.name = name

        self.data = None

    def init(self):
        self.save()

    def save(self):
        with open(f'{self.name}.txt', 'wb') as pickle_file:
            pickle.dump(self.data, pickle_file)

    def load(self):
        if os.path.getsize(f'{self.name}.txt') > 0:
            try:
                with open(f'{self.name}.txt', 'rb') as pickle_file:
                    self.data = pickle.load(pickle_file)
            except FileNotFoundError:
                raise FileNotFoundError(f'File {self.name} does not exist. Please initialise before loading.')
