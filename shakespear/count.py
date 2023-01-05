from decorateur import log_execution_time
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

@log_execution_time
def count_words(file_path):
    with open(file_path, 'r') as f:
        lines = f.read()

        words = lines.split()

        word_counts = {}

        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1


@log_execution_time
def count_word_2(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        
        Counter(content.split())


def comparison(file_path):
    for i in range(2):
        print(i)
        time_1 = []
        time_2 = []

        dict = count_words(file_path)
        counter =count_word_2(file_path)

        time_1.append(float(dict))
        time_2.append(float(counter))

        i = i+1

        

    print(f"Mean of counting using dictionnary is {np.mean(time_1)}")
    print(f"Mean of counting using python's counter is {np.mean(time_2)}")
    print(f"Variance of counting using dictionnary is {np.var(time_2)}")
    print(f"Variance of counting using python's counter is {np.var(time_2)}")

    fig,axs = plt.subplots(2)
    axs[0].plot(time_1)
    axs[1].plot(time_2)
    plt.show()

if __name__ == "__main__":

    comparison('./shakespear.txt')