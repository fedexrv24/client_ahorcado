import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')

@sio.event
def jugadores(data):
    print(data)

sio.connect('http://localhost:5000')

while True:
    b = input("R para reset, D para desconectar, L para listo. ").upper()
    if b == "R":
        sio.disconnect()

        sio.connect('http://localhost:5000')

        sio.emit('jugadores')
        sio.sleep(2)

    elif b == "D":
        # sio.disconnect()
        break

    elif b == "L":
        sio.emit('listo')
        
        continue

sio.disconnect()

