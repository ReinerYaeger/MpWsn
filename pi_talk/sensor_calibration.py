import csv
import numpy as np
from scipy.stats import f_oneway, linregress
import matplotlib.pyplot as plt


def analyse_experiment_csv_results():
    soil_data = {
        'soil_weight_loam': [],
        'soil_weight_sand': [],
        'soil_weight_clay': [],
        'A0_loam': [],
        'A0_sand': [],
        'A0_clay': [],
        'A1_loam': [],
        'A1_sand': [],
        'A1_clay': [],
        'A2_loam': [],
        'A2_sand': [],
        'A2_clay': []
    }

    csv_file = open('experiment.csv', 'r')
    csv_file = csv.DictReader(csv_file)
    for col in csv_file:
        soil_data['soil_weight_loam'].append((float(col['Soil_weight_loam'])))
        soil_data['soil_weight_sand'].append((float(col['Soil_weight_sand'])))
        soil_data['soil_weight_clay'].append((float(col['Soil_weight_clay'])))
        soil_data['A0_loam'].append(float(col['A0_loam']))
        soil_data['A1_loam'].append(float(col['A1_loam']))
        soil_data['A2_loam'].append(float(col['A2_loam']))
        soil_data['A0_sand'].append(float(col['A0_sand']))
        soil_data['A1_sand'].append(float(col['A1_sand']))
        soil_data['A2_sand'].append(float(col['A2_sand']))
        soil_data['A0_clay'].append(float(col['A0_clay']))
        soil_data['A1_clay'].append(float(col['A1_clay']))
        soil_data['A2_clay'].append(float(col['A2_clay']))
    print(soil_data)
    return soil_data


def one_way_anova(data, measurements, soil_types):
    f_statistic, p_value = f_oneway(*[data[measurement + '_' + soil_type] for measurement in measurements for soil_type in soil_types])

    print(f'One-way ANOVA Results:')
    print(f'F-statistic: {f_statistic}')
    print(f'P-value: {p_value}')

    return f_statistic, p_value


def coefficient_of_variation(data, measurements, soil_types):
    cv_results = {}

    for measurement in measurements:
        for soil_type in soil_types:
            key = f'{measurement}_{soil_type}'
            mean_value = np.mean(data[key])
            std_dev = np.std(data[key])
            cv = (std_dev / mean_value) * 100
            cv_results[key] = cv

    print('\nCoefficient of Variation Results:')
    for key, value in cv_results.items():
        print(f'{key}: {value:.2f}%')

    return cv_results


def plot_box_plot(data, measurements, soil_types):
    all_data = [data[measurement + '_' + soil_type] for measurement in measurements for soil_type in soil_types]
    labels = [f'{measurement}_{soil_type}' for measurement in measurements for soil_type in soil_types]

    plt.figure(figsize=(10, 6))
    plt.boxplot(all_data, labels=labels)
    plt.ylabel('Sensor Readings')
    plt.title('Box Plot of Sensor Readings Across Soil Types')
    plt.show()


def plot_log_graph(data, measurements, soil_types, regression_results):
    for measurement in measurements:
        plt.figure(figsize=(10, 6))
        for soil_type in soil_types:
            key = f'{measurement}_{soil_type}'
            x_values = np.arange(len(data[key]))
            plt.scatter(x_values, data[key], label=f'{measurement}_{soil_type}')

            # Calculate regression line on log scale
            log_values = np.log(data[key])
            slope, intercept, _, _, _ = linregress(x_values, log_values)
            regression_line = intercept + slope * x_values
            plt.plot(x_values, np.exp(regression_line), color='red', linestyle='--')

        plt.yscale('log')  # Set y-axis to log scale
        plt.xlabel('Data Points')
        plt.ylabel('Log(Sensor Readings)')
        plt.title(f'Log-scaled Scatter Plot with Regression Line ({measurement})')
        plt.legend()
        plt.show()


def linear_regression(data, measurements, soil_types):
    regression_results = {}

    for measurement in measurements:
        for soil_type in soil_types:
            key = f'{measurement}_{soil_type}'
            x_values = np.arange(len(data[key]))  # Assuming data points are ordered
            slope, intercept, r_value, p_value, std_err = linregress(x_values, data[key])
            regression_results[key] = {
                'slope': slope,
                'intercept': intercept,
                'r_value': r_value,
                'p_value': p_value,
                'std_err': std_err
            }

            # Plot the regression line
            plt.scatter(x_values, data[key], label=f'{measurement}_{soil_type}')
            plt.plot(x_values, intercept + slope * x_values, color='red', linestyle='--')

    plt.xlabel('Data Points')
    plt.ylabel('Sensor Readings')
    plt.title('Linear Regression for Sensor Readings Across Soil Types')
    plt.legend()
    plt.show()

    return regression_results


def plot_anova_results(f_statistic, p_value):
    plt.bar(['F-statistic'], [f_statistic], color='blue')
    plt.bar(['P-value'], [p_value], color='orange')
    plt.ylabel('Values')
    plt.title('ANOVA Results')
    plt.show()


def plot_coefficient_of_variation(cv_results):
    measurements = list(set(key.split('_')[0] for key in cv_results.keys()))
    soil_types = list(set(key.split('_')[1] for key in cv_results.keys()))

    for measurement in measurements:
        cv_values = [cv_results[f'{measurement}_{soil_type}'] for soil_type in soil_types]
        plt.bar(soil_types, cv_values, label=measurement)

    plt.ylabel('Coefficient of Variation (%)')
    plt.title('Coefficient of Variation Across Soil Types')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    soil_data_dict = analyse_experiment_csv_results()
    measurements = ['A0', 'A1', 'A2']
    soil_types = ['loam', 'sand', 'clay']

    f_statistic, p_value = one_way_anova(soil_data_dict, measurements, soil_types)

    cv_results = coefficient_of_variation(soil_data_dict, measurements, soil_types)
    regression_results = linear_regression(soil_data_dict, measurements, soil_types)
    print('\nLinear Regression Results:')
    for key, value in regression_results.items():
        print(
            f'{key}: Slope={value["slope"]:.4f}, Intercept={value["intercept"]:.4f}, R-squared={value["r_value"]:.4f}, P-value={value["p_value"]:.4f}')
    plot_anova_results(f_statistic, p_value)
    plot_box_plot(soil_data_dict, measurements, soil_types)
    plot_coefficient_of_variation(cv_results)
