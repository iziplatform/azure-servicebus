from azure.servicebus import ServiceBusClient, ServiceBusMessage, ServiceBusError
import json
from dotenv import load_dotenv
import os
from colorama import Fore, Style

# Load environment variables from .env file
load_dotenv()

# Azure Service Bus connection string
connection_str = os.getenv("CONNECTION_STRING")

# Name of the queue
queue_name = os.getenv("QUEUE_NAME")

# Path to the JSON file containing messages
json_file_path = os.getenv("JSON_FILE_PATH")


def send_messages_to_service_bus(connection_str, queue_name, messages):
    # Create a ServiceBusClient using the connection string
    servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str)

    # Create a sender for the queue
    sender = servicebus_client.get_queue_sender(queue_name=queue_name)

    sent_messages_count = 0
    successfully_sent_count = 0
    with sender:
        # Send each message to the queue
        for idx, msg in enumerate(messages):
            try:
                message = ServiceBusMessage(json.dumps(msg))
                sender.send_messages(message)
                sent_messages_count += 1
                successfully_sent_count += 1
                print(Fore.GREEN + f"Sent message {idx + 1}/{len(messages)} successfully" + Style.RESET_ALL)
            except ServiceBusError as e:
                sent_messages_count += 1
                print(Fore.RED + f"Failed to send message {idx + 1}/{len(messages)}: {e} - Message: {msg}" + Style.RESET_ALL)

    return sent_messages_count, successfully_sent_count


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


if __name__ == "__main__":
    # Read JSON messages from file
    messages = read_json_file(json_file_path)

    # Send messages to Azure Service Bus
    sent_count, successfully_sent_count = send_messages_to_service_bus(connection_str, queue_name, messages)
    print(Fore.BLUE + f"Total messages sent: {sent_count}" + Style.RESET_ALL)
    print(Fore.BLUE + f"Successfully sent messages: {successfully_sent_count}" + Style.RESET_ALL)
