from .Media import Media

class PlayerQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.is_looping = False
        self.is_replaying = False

    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        new_media = Media(item)
        if self.head is None:
            self.head = new_media
        if self.tail:
            self.tail.next = new_media
        self.tail = new_media

    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        path = self.head.path
        if not self.is_replaying:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            if self.is_looping:
                self.enqueue(path)
        return path

    def replay(self):
        self.is_replaying = not self.is_replaying

    def loop(self):
        self.is_looping = not self.is_looping

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.path.split('/')[-1])
            current = current.next
        return "Queue: " + str(result)