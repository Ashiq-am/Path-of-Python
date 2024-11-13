# Student Resource
class StudentResource(Resource):
    def get(self):

        return students_data, 200

    def post(self):

        data = request.get_json()
        new_id = students_data[-1]['studentId'] + 1
        new_student = {'studentId': new_id, 'firstName': data['firstName'],
                       'lastName': data['lastName'], 'phoneNumber': data['phoneNumber'], 'address': data['address']}
        students_data.append(new_student)
        return new_student, 201


class StudentItemResource(Resource):
    def get(self, student_id):

        for student in students_data:
            if student['studentId'] == student_id:
                return student, 200
        return {'message': 'Student not found'}, 404

    def put(self, student_id):

        data = request.get_json()
        for student in students_data:
            if student['studentId'] == student_id:
                student.update(data)
                return student, 200
        return {'message': 'Student not found'}, 404

    def delete(self, student_id):

        for i, student in enumerate(students_data):
            if student['studentId'] == student_id:
                deleted_student = students_data.pop(i)
                return deleted_student, 200
        return {'message': 'Student not found'}, 404
