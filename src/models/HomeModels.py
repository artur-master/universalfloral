from . import db

class RecentProjectModel(db.Model):
  # table name
  __tablename__ = 'recent_project'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  photo = db.Column(db.String(1000), nullable=True)

  # class constructor
  def __init__(self, data):
    self.name = data.get('name')
    self.photo = data.get('photo')
    
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
  def get_all_projects():
    return RecentProjectModel.query.all()
    
  def __repr__(self):
    return '<id {}>'.format(self.id)
