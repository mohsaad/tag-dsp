#include <SPI.h>

#include <Arduino.h>
#include "LPD8806.h"

// Set to the number of LEDs in your LED strip
#define NUM_LEDS 16
// Maximum number of packets to hold in the buffer. Don't change this.
#define BUFFER_LEN 1024
// Toggles FPS output (1 = print FPS over serial, 0 = disable output)
#define PRINT_FPS 0

// Wifi and socket settings
char packetBuffer[BUFFER_LEN];

int dataPin = 2;
int clockPin = 3;
int len = 4;

uint32_t r;
uint8_t g;
uint8_t b;

// LED strip
LPD8806 strip = LPD8806(NUM_LEDS, dataPin, clockPin);


void setup() {
    Serial.begin(115200);
    strip.begin();
    strip.show();
    
       
}

uint8_t N = 0;

void loop() {
    // Read data over socket
    
    if(Serial.readBytes(packetBuffer, 16) == 0)
    {
      return;
    }
    
    for(int i = 0; i < 4; i++)
    {
       strip.setPixelColor(packetBuffer[4*i], 
       strip.Color(packetBuffer[4*i+1] >> 1,
       packetBuffer[4*i+2] >> 1,
       packetBuffer[4*i+3] >> 1));
       
      
    }
    
    strip.show();
}
