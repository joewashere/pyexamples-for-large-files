# Python script examples for working with large data files

Just some scripts I wrote for playing with large data files.

genfile - generates a 14000000 line text file with junk data

readfile - reads a file and outputs it to a new file

modify - changes first row value in each row of input file and writes to new file

extract4sql - kinda useless... just extracts all of the rows that share the first column value into their own file

process - loops through the large file and does an SQL lookup for each file.

## Some useful commands I found while working with these:


wc -l 

Counts the number of lines in a file


sed -i 1,100d 

removes the first 100 rows from a file. Can change number


