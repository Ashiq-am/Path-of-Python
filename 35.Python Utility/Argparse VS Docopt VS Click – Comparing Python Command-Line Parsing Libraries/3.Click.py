# click_example.py

import click

# initialize result to 0
result=0

@click.command()
@click.option('--num1',
			default=1,
			help='Enter a float value',
			type=float)

@click.option('--num2',
			default=1,
			help='Enter a float value',
			type=float)

@click.option('--op',
			default='+',
			help='Enter the operator')

# Calculator function
def calculator(num1,num2,op):
	if op=='+':
		result=num1+num2
	if op=='*':
		result=num1*num2
	if op=='-':
		result=num1-num2
	if op=='/':
		result=num1/num2

	# print the result
	click.echo("Result is %f" %result)

if __name__ =='__main__':
	calculator()
