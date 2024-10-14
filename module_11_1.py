import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
from time import time
#В качестве тренировочного набора данных будем использовать «Отчет об уровне счастья» в разных странах за 2019 год
# (World Happiness Report)


class WHR:
    df = pd.read_csv('2019.csv')
    countries = df["Country or region"].head(10)  # Например, первые 10 стран
    happiness_scores = df["Score"].head(10)

    t = time()
    print(f"Результат итератора: {sum(x ** 0.5 for x in range(10 ** 7))}.")
    print(f"{time() - t} с.")
    t = time()
    print(f"Результат numpy: {np.sqrt(np.arange(10 ** 7)).sum()}.")
    print(f"{time() - t} с.")

    line = plt.plot(countries, happiness_scores)
    plt.setp(line, linestyle='--')
    # Построение столбчатого графика
    plt.figure(figsize=(10, 6))
    plt.bar(countries, happiness_scores, color='lightgreen')
    plt.show()



