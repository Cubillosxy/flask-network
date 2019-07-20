# 

from .models import User

def get_sugesst_field(field, value):

	query = User.query.filter_by(**{field: value})