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
                    default='Agrofood_co2_emission.csv')

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

args = parser.parse_args()

# select the specified data & print it
fires = my_utils.get_column(args.file_name, args.country_column,
                            args.country, result_column=args.fires_column)
print(fires)
