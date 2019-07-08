import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['T', 'C', 'G', 'A']
men_means = [20, 34, 30, 35]
women_means = [25, 32, 34, 20]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Hemoglobina de Homo sapiens (HBB) mRNA')
rects2 = ax.bar(x + width/2, women_means, width, label='Proteína tumoral homo sapiens (p53) mRNA')

ax.set_ylabel('Score')
ax.set_xlabel('Nucleotídios')
ax.set_title('Pareamento de nucleotídios')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()

