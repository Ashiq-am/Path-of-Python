""""""




'''

DECLARE
GeeksforGeeks EXCEPTION; 
age NUMBER:=16; 
BEGIN

-- sub-block BEGINs 
DECLARE	
		
	-- this declaration prevails 
	GeeksforGeeks EXCEPTION; 
	age NUMBER:=22; 
	
BEGIN
	IF age > 16 THEN
		RAISE GeeksforGeeks; /* this is not handled*/ 
	END IF; 
	
END;		 
-- sub-block ends 

EXCEPTION 
-- Does not handle raised exception 
WHEN GeeksforGeeks THEN
	DBMS_OUTPUT.PUT_LINE 
	('Handling GeeksforGeeks exception.'); 
	
WHEN OTHERS THEN
	DBMS_OUTPUT.PUT_LINE 
	('Could not recognize exception GeeksforGeeks in this scope.'); 
END; 




'''