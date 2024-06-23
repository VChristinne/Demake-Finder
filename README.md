# Demake Finder

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://docker.com/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)


## 📖 Description
This project is a demake for macOS Finder in CLI. 

Key features:
- **Navigate** through files and directories
- **Open** directories
- **Create** new files and directories
- **Delete** files and directories
- **Search** for files and directories
- **Copy** files and directories

## ⚙️ Installation
1. Clone the repository
```
git clone https://github.com/VChristinne/demake-finder.git
```
2. Navigate to the project directory
```
cd demake-finder
```
3. Make the `run.sh` script executable (docker installation)
```
chmod +x run.sh
```
4. Run the script to start the application
```
./run.sh <directory_path> [-h][-s][-d][-v]
```
5. To stop and remove the container, run the following command
```
docker stop run-df && docker rm run-df
```

## 📝 Usage
- **List files and directories**: `entrypoint.py <directory_path> [-h][-s][-d][-v]`
  - Optional arguments:
    - `-h` or `--help`: Display the help message
    - `-s` or `--size`: Display the size of the files and directories
    - `-d` or `--date`: Display the date of the files and directories
    - `-v` or `--verbose`: Display the size and date of the files and directories

## 🗂️ Project Structure
Using the **Component-Based Architecture**, the project is structured as follows:
```
├── Dockerfile
├── LICENSE
├── README.md
├── components
│   ├── file_management
│   │   ├── copy
│   │   ├── delete
│   │   ├── list
│   │   └── move 
│   ├── navigation
│   ├── search
│   ├── ui
│   │   └── cli_controller
│   ├── shared
│   │   ├── config
│   │   └── utils
├── run.sh
└── entrypoint.py
```

## 📑 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
