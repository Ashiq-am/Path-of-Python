import abc
import time
import datetime


class Subject(object):
    def __init__(self):
        self.observers = []
        self.cur_time = None

    def register_observer(self, observer):
        if observer in self.observers:
            print(observer, 'already registered')
        else:
            self.observers.append(observer)

    def unregister_observer(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Cannot Indentify the Observer')

    def notify_observer(self):
        self.cur_time = datetime.datetime.now()

        for observer in self.observers:
            observer.notify(self.cur_time)


class Observer(object, metaclass=abc.ABCMeta):
    """ Abstract class for Observers """

    @abc.abstractmethod
    def notify(self, unix_timestamp):
        pass


class CompanyNewsletterObserver(Observer):
    """ Company Newsletter """

    def __init__(self, name):
        self.name = name

    def notify(self, time):
        print(self.name, ':', time)


class ConsumerNewsletterObserver(Observer):
    """ Consumer Newsletter """

    def __init__(self, name):
        self.name = name

    def notify(self, time):
        print(self.name, ':', time)


if __name__ == '__main__':
    subject = Subject()

    print('Registering company_newsletter_observer')
    cmp_observer = CompanyNewsletterObserver('company_newsletter_observer')
    subject.register_observer(cmp_observer)
    subject.notify_observer()
    print()
    time.sleep(2)

    print('Registering consumer_newsletter_observer')
    con_observer = ConsumerNewsletterObserver('consumer_newsletter_observer')
    subject.register_observer(con_observer)
    subject.notify_observer()
    print()
    time.sleep(2)

    print('Unregistering company_newsletter_observer')
    subject.unregister_observer(cmp_observer)
    subject.notify_observer()
