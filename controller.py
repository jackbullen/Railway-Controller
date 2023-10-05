import time
import threading

class RailwayController:
    def __init__(self):
        self.main_track_mutex = threading.Lock()
        self.east_queue = []
        self.west_queue = []
        self.last_direction = None
        self.consecutive_same_direction = 0

    def add_train_to_queue(self, train):
        if train.direction in ['e', 'E']:
            self.east_queue.append(train)
        else:
            self.west_queue.append(train)

    def get_next_train(self):
        # Check for high-priority trains first
        if self.east_queue and (self.east_queue[0].priority == 'E'):
            return self.east_queue.pop(0)
        if self.west_queue and (self.west_queue[0].priority == 'W'):
            return self.west_queue.pop(0)
        
        # Check for low-priority trains
        if self.east_queue:
            return self.east_queue.pop(0)
        if self.west_queue:
            return self.west_queue.pop(0)
        return None

    def allow_train_to_cross(self, train):
        with self.main_track_mutex:
            print(f"Train {train.id} is crossing the main track.")
            time.sleep(train.crossing_time)
            print(f"Train {train.id} has finished crossing.")