import pyglet

ventana = pyglet.window.Window(1366, 768, "Mi primer juego")

lote = pyglet.graphics.Batch()

jugador_sprite = pyglet.resource.image("Recursos/ImagenJugador.png")
jugador = pyglet.sprite.Sprite(jugador_sprite, x=200, y=100, batch=lote)
control = Control()


@ventana.event
def on_draw():
    ventana.clear()
    lote.draw()


pyglet.app.run()


class jugador:
    def __init__(self):
        self.x = 200
        self.x = 100

    def moverIzquierda(self):
        self.x -= 10

    def moverDerecha(self):
        self.x += 10

    def salto(self):
        self.y += 50


@ventana.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.LEFT:
        control.moverIzquierda()
    elif symbol == pyglet.window.key.RIGHT:
        control.moverDerecha()
    elif symbol == pyglet.window.key.UP:
        control.salto()
