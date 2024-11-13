nested_dict={
	"emp01":{
		"name":"Kate",
		"age":22,
		"designation": "Analyst",
		"Salary":30000
	},
	"emp02":{
		"name":"Rina",
		"age":20,
		"designation":"Programmer",
		"Salary":25000
	},
	"emp03":{
		"name":"Vikas",
		"age":42,
		"designation":"Manager",
		"Salary":35000
	},
	"emp04":{
		"name":"manish",
		"age":42,
		"designation":"Manager",
		"Salary":15000
	}
}

list_li=get_list(nested_dict)

final=convert_heap(list_li)

print("Dictionary as heap :",final)
