# 
import os
import secrets
from PIL import Image
from .models import User
from . import app

def get_sugesst_field(field, value):

	query = User.query.filter_by(**{field: value})


def save_picture(form_picture, folder='profile_img'):
	random_hex = secrets.token_hex(6)
	_, file_text = os.path.splitext(form_picture.filename)

	picture_ = random_hex + file_text
	sub_path = 'static/{}'.format(folder)
	picture_path = os.path.join(app.root_path, sub_path, picture_)

	output_size = (650, 650)
	img = Image.open(form_picture)
	img.thumbnail(output_size)
	

	img.save(picture_path)

	return picture_