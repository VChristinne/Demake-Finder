# Demake Finder

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://docker.com/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)


## 📖 Description
This project is a demake for macOS Finder in CLI. 

Key features:
- **Navigate** through files and directories
- **Open** files
- **Create** new files and directories
- **Delete** files and directories
- **Search** for files and directories
- **Copy** files and directories

## ⚙️ Installation
1. Clone the repository
2. Run the following command to build the Docker image:
```
docker build -t demake-finder .
```
3. Run the following command to start the Docker container:
```
docker run -it --name run-df demake-finder
```
4. You can now use the demake Finder in the CLI.
5. To stop the container, run the following command:
```
docker stop run-df
```
6. To remove the container, run the following command:
```
docker rm run-df
```


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
│   └── ui
│   └── shared
└── entrypoint.py
```

## 📑 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.