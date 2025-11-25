# Data Analysis
# Author: Angel Li
# 20 November 2025

# Analyse the data provided in class


def main():
    path = "data/NYC_Central_Park_weather_1869-2022.csv"
    file = open(path)
    _ = file.readline()

    # # Count and display the number of all the data points
    # count = 0
    # for line in file:
    #     count += 1

    # print(f"Number of data points: {count}")

    # calculate and display the average rainfall for all data points
    # total_rainfall = 0
    # count = 0

    # for line in file:
    #     info = line.split(",")
    #     rainfall = float(info[1])
    #     total_rainfall += rainfall
    #     count += 1

    # avg_rainfall = total_rainfall / count

    # print(f"The average rainfall for all data points is: {avg_rainfall}")

    # Print all the Tmin values
    # for line in file:
    #     info = line.strip().split(",")
    #     print(info[4])

    # calculate and display the average minimum temperature for all data points
    total_minmtemp = 0
    count = 0

    for line in file:
        info = line.split(",")
        t_value = info[4].strip()
        if t_value == "":
            minmtemp = 0.0
        else:
            minmtemp = float(t_value)
        total_minmtemp += minmtemp
        count += 1

    avg_minmtemp = total_minmtemp / count

    print(f"The average minimum temperature for all data points is: {avg_minmtemp}")

    # convert this to celsius
    temp_cel = (5 * (avg_minmtemp - 32)) / 9
    print(f"The average minimum temperature in Celsius is {temp_cel}.")

    # calculate and display the average maximum temperature of all dates in June
    total_maxtemp = 0
    count = 0

    for line in file:
        info = line.split(",")
        t_value = info[5].strip()

        if t_value == "":
            maxtemp = 0.0
        else:
            minmtemp = float(t_value)
        total_maxtemp += maxtemp
        count += 1

    avg_maxtemp = total_maxtemp / count

    print(f"The average minimum temperature for all data points is: {avg_maxtemp}")

    file.close()


if __name__ == "__main__":
    main()
