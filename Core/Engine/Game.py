from Engine import Engine

engine = Engine()

engine.start()

while engine.running:

    engine.update()

    break

engine.stop()