import json
import os
from os.path import join
import shutil
class Person:

    def __init__(self):
        self.data = {
            "name" : str,
            "pic_path" : str,
            "Age" : int
        }
        os.makedirs("user_data", exist_ok=True)   
    def register(self, name, age, pic_path):
        #for i in range(len(pic_path)):
        new_path = pic_path.replace('img', name)
        new_path = new_path.replace('picture', 'Auth')
        print('old ',pic_path)
        print('new ',new_path)
        shutil.copy(pic_path, new_path)
        self.data = {
            "name" : name,
            "pic_path" : pic_path,
            "Age" : age
        }
        file_name = self.data["name"]
        with open(join("./Auth", f"{file_name}.json"), "w") as f:
            json.dump(self.data, f)
