from app import create_app
from config import ConfigClass

app = create_app()

# add to https
if __name__ == '__main__':
	app.run(host=ConfigClass.host, port=ConfigClass.port, debug=True)
