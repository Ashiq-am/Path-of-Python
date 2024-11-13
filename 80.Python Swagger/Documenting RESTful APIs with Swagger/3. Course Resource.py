# Course Resource
class CourseResource(Resource):
    def get(self):

        return courses_data, 200

    def post(self):

        data = request.get_json()
        new_id = courses_data[-1]['courseId'] + 1
        new_course = {'courseId': new_id, 'courseName': data['courseName'],
                      'courseDuration': data['courseDuration'], 'courseType': data['courseType']}
        courses_data.append(new_course)
        return new_course, 201


class CourseItemResource(Resource):
    def get(self, course_id):

        for course in courses_data:
            if course['courseId'] == course_id:
                return course, 200
        return {'message': 'Course not found'}, 404

    def put(self, course_id):

        data = request.get_json()
        for course in courses_data:
            if course['courseId'] == course_id:
                course.update(data)
                return course, 200
        return {'message': 'Course not found'}, 404

    def delete(self, course_id):

        for i, course in enumerate(courses_data):
            if course['courseId'] == course_id:
                deleted_course = courses_data.pop(i)
                return deleted_course, 200
        return {'message': 'Course not found'}, 404
