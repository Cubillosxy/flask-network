# template filters
from settings import LIMIT_PREVIEW_POST
from blog import app


@app.template_filter()
def resume_content(content):
	if content and len(content) > LIMIT_PREVIEW_POST:
		return content[:LIMIT_PREVIEW_POST]
	return content


@app.template_filter()
def set_default(text):
	if not text:
		return 'random-img.png'
	return text