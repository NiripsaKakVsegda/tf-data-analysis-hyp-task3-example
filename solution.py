import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 440047378

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.09
    _, p_value = ttest_ind(x, y)
    return p_value < alpha
