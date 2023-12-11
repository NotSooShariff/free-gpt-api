# GPT-Tokenizer API 🤖

> ⚠️ Note - This GPT-Tokenizer API is a personal side project that I developed because I was running out of GPT tokens for use in various projects via the OpenAI API xD. But since I found a MUCH more well-maintained and better-suited repository [G4F](https://github.com/xtekky/gpt4free) , I will no longer be working on this or maintaining it.

## Overview 📜

This is based on Selenium, which allows it to make requests through a browser and provide responses in a format usable by other APIs. Please note that this project is still under development and may have limitations.

## Quick Links 🔗


- [Overview](#overview)
- [Table of Contents](#table-of-contents)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Solutions](#solutions)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Getting Started 🚀

### Prerequisites 📋

Before running the GPT-Tokenizer API, you'll need the following prerequisites:

- Python 3.x
- Selenium
- Chrome WebDriver
- Ngrok (optional, for web access)

### Installation 💻

1. Clone the repository to your local machine:

```bash
git clone https://github.com/NotSooShariff/free-gpt-api.git
```

2. Install the required Python packages:

```bash
cd free-gpt-api
pip install -r requirements.txt
```

## Usage 🧑‍💻

To run the GPT-Tokenizer API, follow these steps:

1. Navigate to the API directory:

```bash
cd api
```

2. Run the `app.py` script:

```bash
python app.py
```

3. In another terminal, you can make requests to the API using the provided `apitest.py` script located in the `testcode` directory:

```bash
cd ../testcode
python apitest.py
```

## Solutions 🛠️

As mentioned earlier, due to the way Selenium works (by popping up a browser locally), containerizing this project has been challenging. However, there are a few ways to use this project:

1. **Ngrok Tunneling**: You can use Ngrok to open a tunnel to your computer's port and make the API accessible via an external URL. This allows you to use the API remotely.

2. **Local Server**: You can run the API on your local server and use it locally. This is suitable for testing and development purposes.

## Directory Structure 📁

The repository is structured as follows:

- `__pycache__/`: Cache files generated by Python.
- `api/`: Contains the API code.
  - `app.py`: The main API script.
- `testcode/`: Contains scripts for testing the API.
  - `apitest.py`: A script for testing API requests.
- `app.yaml`: Configuration file (if applicable).
- `Dockerfile`: Dockerfile for containerization (work in progress).
- `requirements.txt`: List of required Python packages.

## Contributing 🤝

Contributions to this project are welcome! This project is under development and I appreciate any help. Feel free to open issues, suggest improvements, or submit pull requests. Please review our [contribution guidelines](CONTRIBUTING.md) for more details.

## Disclaimer ⚠️

This project, [Free GPT API](https://github.com/NotSooShariff/free-gpt-api), operates by scraping data from [OnlineGPT](https://onlinegpt.org/) which allows you to use ChatGPT without signup due to it being an ad based model. While I have not found any information in their website or terms and conditions that prohibits the use of web scrapers, I want to clarify that my intention is not to infringe upon any terms or policies set by [OnlineGPT](https://onlinegpt.org/).

If anyone associated with [OnlineGPT](https://onlinegpt.org/) has concerns about the usage of their website in this project, I am open to addressing those concerns promptly. Please feel free to reach out, and I will respect any request to modify or discontinue the use of web scraping on their website.

I aim to maintain ethical and respectful practices in all aspects of this project and its interactions with external resources. Your feedback and concerns are important to me, and I am committed to addressing them in a responsible and cooperative manner. Thank you for your understanding and cooperation.
