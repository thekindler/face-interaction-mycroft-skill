from mycroft import MycroftSkill, intent_file_handler, Message
from flask import Flask, jsonify

app = Flask(__name__)

class FaceSkill(MycroftSkill):

    def __init__(self):
        # pass
        MycroftSkill.__init__(self)

    def start_face_interaction_skill(self):
        print("inside face interaction skill")
        self.bus.emit(Message("recognizer_loop:utterance",
                              {'utterances': ["face recognition greet anupam"],
                               'lang': 'en-us'}))

@app.route('/face_skill_activation', methods=['POST'])
def face_skill_activation():
    print("inside face recognitin")
    faceskill=FaceSkill()
    faceskill.start_face_interaction_skill()

    return jsonify("ok")

if __name__ == '__main__':
     app.run(debug=True)