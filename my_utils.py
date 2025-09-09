from pathlib import Path


def get_column(file_name, query_column, query_value, result_column=1):
    """ Reads a .csv file_name, selects all rows where column query_column matches value query_value, returns the value contained in result_column from those rows 
    
    Inputs:
    - file_name <string>: a path to a .csv file
    - query_column <int>: index of the column used to decide whether a row is selected
    - query_value <any>: rows with query_value in query_column will be selected
    - result_column <int>: column from which data is to be taken for selected rows

    Outputs:
    - result <array>: array of selected values
    
    """


    # intiialize result array
    result = []

    with open(file_name,'r') as f:
        for line in f:
            line_arr = line.split(',')

            # check if value matches user request
            if line_arr[query_column] == query_value:
                result.append(line_arr[result_column])

    return result
        

