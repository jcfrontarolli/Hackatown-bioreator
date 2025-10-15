Arquitetura:
Modularidade Clara: Cada camada tem responsabilidade bem definida

Comunicação Assíncrona: Uso de MQTT para desacoplamento

Persistência Eficiente: Armazenamento em JSON com limite de registros

Interface Responsiva: Dashboard web moderno e responsivo

Extensibilidade: Fácil adição de novos sensores e funcionalidades

Logging Robusto: Monitoramento detalhado de todos os componentes

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
