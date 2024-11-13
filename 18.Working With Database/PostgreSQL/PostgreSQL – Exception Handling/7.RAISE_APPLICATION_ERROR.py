""





'''

DECLARE
	myex EXCEPTION; 
	n NUMBER :=10; 

BEGIN
	FOR i IN 1..n LOOP 
	dbms_output.put_line(i*i); 
		IF i*i=36 THEN
		RAISE myex; 
		END IF; 
	END LOOP; 

EXCEPTION 
	WHEN myex THEN
		RAISE_APPLICATION_ERROR(-20015, 'Welcome to GeeksForGeeks'); 

END; 




'''