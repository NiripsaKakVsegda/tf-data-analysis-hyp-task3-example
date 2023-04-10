import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 440047378

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.09
    stat, p = mannwhitneyu(x, y, alternative='greater')
    crit = len(x) * len(y)
    return stat > crit or p < alpha
