from pathlib import Path
import sys
import numpy as np


def get_column(file_name, query_column, query_value, result_column=1):
    """ Reads a .csv file_name, selects all rows where column query_column
    matches value query_value, returns the value contained in result_column
    from those rows

    Inputs:
    - file_name <string>: a path to a .csv file
    - query_column <int>: index of the column used to decide whether a row is
        selected
    - query_value <any>: rows with query_value in query_column will be selected
    - result_column <int>: column from which data is to be taken for selected
    rows

    Outputs:
    - result <array>: array of selected values

    """

    # intiialize result array
    result = []
    try:
        with open(file_name, 'r') as f:
            for line in f:
                line_arr = line.split(',')

                # check if value matches user request
                if line_arr[query_column] == query_value:
                    try:
                        val = int(float(line_arr[result_column]))
                        result.append(val)
                    except IndexError:
                        print("Error: Invalid result_column index")
                        sys.exit(1)
                    except ValueError:
                        print(f"""Error:
                                Cannot convert
                                {line_arr[result_column]} of type
                                {type(line_arr[result_column])} to int""")
                        sys.exit(1)

    except FileNotFoundError:
        # handle incorrect filename/filepath
        print("Error: The file " + file_name + " was not found.")
        sys.exit(1)

    except IOError as e:
        # Handle other I/O errors (e.g., permission issues)
        print(f"Error reading file: {e}")
        sys.exit(1)

    return result


def calc_mean(arr):
    """ Calculates mean of an array

    Inputs:
    - arr <array>: array of elements from which to compute mean

    Outputs:
    - result <float>: mean of supplied array
    """
    if len(arr)>0:
        return np.mean(arr)
    else:
        raise ArithmeticError("Attempted to calculate mean of empty array")
    

def calc_median(arr):
    """ Calculates median of an array

    Inputs:
    - arr <array>: array of elements from which to compute median

    Outputs:
    - result <float>: median of supplied array
    """
    if len(arr)>0:
        return np.median(arr)
    else:
        raise ArithmeticError("Attempted to calculate median of empty array")
    
def calc_median(arr):
    """ Calculates median of an array

    Inputs:
    - arr <array>: array of elements from which to compute median

    Outputs:
    - result <float>: median of supplied array
    """
    if len(arr)>0:
        return np.median(arr)
    else:
        raise ArithmeticError("Attempted to calculate median of empty array")


def calc_stdev(arr):
    """ Calculates standard deviation of an array

    Inputs:
    - arr <array>: array of elements from which to compute stdev

    Outputs:
    - result <float>: median of supplied array
    """
    if len(arr)>1:
        return np.std(arr)
    else:
        raise ArithmeticError("Attempted to calculate stdev of array with less than 2 elements")



def main():
    print(type(get_column('./Assignments/assignment-2-python-refresher-hessewithbroej/Agrofood_co2_emission.csv', 0,
                     'Zimbabwe', result_column=1)))
    print(calc_mean([1,1,1,2,4,4]))
    print(calc_median([1,1,1,2,4,4]))
    print(calc_stdev([1,2,3]))


if __name__ == '__main__':
    main()
