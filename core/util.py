import datetime


def build_date_query(first_day: datetime.date = None, last_day: datetime.date = None):
    query = {}
    if first_day is not None:
        query.update({'$gte': first_day.isoformat()})
    if last_day is not None:
        query.update({'$lte': last_day.isoformat()})

    return query
