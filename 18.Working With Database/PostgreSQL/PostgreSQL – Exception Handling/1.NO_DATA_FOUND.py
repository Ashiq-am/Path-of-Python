''


"""

DECLARE
temp varchar(20); 

BEGIN
SELECT g_id into temp from geeks where g_name='GeeksforGeeks'; 

exception 
WHEN no_data_found THEN
	dbms_output.put_line('ERROR'); 
	dbms_output.put_line('there is no name as'); 
	dbms_output.put_line('GeeksforGeeks in geeks table'); 
end; 




"""