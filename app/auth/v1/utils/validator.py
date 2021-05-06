from app.auth.v1.model.user_model import UserModels


class Validators():
    def user_exists(self, email, username):
        """Validator to find is username and email already registered"""
        name = UserModels.query.filter_by(username=username).first()
        mail = UserModels.query.filter_by(email=email).first()
        if name:
            return {
                "status": 400,
                "error": "Username already exists"
            }, 400
        if mail:
            return {
                "status": 400,
                "error": "Email already exists"
            }, 400

    def validate_user(self, username):
        """Validate if userId exists"""
        user = UserModels.query.filter_by(username=username).first()
        if not user:
            return {
                "status": 404,
                "error": "User does not exist"
            }, 404
