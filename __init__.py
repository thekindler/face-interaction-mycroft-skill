import time

from mycroft import MycroftSkill, intent_file_handler, Message


class FaceInteraction(MycroftSkill):

    initializer=None

    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('interaction.face.intent')
    def handle_face_interaction(self, message):
        name=str(message.data.get('name'))
        print(name)
        self.speak("welcome Mr. "+name+" to confluence 2019")

        answer=self.get_response("how was your travel Mister "+name+ "?")

        if 'ok' in answer or 'not' in answer or 'hectic':
            answer=self.get_response("ooh.. in that case can i entertain you with a joke")
            if 'yes' or 'joke' in answer:
                self.speak("okay here goes a joke....")
                self.bus.emit(Message("recognizer_loop:utterance",
                                      {'utterances': ["joke"],
                                       'lang': 'en-us'}))

            else:
                self.speak("okay here goes a song....")
                self.bus.emit(Message("recognizer_loop:utterance",
                                      {'utterances': ["sing a song"],
                                       'lang': 'en-us'}))

        time.sleep(6)
        answer = self.get_response("would you also like to see some demo?")
        if 'yes' in answer:
            self.speak("alright here you go: dham dham dham")

def create_skill():
    return FaceInteraction()

