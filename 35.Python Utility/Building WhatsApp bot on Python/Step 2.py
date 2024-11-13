from flask import request

incoming_msg = request.values.get('Body', '').lower()
