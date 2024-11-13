""""""




'''

DECLARE
temp number; 

BEGIN
SELECT g_name into temp from geeks where g_name='Suraj'; 
dbms_output.put_line('the g_name is '||temp); 

EXCEPTION 
WHEN value_error THEN
dbms_output.put_line('Error'); 
dbms_output.put_line('Change data type of temp to varchar(20)'); 

END; 




'''