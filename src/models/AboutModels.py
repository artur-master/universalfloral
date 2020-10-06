from marshmallow import fields, Schema
import datetime
from . import db, bcrypt

class TeamModel(db.Model):
  # table name
  __tablename__ = 'team'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  position = db.Column(db.String(128), nullable=True)
  about = db.Column(db.String(1000), nullable=True)
  call = db.Column(db.String(128), nullable=True)
  email = db.Column(db.String(128), nullable=True)  

  # class constructor
  def __init__(self, data):
    self.name = data.get('name')
    self.position = data.get('email')
    self.about = data.get('about')
    self.call = data.get('call')
    self.email = data.get('email')

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_data():
    return TeamModel.query.all()
    
  def __repr__(self):
    return '<id {}>'.format(self.id)



# class UserSchema(Schema):
#   id = fields.Int(dump_only=True)
#   name = fields.Str(required=True)
#   email = fields.Email(required=True)
#   password = fields.Str(required=True, load_only=True)
#   created_at = fields.DateTime(dump_only=True)
#   modified_at = fields.DateTime(dump_only=True)
#   blogposts = fields.Nested(BlogpostSchema, many=True)
