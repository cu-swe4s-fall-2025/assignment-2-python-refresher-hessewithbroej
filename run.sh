#!/bin/bash

#runs successfully using default values 
python print_fires.py

#errors when trying print fires column as a list of ints 
python print_fires.py --fires_column 0

#errors when trying to read a nonexistent csv fil
python print_fires.py --file_name BadFile.csv