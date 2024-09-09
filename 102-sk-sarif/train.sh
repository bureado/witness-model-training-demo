#!/bin/bash

python3 ./train.py
modelscan -p unsafe_model.pkl -r json -o modelscan.json
python3 ./modelscan2sarif.py < modelscan.json > modelscan.sarif
rm modelscan.json
