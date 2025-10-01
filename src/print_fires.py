import my_utils
import argparse

parser = argparse.ArgumentParser(
            description="""Assignment3 Code: Prints user-selected data from a
                            csv""",
            prog='print_fires'
)

parser.add_argument('--file_name',
                    type=str,
                    help='Name or path to .csv file',
                    default='Assignments/'
                            'assignment-2-python-refresher-hessewithbroej/'
                            'Agrofood_co2_emission.csv')

parser.add_argument('--country',
                    type=str,
                    help='Name of country from which to select data',
                    default='United States of America')

parser.add_argument('--country_column',
                    type=int,
                    help="""Index of column of .csv file that contains the
                             countries""",
                    default=0)

parser.add_argument('--fires_column',
                    type=int,
                    help="""Index of column of .csv file that contains the fire
                             data""",
                    default=3)

parser.add_argument('--operation',
                    type=str,
                    help="""Operation to perform on selected data""",
                    required=False)

args = parser.parse_args()

# select the specified data & print it
fires = my_utils.get_column(args.file_name, args.country_column,
                            args.country, result_column=args.fires_column)

if args.operation == 'mean':
    print(my_utils.calc_mean(fires))
elif args.operation == 'median':
    print(my_utils.calc_median(fires))
elif args.operation == 'stdev':
    print(my_utils.calc_stdev(fires))
else:
    print(fires)