from app import db

class Image(db.Model):
    # 테이블 이름 설정
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(200), nullable=False)
    image_file = db.Column(db.LargeBinary, nullable=False)
    upload_date = db.Column(db.DateTime(), nullable=False)