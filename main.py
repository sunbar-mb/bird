PositionY = 2
FlashInterval = 400


basic.forever(FlashingPoint)


def FlashingPoint():
    led.plot(0, PositionY)
    basic.pause(FlashInterval)
    led.unplot(0, PositionY)
    basic.pause(FlashInterval)
    pass
