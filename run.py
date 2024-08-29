from history import create_app, db
from socket import gethostname
app = create_app()
# need to add functio to ad  
bookmark = lambda x: x.upper()

# app.jinja_env.globals.update(bookmark=bookmark)
# print(app.url_map)
if __name__ == '__main__':
    app.run(debug=True)
    ''''
        The code below is for live console and production only
    '''
    # db.create_all()
    # if 'liveconsole' not in gethostname():
    #     app.run()