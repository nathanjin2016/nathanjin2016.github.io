import statistics

def calculate_sd(number_list):
    try:
        return "The Standard Deviation of the input data is: {}".format(statistics.stdev(number_list))
    except statistics.StatisticsError as exc:
        return "Error calculating StDev: {}".format(exc)

