cd test

curl -fsSL -o ssshtest https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ./ssshtest

# run (ssshtest keyword) <test_name> <script> <args>
run test_print_fires1 src/print_fires.py --country Zimbabwe --fires_column 3 --file_name test/TestAgrofood.csv
assert_in_stdout [185, 185, 185, 185, 185, 185, 221, 408, 473, 305, 19, 26, 45, 67, 87, 164, 113, 229, 255, 168, 283, 168, 259, 238, 166, 287, 232, 131, 221, 171, 48]
assert_exit_code 0

run test_print_fires1 python src/print_fires.py --country FAKECOUNTRY --fires_column 3 --file_name test/TestAgrofood.csv
assert_in_stdout 
assert_exit_code 0

cd ..