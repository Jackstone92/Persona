from flask_script import Manager

from API import create_app

# set up the app
app, db = create_app()

manager = Manager(app)

@manager.command
def rundev():
    app.run(debug=True, host="0.0.0.0", port=5000)

@manager.command
def runserver():
    app.run(debug=False)


if __name__ == "__main__":
    manager.run()
