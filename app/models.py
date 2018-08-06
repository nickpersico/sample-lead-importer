# from app import db
# from datetime import datetime

# class Import(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	email = db.Column(db.String(120), index=True)
# 	list_type = db.Column(db.String(64))
# 	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
# 	status = db.Column(db.String(64))

# 	def __repr__(self):
# 		return '<Import {}>'.format(self.email)