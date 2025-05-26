# Scraper Server

This is a **Scraper Server** project developed using **Flask**, which utilizes **Selenium** with **undetected_chromedriver** to scrape information from Google, particularly related to product search results.

The server accepts a **POST** request with a `desc` parameter, which is used as part of a Google search query. The scraper returns the titles and descriptions of the search results.

## 🚀 Features

- **Google Search**: The server performs a web search using the description provided in the POST request.
- **Selenium with undetected_chromedriver**: Uses `undetected_chromedriver` to bypass Google’s detection of Selenium.

## 🛠 Technologies

- **Flask**: Python web framework.
- **Selenium**: Browser automation tool.
- **undetected_chromedriver**: Used to avoid detection by Google.
- **Docker**: For containerizing the environment.
- **Python 3.8+**: Programming language used.

## ⚡ Installation

### 1. Cloning the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/scraper-server.git
cd scraper-server
```

### 2. Creating a Virtual Environment
It's recommended to use a virtual environment to isolate the project dependencies. To create a virtual environment, run:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3. Installing Dependencies
Install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

### 4. Running the Project
Once the dependencies are installed, you can run the server locally:

```bash
python app.py
```
The server will be available at http://localhost:5000.

## 🐳 Running with Docker
If you prefer to run the project using Docker, follow the steps below.

### 1. Building the Docker Image
To build the Docker image, run the following command at the root of the project:

```bash
docker build -t scraper-server .
```
### 2. Running the Docker Container
After building the image, you can run the container:

```bash
docker run -p 5000:5000 scraper-server
```

## 📡 Using the Endpoint
The application exposes a POST endpoint to perform Google searches.

### 1. Search Endpoint
**URL:** /buscar

**Method:** POST

**Parameter:**
* **desc:** A description of the product or term to be searched on Google (example: "raspberry pi").

Example Request (using curl):
```bash
curl -X POST http://localhost:5000/buscar \
    -H "Content-Type: application/json" \
    -d '{"desc": "raspberry pi"}'
```

### Example Response:

```bash
[
    {
        "titulo": "Raspberry Pi 4 Model B",
        "desc": "Buy the fastest Raspberry Pi 4 Model B from various stores."
    },
    {
        "titulo": "Raspberry Pi 4 Kit",
        "desc": "Complete kit with Raspberry Pi 4, case, and accessories."
    }
]
```

## 🔧 Debug and Development

### 1. Running the Server in Development Mode
If you need a development mode with debugging, run the server with the **debug=True** parameter:

```bash
app.run(host="0.0.0.0", port=5000, debug=True)
```

### 2. Logs and Debugging
While the server is running, Flask will generate logs in the terminal which can be useful for debugging.

## 🛠 Dependencies
The project dependencies are listed in the requirements.txt file:
* Flask
* Selenium
* undetected_chromedriver
* ...

If you need to add more dependencies, simply edit the requirements.txt file and run:

```bash
pip install -r requirements.txt
```

## ⚠️ Warnings and Limitations
* Selenium Usage: Selenium usage may be blocked by Google in some cases. The undetected_chromedriver library helps to bypass these blocks but does not guarantee 100% success.
* Performance: Response time may vary depending on your internet connection and how long Google takes to load search results.

## 💡 Contributing
If you want to contribute to this project, feel free to open issues or pull requests. Your contribution will be greatly appreciated!

## 📜 License
This project is licensed under the MIT License. See the [MIT License](https://opensource.org/licenses/MIT) for more details.


Author: Fabio Batista Rodrigues
Email: fabiob.rodrigues123@gmail.com


### Translation Breakdown:

- **General Description**: Translated the purpose and functionalities of the scraper.
- **Installation and Running**: Translated the setup instructions for local installation and Docker setup.
- **Usage Instructions**: Translated how to use the endpoint with an example.
- **Debugging and Development**: Provided info on running the server in debug mode.
- **Dependencies**: Explained how to install dependencies.
- **Warnings**: Information about limitations and potential issues with Google blocking Selenium.

Feel free to copy and paste esse arquivo no seu repositório e adaptá-lo conforme necessário. Se precisar de mais alguma coisa, estou à disposição!

