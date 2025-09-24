[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

## my_utils.py
### get_column(file_name, query_column, query_value, result_column) 
function created to enable selection of specified data within a .csv file. Can specify the desired value of a specified query column, then return the value in a different specified result column of all rows who match the query criteria. 

Example usage:
`get_column('Agrofood_co2_emission.csv', 0,'Zimbabwe', result_column=1)`

### calc_mean(arr)
Function to calculate the mean of an array of floats

Example usage:
`calc_mean([1,2.3,4])`

### calc_median(arr)
Function to calculate the median of an array of floats

Example usage:
`calc_median([1,2.3,4])`

### calc_stdev(arr)
Function to calculate the standard deviation of an array of floats

Example usage:
`calc_stdev([1,2.3,4])`


## print_fires.py
python script created to print the number of fires, or other specifiable numeric column in the agrofood_co2_emission.csv, in a user-specified country by year, utilizing my_utils.get_column() 

## run.sh
bash script created to run print_fires.py correctly, and with two example incorrect usages.
