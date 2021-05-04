'''User model'''

class UserModels:
  '''Class for user operation'''
  users = [{},{},{}]

  def __init__(self,email,password,confirm_password):
    '''Init user model'''
    self.userId = len(UserModels.users)+ 1 
    self.email = email
    self.password = password
    slef.confirm_password = confirm_password


    def register(self):
      '''method to sign up a user '''
      data = dict(
        userID = self.userId,
        email = self.email,
        password=self.password,
        confirm_password= self.confirm_password
      )
      self.users.append(data)
      return self.userId

    def fetch_user_by_userId(self,userId):
      ''' Get a user instance using their id '''
      for user in users:
        if user['userId'] == userId:
          return user 
