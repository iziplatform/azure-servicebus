# Azure Service Bus Message Sender

This Python script allows you to send messages from a JSON file to an Azure Service Bus queue.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your machine (version 3.6 or higher)
- An Azure subscription
- A Service Bus namespace and a queue created in Azure

## Installation

1. Clone or download this repository to your local machine.

2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```
3. Create a .env file in the root directory of the project and add the following environment variables:
```commandline
CONNECTION_STRING=<Your Azure Service Bus connection string>
QUEUE_NAME=<Your Azure Service Bus queue name>
JSON_FILE_PATH=<Path to your JSON file containing messages>
```
## Usage
Run the script using the following command:
```python
python sendMessages.py
```
The script will read the messages from the JSON file specified in the .env file and send them to the Azure Service Bus queue specified.

## Additional Notes
- If any message fails to be sent, the script will print an error message indicating which message failed.
- Make sure your JSON file contains valid JSON objects or an array of JSON objects.
- Ensure that your Azure Service Bus namespace and queue are correctly set up with the necessary permissions.

For more information about Azure Service Bus, refer to the [Azure documentation](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview).

## License
This project is licensed under the MIT License - see the [LICENSE]() file for details.

Feel free to customize this `README.md` file further according to your project's specific details and requirements.



