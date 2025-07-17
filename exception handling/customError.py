class CustomError(Exception):
  pass
class ValidationError(Exception):
  def __init__(self,message,code=None):
    super().__init__(message)
    self.code=code

def validate_age(age):
  if age<0:
    raise ValidationError("Age can not be negative",code="NEGATIVE_AGE")
  if age>150:
    raise ValidationError("Age seems unrealistic",code="unrealistic_age")
  
try:
  validate_age(250)
except ValidationError as e:
  print(f"Validation failed: {e}")
  print(f"Error code:{e.code}")
    
