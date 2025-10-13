<?php
header("Content-Type: application/json; charset=utf-8");
$dataFile = __DIR__ . "/data.json";
if (!file_exists($dataFile)) {
  echo json_encode(["tempo" => [], "umidade" => [], "temperatura" => []]);
  exit;
}
echo file_get_contents($dataFile);
