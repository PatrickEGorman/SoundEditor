from app import app
from app import views, config
from app.projects import views
from app.projects.uploads import views


if __name__ == '__main__':
    app.run(debug=True)