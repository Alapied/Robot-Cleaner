void led(String messageFromPC, int Count) {
  switch (Count) {
    case 0:
      NormalRunning();
      break;
    case 1:
      RED();
      break;
    case 2:
      BLUE();
      break;
    case 3:
      LEDBOOT();  
      break;
  }
}
void LEDBOOT() {
  // set pixel to orange interchange, delay(1000)
  strip.setPixelColor(0, 255, 180, 0);
  strip.setPixelColor(1, 0, 0, 0);
  strip.setPixelColor(2, 255, 180, 0);
  strip.setPixelColor(3, 0, 0, 0);
  strip.setPixelColor(4, 255, 180, 0);
  strip.setPixelColor(5, 0, 0, 0);
  strip.setPixelColor(6, 255, 180, 0);
  strip.setPixelColor(7, 0, 0, 0);
  strip.show();
  delay(1000);
  // set pixel to other, delay(1000)
  strip.setPixelColor(0, 0, 0, 0);
  strip.setPixelColor(1, 255, 180, 0);
  strip.setPixelColor(2, 0, 0, 0);
  strip.setPixelColor(3, 255, 180, 0);
  strip.setPixelColor(4, 0, 0, 0);
  strip.setPixelColor(5, 255, 180, 0);
  strip.setPixelColor(6, 0, 0, 0);
  strip.setPixelColor(7, 255, 180, 0);
  strip.show();
  delay(1000);
}

void NormalRunning() {
  // set pixel to Green, delay(1000)
  strip.setPixelColor(0, 0, 255, 0);
  strip.setPixelColor(1, 0, 255, 0);
  strip.setPixelColor(2, 0, 255, 0);
  strip.setPixelColor(3, 0, 255, 0);
  strip.setPixelColor(4, 0, 255, 0);
  strip.setPixelColor(5, 0, 255, 0);
  strip.setPixelColor(6, 0, 255, 0);
  strip.setPixelColor(7, 0, 255, 0);
  strip.show();
  delay(1000);

}

void RED() {
  strip.setPixelColor(0, 255, 0, 0);
  strip.setPixelColor(1, 255, 0, 0);
  strip.setPixelColor(2, 255, 0, 0);
  strip.setPixelColor(3, 255, 0, 0);
  strip.setPixelColor(4, 255, 0, 0);
  strip.setPixelColor(5, 255, 0, 0);
  strip.setPixelColor(6, 255, 0, 0);
  strip.setPixelColor(7, 255, 0, 0);
  strip.show();
  delay(1000);
}
void BLUE() {
  strip.setPixelColor(0, 0, 0, 255);
  strip.setPixelColor(1, 0, 0, 255);
  strip.setPixelColor(2, 0, 0, 255);
  strip.setPixelColor(3, 0, 0, 255);
  strip.setPixelColor(4, 0, 0, 255);
  strip.setPixelColor(5, 0, 0, 255);
  strip.setPixelColor(6, 0, 0, 255);
  strip.setPixelColor(7, 0, 0, 255);
  strip.show();
  delay(1000);
}
