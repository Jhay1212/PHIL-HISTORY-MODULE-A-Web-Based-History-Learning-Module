from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from history import create_app, db
from history.main.models import BookMark, Lesson, MiniNotes
from history.auth.models import User

app = create_app()
admin = Admin(app)
admin.add_view(ModelView(MiniNotes, db.session))
admin.add_view(ModelView(Lesson, db.session))
admin.add_view(ModelView(BookMark, db.session))
admin.add_view(ModelView(User, db.session))