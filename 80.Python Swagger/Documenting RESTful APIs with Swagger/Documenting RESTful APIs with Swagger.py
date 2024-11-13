from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

# In-memory data storage for courses and students
courses_data = [
    {'courseId': 3, 'courseName': 'Computer Science',
        'courseDuration': '2', 'courseType': 'Engineering'},
    # Add more courses as needed
]

students_data = [
    {'studentId': 103, 'firstName': 'Sriya', 'lastName': 'Radhika',
        'phoneNumber': '452-123-1254', 'address': 'IN'},
    # Add more students as needed
]

# Course Resource


class CourseResource(Resource):
    def get(self):
        """
        Get all the courses
        ---
        responses:
          200:
            description: A list of courses
        """
        return courses_data, 200

    def post(self):
        """
        Add a new course
        ---
        parameters:
          - in: body
            name: body
            required: true
            schema:
              $ref: '#/components/schemas/Course'
        responses:
          201:
            description: The added course
          400:
            description: Bad request
        """
        data = request.get_json()
        new_id = courses_data[-1]['courseId'] + 1
        new_course = {'courseId': new_id, 'courseName': data['courseName'],
                      'courseDuration': data['courseDuration'], 'courseType': data['courseType']}
        courses_data.append(new_course)
        return new_course, 201


class CourseItemResource(Resource):
    def get(self, course_id):
        """
        Get a specific course
        ---
        parameters:
          - in: path
            name: course_id
            type: integer
            required: true
        responses:
          200:
            description: Details of the requested course
          404:
            description: Course not found
        """
        for course in courses_data:
            if course['courseId'] == course_id:
                return course, 200
        return {'message': 'Course not found'}, 404

    def put(self, course_id):
        """
        Update an existing course
        ---
        parameters:
          - in: path
            name: course_id
            type: integer
            required: true
          - in: body
            name: body
            required: true
            schema:
              $ref: '#/components/schemas/Course'
        responses:
          200:
            description: Successfully updated the course
          404:
            description: Course not found
        """
        data = request.get_json()
        for course in courses_data:
            if course['courseId'] == course_id:
                course.update(data)
                return course, 200
        return {'message': 'Course not found'}, 404

    def delete(self, course_id):
        """
        Delete a specific course
        ---
        parameters:
          - in: path
            name: course_id
            type: integer
            required: true
        responses:
          200:
            description: Successfully deleted the course
          404:
            description: Course not found
        """
        for i, course in enumerate(courses_data):
            if course['courseId'] == course_id:
                deleted_course = courses_data.pop(i)
                return deleted_course, 200
        return {'message': 'Course not found'}, 404

# Student Resource


class StudentResource(Resource):
    def get(self):
        """
        Get all the students
        ---
        responses:
          200:
            description: A list of students
        """
        return students_data, 200

    def post(self):
        """
        Add a new student
        ---
        parameters:
          - in: body
            name: body
            required: true
            schema:
              $ref: '#/components/schemas/Student'
        responses:
          201:
            description: The added student
          400:
            description: Bad request
        """
        data = request.get_json()
        new_id = students_data[-1]['studentId'] + 1
        new_student = {'studentId': new_id, 'firstName': data['firstName'],
                       'lastName': data['lastName'], 'phoneNumber': data['phoneNumber'], 'address': data['address']}
        students_data.append(new_student)
        return new_student, 201


class StudentItemResource(Resource):
    def get(self, student_id):
        """
        Get a specific student
        ---
        parameters:
          - in: path
            name: student_id
            type: integer
            required: true
        responses:
          200:
            description: Details of the requested student
          404:
            description: Student not found
        """
        for student in students_data:
            if student['studentId'] == student_id:
                return student, 200
        return {'message': 'Student not found'}, 404

    def put(self, student_id):
        """
        Update an existing student
        ---
        parameters:
          - in: path
            name: student_id
            type: integer
            required: true
          - in: body
            name: body
            required: true
            schema:
              $ref: '#/components/schemas/Student'
        responses:
          200:
            description: Successfully updated the student
          404:
            description: Student not found
        """
        data = request.get_json()
        for student in students_data:
            if student['studentId'] == student_id:
                student.update(data)
                return student, 200
        return {'message': 'Student not found'}, 404

    def delete(self, student_id):
        """
        Delete a specific student
        ---
        parameters:
          - in: path
            name: student_id
            type: integer
            required: true
        responses:
          200:
            description: Successfully deleted the student
          404:
            description: Student not found
        """
        for i, student in enumerate(students_data):
            if student['studentId'] == student_id:
                deleted_student = students_data.pop(i)
                return deleted_student, 200
        return {'message': 'Student not found'}, 404


# API routes
api.add_resource(CourseResource, '/courses')
api.add_resource(CourseItemResource, '/courses/<int:course_id>')
api.add_resource(StudentResource, '/students')
api.add_resource(StudentItemResource, '/students/<int:student_id>')

if __name__ == '__main__':
    app.run(debug=True)
