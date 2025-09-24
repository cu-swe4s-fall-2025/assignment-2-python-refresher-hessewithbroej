from pathlib import Path
import sys


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


def main():
    print(get_column('Agrofood_co2_emission.csv', 0,
                     'Zimbabwe', result_column=1))


if __name__ == '__main__':
    main()
