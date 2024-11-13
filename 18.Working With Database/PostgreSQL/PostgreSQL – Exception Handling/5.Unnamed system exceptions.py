''




'''

DECLARE
exp exception; 
pragma exception_init (exp, -20015); 
n int:=10; 

BEGIN
FOR i IN 1..n LOOP 
	dbms_output.put_line(i*i); 
		IF i*i=36 THEN
			RAISE exp; 
		END IF; 
END LOOP; 

EXCEPTION 
WHEN exp THEN
	dbms_output.put_line('Welcome to GeeksforGeeks'); 

END; 



'''