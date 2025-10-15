Compostech/
├── hardware/
│   └── Sensor-umidade-YL-69.cpp
├── backend/
│   ├── app.py
│   ├── dashboard.py
│   ├── data_source.py
│   ├── data.json
│   └── requirements.txt
├── frontend/
│   └── dashboard.html
└── docs/
    └── arquitetura.md

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
