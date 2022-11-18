from mycroft import MycroftSkill, intent_file_handler


class Kerianne(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('kerianne.intent')
    def handle_kerianne(self, message):
        self.speak_dialog('kerianne')


def create_skill():
    return Kerianne()

