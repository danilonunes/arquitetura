from app import app as application
import os

application.run(host=os.environ['IP'], port=int(os.environ['PORT']), debug=True)