import time

class Train:
    train_count = 0

    def __init__(self, direction, priority, loading_time, crossing_time):
        self.id = Train.train_count
        Train.train_count += 1
        self.direction = direction
        self.priority = priority
        self.loading_time = loading_time
        self.crossing_time = crossing_time

def train_thread_function(train, controller):
    time.sleep(train.loading_time)
    print(f"Train {train.id} has finished loading.")
    controller.add_train_to_queue(train)
    controller.allow_train_to_cross(train)

