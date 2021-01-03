let PositionY = 2
let FlashInterval = 400
basic.forever(function FlashingPoint() {
    led.plot(0, PositionY)
    basic.pause(FlashInterval)
    led.unplot(0, PositionY)
    basic.pause(FlashInterval)
    
})
