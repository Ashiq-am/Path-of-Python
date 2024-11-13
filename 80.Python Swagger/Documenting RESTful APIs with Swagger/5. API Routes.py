api.add_resource(CourseResource, '/courses')
api.add_resource(CourseItemResource, '/courses/<int:course_id>')
api.add_resource(StudentResource, '/students')
api.add_resource(StudentItemResource, '/students/<int:student_id>')
