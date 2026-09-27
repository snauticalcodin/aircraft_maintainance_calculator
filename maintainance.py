class MaintenanceTask:
def init(self, task, interval, last_service, cost):
self.task = task
self.interval = interval
self.last_service = last_service
self.cost = cost

    self.next_service = last_service + interval
    self.remaining = 0
    self.status = "UNKNOWN"

def update_status(self, current_hours):
    self.remaining = self.next_service - current_hours

    if self.remaining < 0:
        self.status = "OVERDUE"
    elif self.remaining <= 50:
        self.status = "DUE SOON"
    else:
        self.status = "OK"
