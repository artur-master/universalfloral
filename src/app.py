from flask import Flask, render_template, url_for, request
from flask_mail import Mail, Message
import json

from .config import app_config
from .forms import ContactForm
from .models import db
from .models.AboutModels import TeamModel
from .models.HomeModels import RecentProjectModel

def create_app(env_name):
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  mail = Mail(app)

  db.init_app(app)

  def send_email(subject, sender, recipients, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.html = html_body
    mail.send(msg)

  @app.route('/', methods=['GET', 'POST'])
  def index():
    form = ContactForm()
    msg = ""
    if request.method == "POST":
        if form.validate_on_submit():
            msg = "Massage send!"
            send_email(subject='Message from contact form', sender=app.config['MAIL_USERNAME'], recipients=app.config['MAIL_RECIPIENTS'],
                       html_body='Name:' + str(request.form.get('name')) + '</br>' + 'Email:' + str(request.form.get('email')) + '</br>' + 'Message:' + request.form.get('message'))
        else:
            msg = "Validation error"

    projects = RecentProjectModel.get_all_projects()
    # form.reset()
    return render_template('home.html', form=form, msg=msg, projects=projects)

  @app.route('/about/')
  def about():
    teams = TeamModel.get_all_data()

    return render_template('about.html', active_page="about", teams=teams)

  @app.route('/how-we-work/')
  def howwework():
    return render_template('how-we-work.html', active_page="how-we-work")
  
  @app.route('/what-we-do/')
  def whatwedo():
    return render_template('what-we-do.html', active_page="what-we-do")
  
  @app.route('/clients/')
  def clients():
    return render_template('clients.html', active_page="clients")
  
  @app.route('/contact/')
  def contact():
    return render_template('contact.html', active_page="contact")

  @app.errorhandler(404)
  def not_found_error(error):
    return render_template('404.html', title='Not found'), 404

  with app.test_request_context():
    db.create_all()

    with open('src/models/data.json', 'r') as f:
      data = json.load(f)
      if RecentProjectModel.query.first() == None:
        for project in data["RecentProjects"]:
          rp = RecentProjectModel(project)
          db.session.add(rp)
          
      if TeamModel.query.first() == None:
        for team in data["Teams"]:
          tm = TeamModel(team)
          db.session.add(tm)

      db.session.commit()

  return app