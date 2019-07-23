from mycroft import MycroftSkill, intent_file_handler


class FaceInteraction(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('interaction.face.intent')
    def handle_interaction_face(self, message):
        self.speak_dialog('interaction.face')


def create_skill():
    return FaceInteraction()

