import sae
from robot import robot


application = sae.create_wsgi_app(robot.wsgi)
