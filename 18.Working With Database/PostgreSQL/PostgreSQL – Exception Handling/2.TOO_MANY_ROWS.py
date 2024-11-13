""



'''
DECLARE
temp varchar(20); 

BEGIN

-- raises an exception as SELECT 
-- into trying to return too many rows 
SELECT g_name into temp from geeks; 
dbms_output.put_line(temp); 

EXCEPTION 
WHEN too_many_rows THEN
	dbms_output.put_line('error trying to SELECT too many rows'); 

end; 


'''