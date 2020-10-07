from flask import Flask, render_template, url_for

from .config import app_config
from .models import db
from .models.AboutModels import TeamModel

def create_app(env_name):
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  # db.init_app(app)

  @app.route('/')
  def index():
    # teams = TeamModel.get_all_data()
    return render_template('home.html')

  @app.route('/about')
  def about():
    return render_template('about.html', active_page = "about")

  @app.route('/how-we-work')
  def howwework():
    return render_template('/how-we-work.html', active_page = "how-we-work")
  
  @app.route('/what-we-do')
  def whatwedo():
    return render_template('/what-we-do.html', active_page = "what-we-do")
  
  @app.route('/clients')
  def clients():
    return render_template('/clients.html', active_page = "clients")
  
  @app.route('/contact')
  def contact():
    return render_template('/contact.html', active_page = "contact")

  return app

