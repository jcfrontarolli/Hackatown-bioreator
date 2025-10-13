#include <Wire.h>
#include <Adafruit_ADS1X15.h>
#include <ArduinoJson.h>

Adafruit_ADS1115 ads;  // Objeto ADS1115
const int dryValue = 14216;    // Ajuste com base na calibração :cite[2]
const int wetValue = 3230;     // Ajuste com base na calibração :cite[2]

void setup() {
  Serial.begin(9600);
  
  // Inicialização do ADS1115
  if (!ads.begin()) {
    Serial.println("Falha ao inicializar ADS1115!");
    while (1);
  }
  
  // Configurar ganho para ±4.096V (ajustável conforme necessidade)
  ads.setGain(GAIN_ONE);
  Serial.println("Sistema iniciado - Enviando dados...");
}

void loop() {
  // Leitura do canal A0 do ADS1115
  int16_t adc0 = ads.readADC_SingleEnded(0);
  
  // Converter para porcentagem (valores invertidos: seco → maior valor)
  int moisturePercent = map(adc0, dryValue, wetValue, 0, 100);
  moisturePercent = constrain(moisturePercent, 0, 100);

  // Criar JSON com os dados
  StaticJsonDocument<200> doc;
  doc["sensor"] = "YL-69";
  doc["umidade"] = moisturePercent;
  doc["valor_cru"] = adc0;
  doc["voltagem"] = (adc0 * 0.0078125);  // Conversão para volts com ganho 1

  // Serializar e enviar JSON
  serializeJson(doc, Serial);
  Serial.println();  // Nova linha para delimitar dados

  delay(2000);  // Espera 2 segundos entre leituras
}