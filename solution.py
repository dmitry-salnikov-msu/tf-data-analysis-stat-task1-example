import pandas as pd
import numpy as np


chat_id = 626925789 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x = (x + 46)/10
    return x.mean() # Ваш ответ
