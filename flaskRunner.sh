docker-compose --project-directory ./tools/rabbitMQ/ --file ./tools/rabbitMQ/docker-compose.yaml up -d

source venv/bin/activate
export FLASK_DEBUG=true
export FLASK_APP=main.py
flask run
