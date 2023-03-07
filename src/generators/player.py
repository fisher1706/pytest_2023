from src.enums.user_enums import Statuses
from src.generators.plaer_localization import PlayerLocalization
from src.base_classes.builder import BuilderBaseClass


class Player(BuilderBaseClass):
    def __init__(self):
        super().__init__()
        self.reset()

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar='https://google.com'):
        self.result['avatar'] = avatar

    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result['localize'] = {
            'en': PlayerLocalization('en_US').build(),
            'ru': PlayerLocalization('ru_RU').build()
        }
        return self


if __name__ == '__main__':
    person = Player().set_balance(100).set_status('ZAPEL').build()
    print(person)
