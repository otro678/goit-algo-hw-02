import queue
import random
import time

requests_queue = queue.Queue()

request_id = 0

def generate_request():
    global request_id
    request_id += 1
    new_request = {
        "req_id": request_id
    }
    print(f"Generated new request: {new_request}")
    requests_queue.put(new_request)

def process_request():
    if not requests_queue.empty():
        current_request = requests_queue.get()
        print(f"Processing {current_request}")
        time.sleep(1)
        print(f"{current_request['id']} processed")
    else:
        print("Queue is empty")

def main():
    try:
        while True:
            generate_request()
            time.sleep(random.uniform(0.5, 2))
            process_request()
            
    except KeyboardInterrupt:
        print("Exiting the program.")

if __name__ == "__main__":
    main()