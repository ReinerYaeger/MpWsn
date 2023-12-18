#define AOUT_PIN_0 A0 // Arduino pin that connects to AOUT pin of moisture sensor
#define AOUT_PIN_1 A1 
#define AOUT_PIN_2 A2 
#define AOUT_PIN_3 A3 
#define AOUT_PIN_4 A4  

void setup() {
  Serial.begin(9600);
  
}

void loop() {
  int a_out_array[5];

  a_out_array[0] = analogRead(AOUT_PIN_0);
  a_out_array[1] = analogRead(AOUT_PIN_1);
  a_out_array[2] = analogRead(AOUT_PIN_2);
  a_out_array[3] = analogRead(AOUT_PIN_3);
  a_out_array[4] = analogRead(AOUT_PIN_4);

  float wet_base_value = 207.0;
  float dry_base_value = 487.0;
  float range = wet_base_value - dry_base_value;


  float moisture_0 = (a_out_array[0] - dry_base_value) / range; 
  float moisture_1 = (a_out_array[1] - dry_base_value) / range; 

  Serial.print("A");
  Serial.print(0);
  Serial.print(": ");
  Serial.print(moisture_0,5);

  Serial.print("\t");

  Serial.print("A");
  Serial.print(1);
  Serial.print(": ");
  Serial.println(moisture_1,5);

  // for(int i = 0; i <= 4; i++){

  //   if (a_out_array[i] <100 ||  a_out_array[i] > 900){
  //     Serial.print("Skip");
  //       continue;
  //   }
  //   float moisture = (a_out_array[i] - dry_base_value) / range; 
  //   Serial.print(a_out_array[i]);
  //   Serial.print("Moisture: A");
  //   Serial.print(i);
  //   Serial.print(": ");
  //   Serial.println(moisture,5); // Print moisture with 4 decimal places

  // }
  

  delay(30000);
}
