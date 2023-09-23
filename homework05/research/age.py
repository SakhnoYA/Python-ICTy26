import datetime as dt
import statistics
import typing as tp

from vkapi.friends import get_friends


def age_predict(user_id: int) -> tp.Optional[float]:
    """
    Наивный прогноз возраста пользователя по возрасту его друзей.

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: Идентификатор пользователя.
    :return: Медианный возраст пользователя.
    """
    ages = []
    current_time = dt.date.today().year
    friends = get_friends(user_id, fields=["bdate"]).items
    for friend in friends:
        try:
            bdate = dt.datetime.strptime(friend["bdate"], "%d.%m.%Y").year  # type: ignore
        except (KeyError, ValueError):
            continue
        ages.append(current_time - bdate)
    try:
        return statistics.median(ages)
    except statistics.StatisticsError:
        return None
