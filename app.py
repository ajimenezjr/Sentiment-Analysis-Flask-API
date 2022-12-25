# app.py

from werkzeug.middleware.dispatcher import \
    DispatcherMiddleware  # use to combine each Flask app into a larger one that is dispatched based on prefix
from app_sentiment import app as flask_app_1
from app_summary import app as flask_app_2

application = DispatcherMiddleware(flask_app_1, {
    '/summary': flask_app_2
})
