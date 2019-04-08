import datetime


class EventManager:
    def __init__(self, repository):
        self.repository = repository

    def get_by_id(self, event_id):
        ret = self.repository.find({'event_id': event_id})
        return ret

    def get_by_day(self, first_day: datetime.date, last_day: datetime.date):
        ret = self.repository.find(
            {
                'date':
                {
                    '$gte': first_day.isoformat(),
                    '$lte': last_day.isoformat()
                }
            }
        )
        return ret

    def get_by_tag(self, tag):
        pass

    def update(self, event_id, name, date, tag):
        pass

    def delete(self, event_id):
        pass

    def add(self, subject, detail, deadline, tag):
        pass
