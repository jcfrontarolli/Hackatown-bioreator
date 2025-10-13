from flask import Flask, render_template, jsonify
import serial
import json
import threading
from datetime import datetime
import logging

app = Flask(__name__)

# Configuração da comunicação serial
try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
except Exception as e:
    print(f"Erro ao abrir porta serial: {e}")
    ser = None

# Armazenamento temporário dos dados
sensor_data = {
    'umidade': 0,
    'valor_cru': 0,
    'voltagem': 0,
    'timestamp': ''
}

def read_serial_data():
    """Thread para leitura contínua de dados seriais"""
    global sensor_data
    while True:
        if ser and ser.in_waiting > 0:
            try:
                line = ser.readline().decode().strip()
                if line:
                    data = json.loads(line)
                    sensor_data.update(data)
                    sensor_data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print(f"Dados recebidos: {sensor_data}")
            except json.JSONDecodeError as e:
                print(f"Erro ao decodificar JSON: {e}")
            except Exception as e:
                print(f"Erro na leitura serial: {e}")

# Iniciar thread de leitura serial
serial_thread = threading.Thread(target=read_serial_data)
serial_thread.daemon = True
serial_thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dados')
def get_dados():
    return jsonify(sensor_data)

@app.route('/api/historico')
def get_historico():
    # Retorna dados para gráfico histórico (simplificado)
    return jsonify([sensor_data])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)