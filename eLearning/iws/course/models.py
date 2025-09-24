#
# Author: Rohtash Lakra
#
from globals import db


class Course(db.Model):
    # Course ID
    id = db.Column(db.Integer, primary_key=True)
    # The name of the course.
    title = db.Column(db.String(32))
    # The name of the author.
    author = db.Column(db.String(64))
    # A brief description of the course.
    overview = db.Column(db.String(256))
    # A hyperlink that opens the course’s homepage in a new tab.
    image = db.Column(db.String(256))
    # A URL of the image.
    url = db.Column(db.String(128))
