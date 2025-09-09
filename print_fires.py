import my_utils

# user data selection block
country='United States of America'
country_column = 0
fires_column = 3
file_name = "Agrofood_co2_emission.csv"

# select the specified data
fires = my_utils.get_column(file_name,country_column,country,result_column=fires_column)
print(fires)
