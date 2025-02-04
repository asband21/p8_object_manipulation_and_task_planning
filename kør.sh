#!/bin/bash
PROJECT_NAME=$(basename "$PWD")
cd ..

python3 -m venv "${PROJECT_NAME}"

cd "${PROJECT_NAME}"
source bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "det skuller virke nu der er kørn \"source bin/activate\""

