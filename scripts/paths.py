
import os

data_path = os.path.join('..', 'data')
bruto_path = os.path.join(data_path, 'brutos')
output_path = os.path.join(data_path, 'output')

os.makedirs(data_path, exist_ok=True)
os.makedirs(bruto_path, exist_ok=True)
os.makedirs(output_path, exist_ok=True)