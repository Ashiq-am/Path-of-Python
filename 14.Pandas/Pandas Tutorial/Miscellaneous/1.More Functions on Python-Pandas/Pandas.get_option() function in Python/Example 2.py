# importing the module
import pandas as pd

# default Excel reader engine for ‘ods’ files
print("The default Excel reader engine for ‘ods’ files : " + str(pd.get_option("io.excel.ods.reader")))

# default Excel reader engine for ‘xls’ files
print("The default Excel reader engine for ‘xls’ files : " + str(pd.get_option("io.excel.xls.reader")))

# default Excel writer engine for ‘xls’ files
print("The default Excel writer engine for ‘xls’ files : " + str(pd.get_option("io.excel.xls.writer")))

# default Excel reader engine for ‘xlsb’ files
print("The default Excel reader engine for ‘xlsb’ files : " + str(pd.get_option("io.excel.xlsb.reader")))

# default Excel reader engine for ‘xlsm’ files
print("The default Excel reader engine for ‘xlsm’ files : " + str(pd.get_option("io.excel.xlsm.reader")))

# default Excel writer engine for ‘xlsm’ files
print("The default Excel writer engine for ‘xlsm’ files : " + str(pd.get_option("io.excel.xlsm.writer")))

# default Excel reader engine for ‘xlsm’ files
print("The default Excel reader engine for ‘xlsx’ files : " + str(pd.get_option("io.excel.xlsx.reader")))

# default Excel writer engine for ‘xlsx’ files
print("The default Excel writer engine for ‘xlsx’ files : " + str(pd.get_option("io.excel.xlsx.writer")))
