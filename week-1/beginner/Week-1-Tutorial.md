# TAG-DSP Week 1
# Introduction to Arduino (and a little Python on top)

So this week, we started our journey of DSP with a little Arduino. Here's a guide to getting started with what we covered this week.

## Setting up Arduino

### Downloading Arduino

Go to [the Arduno website](https://www.arduino.cc/en/Main/Software) and download their Arduino software for your operating system. You can either do the standalone installer or the portable version, either should work.

### Setting up the Arduino
To set up the Arduino for our demos, put an LED into pin 11. We use this pin because not only is it a digital pin, but it also can simulate an analog one, which makes it useful for Pulse-Width Modulation. 

The Arduino should look like this:
(img goes here)

### Blink
The Blink demo can be found in Arduino/Blink.ino. It's a fairly simple demo - turn the LEDs on, delay for a second, turn LED off, delay for a second. Play around with it - if you don't have an LED, you can use pin 13. Pin 13 is also connected to an LED on the board, so you can see the LED turn on and off at certain times.

### Pulse-Width Modulation

