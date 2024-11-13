""





'''

DECLARE
x int:=&x; /*taking value at run time*/ 
y int:=&y; 
div_r float; 
exp1 EXCEPTION; 
exp2 EXCEPTION; 

BEGIN
IF y=0 then
	raise exp1; 

ELSEIF y > x then
	raise exp2; 

ELSE
	div_r:= x / y; 
	dbms_output.put_line('the result is '||div_r); 

END IF; 

EXCEPTION 
WHEN exp1 THEN
	dbms_output.put_line('Error'); 
	dbms_output.put_line('division by zero not allowed'); 

WHEN exp2 THEN
	dbms_output.put_line('Error'); 
	dbms_output.put_line('y is greater than x please check the input'); 

END; 




'''