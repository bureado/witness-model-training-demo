#!/bin/bash

cd 102-sk-sarif/
python3 ./train.py || true

modelscan -p unsafe_model.pkl -r json -o modelscan.json || true
python3 ./modelscan2sarif.py < modelscan.json > modelscan-sarif.json || true

tr -cd '\11\12\15\40-\176' < modelscan-sarif.json > ../modelscan-sarif.json || true

rm modelscan*.json

cat ../modelscan-sarif.json
