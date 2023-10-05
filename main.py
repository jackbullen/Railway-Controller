from train import Train, train_thread_function
from controller import RailwayController
import threading

def main():
    controller = RailwayController()
    trains = []

    with open('input.txt', 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            direction, loading_time, crossing_time = line.strip().split()
            priority = direction.upper()
            train = Train(direction, priority, float(loading_time)/10, float(crossing_time)/10)
            trains.append(train)

    threads = []
    for train in trains:
        thread = threading.Thread(target=train_thread_function, args=(train, controller))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All trains have crossed.")

if __name__ == "__main__":
    main()
