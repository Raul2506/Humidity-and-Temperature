 #include <dht.h>
 
dht DHT;
 
#define DHT11_PIN 3
#define pinRED 5
#define pinGREEN 7
#define pinBLUE 6
 
void setup(){
  Serial.begin(9600);
  pinMode(pinRED,OUTPUT);
  pinMode(pinGREEN,OUTPUT);
  pinMode(pinBLUE,OUTPUT);
}
 
void loop()
{
  String mesaj;
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("Temperature = ");
  Serial.println(DHT.temperature);
  Serial.print("Humidity = ");
  Serial.println(DHT.humidity);
  bool red = 0, green = 0, blue = 0;
  if(DHT.temperature < 23) red = 1;
  else green = 1;
  if(DHT.humidity > 50) blue = 1;
  mesaj = (String)DHT.temperature +";"+(String)DHT.humidity+";"+(String)red+";"+(String)green+";"+(String)blue;
  Serial.println(mesaj);
  color(red, green, blue);
  delay(4000);
  analogWrite(pinRED, LOW);
  analogWrite(pinGREEN, LOW);
  analogWrite(pinBLUE, LOW);
  delay(1500);
}
 
void color(bool red, bool green, bool blue){
if(red)analogWrite(pinRED,255);
if(green)analogWrite(pinGREEN,255);
if(blue)analogWrite(pinBLUE,255);
 
}