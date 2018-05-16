Instruction
---
The script `recurrence-plot.py` is a simple tool for creating Recurrence or Distance Plots.
<br>
The files `t-series1.txt`(one column data) and `t-series2.csv`(Excel spreadsheet) are examples of input data.
<br><br>
Usage:
* When your time series file is like `t-series1.txt` you can do:
```Bash
python3 recurrence-plot -b t-series1.txt
```
The `-b` argument is used to indicate a Recurrence Plot will be created.<br>
To create a Distance Plot, just do:
```Bash
python3 recurrence-plot t-series2.csv
```
* When your input data have more than one column, you must inform which column need to be load, e.g.:
```Bash
python3 recurrence-plot -b --column 4 t-series1.txt
```
For more information, run the script without arguments or use `-h`.
