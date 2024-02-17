import random
import time

from botpy import BotAPI

def determine_img(user_id:int) -> str:
    url_list=["https://i0.imgs.ovh/2024/02/14/oHsCt.png","https://i0.imgs.ovh/2024/02/14/oHx6m.png"]
    random.seed(user_id * time.time() // 60)
    return random.choice(url_list)
    

