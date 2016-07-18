# -*- coding: utf-8 -*-
import time
import random


def get_random_str():
    time_test = time.time()
    time_int = int(time_test * 10)
    time_str = str(time_int)
    random_number = random.randrange(101, 999)
    random_str = str(random_number)
    final_random_str = time_str + random_str

    return final_random_str
