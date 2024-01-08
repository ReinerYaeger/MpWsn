import matplotlib.pyplot as plt
from scipy.stats import f_oneway

def anova():
    # Change the data
    loam = [3, 4, 4, 5]
    sandy = [6, 5, 2, 4]
    clay = [1, 7, 4, 1]

    # Perform ANOVA
    f_statistic, p_value = f_oneway(loam, sandy, clay)

    return f_statistic, p_value

def boxplot():
    # Change the data
    loam = [3, 4, 4, 5]
    sandy = [6, 5, 2, 4]
    clay = [1, 7, 4, 1]

    data = [loam, sandy, clay]

    plt.figure(figsize=(8, 6))
    plt.boxplot(data, labels=['loam', 'sandy', 'clay'])
    plt.title('Boxplot showing the ANOVA results of the readings of different soil types')
    plt.xlabel('Soil')
    plt.ylabel('Sensor reading')
    plt.grid(True)

    f_statistic, p_value = anova()

    plt.annotate(f'P-value: {p_value:.4f}', xy=(0.9, 0.0125), xycoords='axes fraction', fontsize=10)
    plt.annotate(f'F-statistic: {f_statistic:.2f}', xy=(0.9, 0.125), xycoords='axes fraction', fontsize=10)

    plt.show()

# Call the function to display the boxplot with annotations
if __name__ == '__main__':
    boxplot()