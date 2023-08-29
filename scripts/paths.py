"""
Pastas do Projeto
mar.2023
"""


from pathlib import Path


# Project Path
project_path = Path(__file__).parents[1]


# Data
data_path = project_path / 'data'
data_path.mkdir(exist_ok=True)

# Input
input_path = data_path / 'input'
input_path.mkdir(exist_ok=True)


# Output
output_path = data_path / 'output'
output_path.mkdir(exist_ok=True)


if __name__ == '__main__':
    print(project_path)
