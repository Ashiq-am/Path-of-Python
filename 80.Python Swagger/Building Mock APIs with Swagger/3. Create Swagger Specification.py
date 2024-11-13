swagger: '2.0'
info:
title: Todo API
description: Simple Todo API with CRUD operations
version: '1.0'

paths:
/todos:
	get:
	summary: Get all todos
	responses:
		'200':
		description: A list of todos
	post:
	summary: Create a new todo
	parameters:
		- name: todo
		in: body
		required: true
		schema:
			type: object
			properties:
			task:
				type: string
				description: The task for the new todo
			completed:
				type: boolean
				description: Whether the task is completed
	responses:
		'201':
		description: Todo created successfully

/todos/{todo_id}:
	parameters:
	- name: todo_id
		in: path
		required: true
		type: integer
	get:
	summary: Get a specific todo by ID
	responses:
		'200':
		description: Todo details
		'404':
		description: Todo not found
	put:
	summary: Update a specific todo by ID
	parameters:
		- name: todo
		in: body
		required: true
		schema:
			type: object
			properties:
			task:
				type: string
				description: The updated task
			completed:
				type: boolean
				description: Whether the task is completed
	responses:
		'200':
		description: Todo updated successfully
		'404':
		description: Todo not found
	delete:
	summary: Delete a specific todo by ID
	responses:
		'200':
		description: Todo deleted successfully
		'404':
		description: Todo not found
