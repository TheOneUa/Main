const int ledPin = 13;

bool ledState = false;

String commandBuffer = ""; 

void setup() {
  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);

  digitalWrite(ledPin, LOW);
}

void loop() {
  if (Serial.available()) { 
    char receivedChar = Serial.read(); // Читаем символ из последовательного порта
    if (receivedChar == '\n') { // Если получен символ новой строки
      if (commandBuffer.startsWith("AT+")) { // Проверяем, начинается ли команда с "AT+"
        String numberString = commandBuffer.substring(3); // Получаем число из команды
        int number = numberString.toInt(); // Преобразуем строку в число
        if (number % 10 == 0) { // Проверяем, является ли число кратным 10
          ledState = !ledState;
          // Установка состояния светодиода
          digitalWrite(ledPin, ledState ? HIGH : LOW);
        }
      }
      commandBuffer = ""; // Очищаем буфер для следующей команды
    } else {
      commandBuffer += receivedChar; // Добавляем принятый символ в буфер
    }
  }
}

