import datetime


class EventManager:
    def __init__(self, repository):
        self.repository = repository

    def get_by_id(self, event_id):
        ret = self.repository.find({'event_id': event_id})
        return ret

    def get_by_day(self, first_day, last_day):
        pass

    def get_by_tag(self, tag):
        pass

    def update(self, event_id, name, date, tag):
        pass

    def delete(self, event_id):
        pass

    def add(self, subject, detail, deadline, tag):
        pass
