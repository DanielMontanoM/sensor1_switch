strip = neopixel.create(DigitalPin.P14, 10, NeoPixelMode.RGB)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P1) == 1:
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
basic.forever(on_forever)
