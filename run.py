from history import create_app, db
from socket import gethostname
from waitress import serve
app = create_app()
# need to add functio to ad  
bookmark = lambda x: x.upper()

# app.jinja_env.globals.update(bookmark=bookmark)
# print(app.url_map)
if __name__ == '__main__':
    # serve(app, host="0.0.0.0", port=5000)
    app.run(debug=True)
    ''''
        The code below is for live console and production only
    '''
    # db.create_all()
    # if 'liveconsole' not in gethostname():
    #     app.run()