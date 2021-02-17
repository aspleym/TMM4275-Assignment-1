

# TMM4275-Assignment-1

[![](https://img.shields.io/badge/HTML5-a?style=flat&logo=html5&label=Code&color=E34F26&logoColor=ffffff)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![](https://img.shields.io/badge/JavaScript-a?style=flat&logo=javascript&label=Code&color=F7DF1E&logoColor=ffffff)](https://www.javascript.com/)
[![](https://img.shields.io/badge/Python-a?style=flat&logo=python&label=Code&color=3776AB&logoColor=ffffff)](https://www.python.org/)
[![](https://img.shields.io/badge/CSS3-a?style=flat&logo=css3&label=Code&color=1572B6&logoColor=ffffff)](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
[![](https://img.shields.io/badge/Code-Json-informational?style=flat&logo=json&logoColor=white&color=000000)](https://www.json.org/json-en.html)  
[![](https://img.shields.io/badge/VSCode-a?style=flat&logo=visual-studio-code&label=Editor&color=007ACC)](https://code.visualstudio.com/)
[![](https://img.shields.io/badge/Three.js-a?style=flat&logo=three.js&label=Library&color=000000&logoColor=ffffff)](https://threejs.org/)
[![](https://img.shields.io/badge/NX-a?style=flat&logo=siemens&label=CAD&color=009999&logoColor=ffffff)](https://www.plm.automation.siemens.com/global/en/products/nx/)
[![](https://img.shields.io/badge/Fuseki-a?style=flat&logo=apache&label=Server&color=D22128&logoColor=ffffff)](https://jena.apache.org/documentation/fuseki2/index.html)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/maintenance/no/2021)

## Table of Contents

- [Task](#taskl)
  - [Built With](#built-with)
    - [Libraries](#libraries)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Download project](#download-project)
  - [Run the system](#run-the-system)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [File Structure](#file-structure)
- [Contributors](#contributors)
- [License](#license)

## Task

You have founded a company implementing KBE systems for various manufacturers. This time you have received an offer to build the KBE for the factory making furniture. In particular, a parametric design of a chair shall be made. Customers should be able to define the “sizes”/”shapes” of different elements of the chair and observe the result as well as if it is possible to make. Customer wishes should be checked with the capabilities at the production floor.

## Sketch and architecture
![image of ui example](https://github.com/aspleym/TMM4275-Assignment-1/blob/main/images/ui.png)

![image of client-server architecture](https://github.com/aspleym/TMM4275-Assignment-1/blob/main/images/Client-server%20architecture.png)

### Built With

Everyone that contributed to the project used Visual Studio Code to develop this software. The next section has a list of libraries and applications that have been used in this project. The names are linked to one of the developers home page for the library.

#### Libraries

- [Three.js](https://threejs.org/)
- [http.server](https://docs.python.org/3/library/http.server.html)
- [socketserver](https://docs.python.org/3/library/socketserver.html)
- [Requests](https://requests.readthedocs.io/en/master/)
- [os](https://docs.python.org/3/library/os.html)
- [json](https://docs.python.org/3/library/json.html)

## Getting Started

### Prerequisites

To run this project you would need to install [Python](https://www.python.org/) to run the website and [Java](https://www.java.com/en/) if you want to run the Fuseki server with Java.

### Download project

This section will guide you to clone this git repository. Type the following lines in the terminal (for **_unix_** users):

```sh
cd /to-your-desired-directory
git clone https://github.com/aspleym/TMM4275-Assignment-1.git
cd TMM4275-Assignment-1
```

You are now inside the project folder.

Type `ls` in the terminal to see the root folder structure.

### Run the system

In this section you will be guided step by step on how to run the system on your computer.
#### Fuseki server
- Go to the directory of the project
- Enter the directory for the Fuseki server, `fuseki-server`.
- Execute one of the fuseki-server files depending on your operating system:
	- fuseki-server `UNIX`
	- fuseki-server.bat `WINDOWS`
	- fuseki-server.jar `JAVA`

#### Adding OWL model
- To add the OWL model to the server, open a web browser and type in the following un the URL field: `localhost:3030`.
- Locate the dataset named /kbe: `http://localhost:3030/dataset.html`
- Select the tab *upload files* and then hit the button *+ select files...* to add the OWL-model to the Fuseki server.
	- The owl file should be: `project-directory/fuseki-server/owl-files/shapes.owl`
- Press the button *upload all* and verify that the upload was successful.
#### Web server
- To run the Python server, start by opening a command-line interpreter like CMD or Termnial.
- Navigate to the project directory by using commands like `cd`.
- When inside project folder, type the following to execute check Python version:
```sh
python --version
```
- You should verify that you are using **Python 3**.
- To execute the web server, type the following and press enter:
```sh
python httpserver.py
```
- The web server should be available at: `localhost:8080` in the web browser.
## Usage
The website *ChairMaker* is able to simulate and create DFA-files for chair products of three types. Dining-, stool- and modern chair. These different types of chairs have some parameters that can be changed and visualized in a preview window before *ordering* the DFA file.

If the values in the parameters are valid, the user will be directed to a *order page* where it will be possible to view the chair and download the corresponding DFA file.
## Roadmap

We have no further plans for this school project. Until there are changes to our roadmap, this project will have no maintenance of the code as of 19. February 2021.

## File structure

This is an overview of the file structure for this repository and a short explanation for some of the files.

```
TMM4275-Assignment-1
│   .gitignore					A file to tell Github to ignore files.
│   httpserver.py				httpserver.py: Python script to execute a http server for the customer.
│   queries.txt					A txt file with examples of queries in SPARQL.
│   README.md					This file.
│
├───ChairMaker
│   │   index.html				Main HTML file with fields to recieve chair paramters and a 3d preview with three.js.
│   │   main.css				CSS for styling of the index.html file.
│   │   order.css				CSS for styling of the order.html file.
│   │   order.html				Order HTML file where you see final preview and a download link for the DFA file.
│   │
│   └───js					JavaScript files to visualize the Chair in 3d
│           dining_chair.js			Script to build a dining chair in Three.js.
│           modern_chair.js			Script to build a modern chair in Three.js.
│           OrbitControls.js			Camera controll
│           order.js				JavaScript for order page.
│           preview.js				Preview script
│           stool_chair.js			Script to build a stool chair in Three.js.
│           three.js				The Three.js library
│           three.min.js			Support file for Three.js
│           three.module.js			Support file for Three.js
│
├───fuseki-server				Fuseki server files to execute the server.
│   │   fuseki-server
│   │   fuseki-server.bat
│   │   fuseki-server.jar
│   │   
│   ├───owl-files
│   │       shapes.owl				The OWL model.
│
├───images					Images for the README
│       Client-server architecture.png
│       ui.png
│
├───products					A folder to store chair DFA files.
│   └───templates				Templates for different chair types as a DFA file.
│           diningChair.dfa
│           modernChair.dfa
│           stoolChair.dfa
│
└───py
    │   fusekiposter.py				The Python file that contains functions to post chairs to the Fuseki server.
    │   generateDFA.py				Functions to generate DFA files of chairs.
```
## Contributors

[<img src="https://github.com/Magwest1.png?size=50" alt="" data-canonical-src="" width="50" height="50" />](https://github.com/Magwest1)  
Magnus Ølstad  

[<img src="https://github.com/aspleym.png?size=50" alt="" data-canonical-src="" width="50" height="50" />](https://github.com/aspleym)  
Adrian Pleym  

## LICENSE

Distributed under the [MIT](https://opensource.org/licenses/MIT) License.
