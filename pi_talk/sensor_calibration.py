import csv


def gravimetric_method(soil_sample_weight, container_mass=22.75, mass_of_dried_soil=26.33, bulk_density=0.13165):
    try:
        soil_sample_weight = soil_sample_weight - container_mass

        vmc = ((soil_sample_weight - mass_of_dried_soil) / mass_of_dried_soil) * (
            bulk_density/.997)  # volumetric water content
    except ZeroDivisionError as e:
        return e
    return vmc


def analyse_experiment_csv_results():
    weight = []
    A0 = []
    A1 = []
    A2 = []
    csv_file = open('experiment.csv', 'r')
    csv_file = csv.DictReader(csv_file)
    for col in csv_file:
        weight.append(gravimetric_method(float(col['Soil_weight'])))
        A0.append(float(col['A0']))
        A1.append(float(col['A1']))
        A2.append(float(col['A2']))

    print(weight)
    print(A0)
    print(A1)
    print(A2)


analyse_experiment_csv_results()
