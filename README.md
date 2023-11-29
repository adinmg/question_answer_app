# Question-Answering System 🤖

## Project Overview

Welcome to our Question-Answering System project! This project introduces an advanced question-answering system that strategically opts for a model optimized for low latency, minimal resource requirements, and impressive efficiency. Welcome to a world where intelligence meets practicality, transforming the landscape of information retrieval.


In this project, we harness the power of a finely-tuned [**miniLM**](https://www.sbert.net/) language model. The choice of miniLM is deliberate, driven by its compact size-making it an excellent fit for environments with low latency requirements and resource limitations. Our focus on efficiency ensures that the system delivers swift responses even in constrained computing environments.

## Training with SQuAD Dataset 📘

At the core of our system's intelligence is the renowned SQuAD dataset. By training our language model on SQuAD, a gold standard in question-answering, we empower it to comprehend and respond to a diverse array of questions with context. This training enhances its effectiveness in real-world scenarios.

## Fine-Tuning with Hugging Face Transformer LLM 🚀

In the quest to refine our Question-Answering System, we fine-tuned the language model using Hugging Face Transformers. This process allows us to tailor the model to the specific nuances and intricacies of our application.

## Performance Metrics: miniLM vs BERT 📊

Our pursuit of a well-balanced trade-off between model size, speed, and accuracy led us to compare miniLM against the heavyweight BERT model. While miniLM achieved an F1 score of 82.8%, slightly below BERT's 88.6%, the real marvel lies in miniLM's efficiency. Despite its reduced accuracy, miniLM is a lightweight alternative, boasting a mere 90.9 MB in size. What's truly remarkable is its speed; miniLM is approximately 10 times faster than BERT, which weighs in at a hefty 436 MB.

## PEFT/LoRA Technique on a Larger LLM. 🌐

Under Development  ...


## Flask App for Seamless Interaction 🌐

To facilitate seamless interaction with our Question-Answering System, I've integrated a Flask web application. This user-friendly interface allows users to effortlessly input queries and receive instant answers. The Flask app ensures that the power of our system is accessible to users of all levels, making information retrieval a breeze.

## Scaling Up with Azure Virtual Machine ☁️

As we envision scaling up our system to handle increased demand and complexity, we turn to the cloud infrastructure provided by Azure Virtual Machines. This robust and scalable environment ensures that our Question-Answering System can accommodate growing user needs while maintaining optimal performance and reliability.

## Docker Deployment for Efficiency 🐳

Efficiency is at the core of our deployment strategy. Leveraging Docker containers, we encapsulate our system and its dependencies, providing a consistent and efficient runtime environment. Docker deployment not only streamlines the setup process but also enhances portability and scalability, making our Question-Answering System ready for diverse deployment scenarios.


## Table of Contents

1. [Project Highlights](#1-project-highlights)

2. [Why Question Answering?](#2-why-question-answering)

3. [Get Started](#3-get-started)

4. [Deploying on Azure Virtual Machines](#4-deploying-on-azure-virtual-machines)

5. [Docker Deployment](#5-docker-deployment)


## 1. Project Highlights

- **Transformer LLM Fine-Tuning:** Find detailed insights in the notebook file [Question_Answering_System_Using_LLMs.ipynb](https://github.com/adinmg/question_answering_app.git/Question_Answering_System_Using_LLMs.ipynb).

- **PEFT/LoRA Technique:** Under Development.

<!-- Explore an additional fine-tuning technique, the PEFT/LoRA method. Refer to [Question_Answering_System_Using_LLMs.ipynb](https://github.com/adinmg/question_answering_app.git/Question_Answering_System_Using_LLMs.ipynb) for a comprehensive understanding. -->


## 2. Why Question Answering?

Question Answering (QA) plays a pivotal role in the realm of Information Retrieval, especially when powered by Large Language Models (LLMs). Here are some key reasons why QA is crucial:

1. **Efficient Information Access:**
   - QA systems enable users to retrieve information with precision and speed by allowing them to formulate queries in natural language. This streamlines the process of obtaining specific details from vast datasets.

2. **User-Friendly Interaction:**
   - LLM-based QA systems provide a user-friendly interface, making it accessible to individuals with varying levels of technical expertise. Users can engage with the system using everyday language, eliminating the need for complex search queries.

3. **Personalization and Contextual Understanding:**
   - LLMs excel at understanding context and can provide personalized responses. By considering the context of a query, QA systems powered by LLMs can deliver more accurate and relevant information tailored to the user's needs.

4. **Handling Ambiguity and Nuances:**
   - Natural language is often ambiguous and nuanced. LLMs, with their advanced language understanding capabilities, excel in deciphering the subtleties of human language. This enables QA systems to handle a wide range of queries with varying degrees of complexity.

6. **Real-Time Information Retrieval:**
   - QA systems, powered by efficient LLMs, can provide real-time responses, making them invaluable in scenarios where up-to-date information is crucial. This real-time capability ensures that users receive the latest and most relevant information.

7. **Applications Across Industries:**
   - QA systems find applications in diverse industries, including healthcare, education, customer support, and more. They act as intelligent assistants, aiding professionals and individuals in obtaining information quickly and accurately.


## 3. Get Started

Clone the Book Genre Classifier repository and explore the precision of diverse approaches to revolutionize book genre classification.

```bash
git clone https://github.com/adinmg/question_answering_app.git
```

### Requirements

Ensure a seamless setup by installing the required packages listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Flask Integration

1. Navigate to the project directory:

   ```bash
   cd book_genre_classifier
   ```

2. Run the Flask app:

   ```bash
   python app.py
   ```

3. Access the Question Answering App at `http://127.0.0.1:5000/` in your web browser to interact with the classification system.


## 4. Deploying on Azure Virtual Machines

1. **Create an Azure Virtual Machine:**
   - Log in to your Azure Portal.
   - Navigate to Virtual Machines and create a new virtual machine.
   - Choose an appropriate Linux Operating System (e.g., Ubuntu) and configure instance details.

2. **Configure Network Security Groups:**
   - Set up Network Security Groups (NSG) to allow inbound traffic on the necessary ports. For our Question Answering App, ensure that you open the following ports:
     - Port 80 (HTTP): Ensure that this port is open for general web traffic.

   You can configure these settings in the Azure Portal under the Network Security Groups section for your Azure Virtual Machine.


3. **SSH into the Azure Virtual Machine:**
   - Use the provided SSH key pair to connect to your Azure Virtual Machine.

4. **Clone the Repository:**
   - Clone the Question Answering App repository into your Azure Virtual Machine:

   ```bash
   git clone https://github.com/your-username/question_answering_app.git
   ```

   ```bash
   cd question_answering_app
   ```

   - Create a virtual environment:

   ```bash
   python -m venv venv
   ```

   - Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

5. **Install Dependencies:**
   - Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

6. **Test the App in Gunicorn:**
   - Run the app using Gunicorn:

   ```bash
   gunicorn -b 0.0.0.0:8000 app:app
   ```

   (Make sure you are in the app folder)

7. **Configure Gunicorn Service:**
   - Create a Gunicorn service configuration file:

   ```bash
   sudo nano /etc/systemd/system/myapp.service
   ```

   **"myapp.service" file:**

   ```ini
   [Unit]
   Description=gunicorn instance for a simple flask app
   After=network.target

   [Service]
   User=your-username
   Group=www-data
   WorkingDirectory=/home/your-username/question_answering_app
   ExecStart=/home/your-username/question_answering_app/venv/bin/gunicorn -b localhost:8000 app:app
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

8. **Restart Daemon:**
   - Reload the systemd daemon to apply the changes:

   ```bash
   sudo systemctl daemon-reload
   ```

9. **Start the Gunicorn Service:**
    - Start the Gunicorn service:

    ```bash
    sudo systemctl start myapp
    ```

10. **Enable the Gunicorn Service:**
    - Enable the Gunicorn service to start on boot:

    ```bash
    sudo systemctl enable myapp
    ```

11. **Install Nginx:**
    - Install the Nginx web server:

    ```bash
    sudo apt install nginx
    ```

12. **Start Nginx:**
    - Start the Nginx service:

    ```bash
    sudo systemctl start nginx
    ```

13. **Enable Nginx:**
    - Enable Nginx to start on boot:

    ```bash
    sudo systemctl enable nginx
    ```

14. **Edit Nginx Default File:**
    - Open the default Nginx configuration file for editing:

    ```bash
    sudo nano /etc/nginx/sites-available/default
    ```

15. **Modify Default File:**
    - Add the following upstream block and modify the location block:

    ```nginx
    # Default server configuration (add)
    upstream myapp {
        server 127.0.0.1:8000;
    }

    # modify location
    location / {
        ...
        proxy_pass http://myapp;
    }
    ```

16. **Restart Nginx:**
    - Restart the Nginx service to apply the changes:

    ```bash
    sudo systemctl restart nginx
    ```

17. **Debug NGINX if necessary:**
    - Check the Nginx error log for debugging:

    ```bash
    sudo tail /var/log/nginx/error.log
    ```

Now, your Question Answering App is deployed on Azure Virtual Machine with Gunicorn and Nginx for efficient and reliable web service.


## 5. Docker Deployment

1. Ensure Docker is installed on your machine.

2. Build the Docker image:

   ```bash
   docker build -t question-answer-app .
   ```

3. Run the Docker container:

   ```bash
   docker run -p 5000:5000 question-answer-app
   ```

4. Access the Question Answering App at `http://127.0.0.1:5000/` in your web browser to experience the precision of diverse approaches in book genre classification.

