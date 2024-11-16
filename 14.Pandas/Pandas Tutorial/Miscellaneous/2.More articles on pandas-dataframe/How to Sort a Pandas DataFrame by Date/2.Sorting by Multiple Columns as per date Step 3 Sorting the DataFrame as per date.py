# sorting DateFrame by giving first priority to Expiry Date and then Mfg. Date
data_1.sort_values(by=['Expiry Date', 'Mfg. Date'])
