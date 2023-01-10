from flask import Flask
import redis

app = Flask(__name__)

# Creamos una conexión a Redis
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/subscribe')
def subscribe():
    # Suscribimos el cliente a un canal
    pubsub = r.pubsub()
    pubsub.subscribe('joerlyn')

    # Iteramos sobre los mensajes del canal
    for message in pubsub.listen():
        print(message)

if __name__ == '__main__':
    app.run()
