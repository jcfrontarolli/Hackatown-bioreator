Interface Web

A interface (frontend/dashboard.html) exibe gráficos dinâmicos de umidade e temperatura em tempo real usando Chart.js.

Integração MQTT

O arquivo backend/dashboard.py
 realiza a ponte entre o Arduino (Serial) e o servidor MQTT, enviando dados para o tópico compostech/data.

    [SENSOR + ADS1115] 
        │ Serial (USB)
        ▼
[Arduino] --dados--> [dashboard.py]
        │ MQTT
        ▼
[Broker MQTT local]
        │ HTTP REST
        ▼
[Servidor Flask - app.py] <----> [data_source.py]
        │
        ▼
[Interface Web - dashboard.html]
