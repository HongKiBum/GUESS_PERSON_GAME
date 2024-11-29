import random
import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock

class GuessPersonGame(App):
    def __init__(self, questions=None, font_path=None, background_image=None, **kwargs):
        super().__init__(**kwargs)
        # 기본 경로 설정
        base_dir = os.path.dirname(os.path.abspath(__file__))
        resources_dir = os.path.join(base_dir, "resources")

        # 기본 리소스 경로
        self.font_path = font_path or os.path.join(resources_dir, "NanumGothic.ttf")
        self.background_image = background_image or os.path.join(resources_dir, "bg_image.jpg")

        # 기본 질문 데이터
        self.questions = questions or [
            {"image": os.path.join(resources_dir, "person_images", "태양.jpg"), "answer": "태양"},
            {"image": os.path.join(resources_dir, "person_images", "지디.jpg"), "answer": "지디"},
            {"image": os.path.join(resources_dir, "person_images", "대성.jpg"), "answer": "대성"},
        ]

        self.current_index = 0
        self.score = 0
        self.text_input = None
        self.result = None

    def build(self):
        self.root = FloatLayout()
        return self.show_question_screen()

    def show_question_screen(self):
        self.root.clear_widgets()
        bg_image = Image(source=self.background_image, allow_stretch=True, keep_ratio=False)
        self.root.add_widget(bg_image)

        content = BoxLayout(orientation="vertical", size_hint=(0.8, 0.8), pos_hint={"center_x": 0.5, "center_y": 0.5})

        self.image = Image(source=self.questions[self.current_index]["image"], size_hint=(1, 0.6))
        content.add_widget(self.image)

        if not self.text_input:
            self.text_input = TextInput(
                hint_text="정답을 입력하세요", multiline=False, size_hint=(0.5, 0.1),
                font_name=self.font_path, pos_hint={"center_x": 0.5}
            )
            self.text_input.bind(on_text_validate=self.check_answer)
        self.text_input.text = ""
        content.add_widget(self.text_input)

        submit_button = Button(
            text="제출", size_hint=(0.5, 0.1), font_name=self.font_path, pos_hint={"center_x": 0.5}
        )
        submit_button.bind(on_press=self.check_answer)
        content.add_widget(submit_button)

        self.result_label = Label(text="", size_hint=(1, 0.2), font_name=self.font_path)
        content.add_widget(self.result_label)

        self.root.add_widget(content)
        Clock.schedule_once(self.set_focus, 0.1)

    def set_focus(self, *args):
        if self.text_input:
            self.text_input.focus = True

    def check_answer(self, instance):
        user_input = self.text_input.text.strip()
        correct_answer = self.questions[self.current_index]["answer"]

        if user_input == correct_answer:
            self.result_label.text = "정답입니다!"
            self.result_label.color = (0, 1, 0, 1)
            self.score += 1
        else:
            self.result_label.text = f"오답입니다! 정답은 '{correct_answer}'였습니다."
            self.result_label.color = (1, 0, 0, 1)

        self.current_index += 1
        if self.current_index < len(self.questions):
            self.image.source = self.questions[self.current_index]["image"]
            self.text_input.text = ""
            Clock.schedule_once(self.set_focus, 0.1)
        else:
            self.result_label.text = f"게임 종료! 점수: {self.score}/{len(self.questions)}"
            self.result_label.color = (0, 0, 1, 1)
            self.text_input.disabled = True
            instance.disabled = True
            self.result = {"score": self.score, "total": len(self.questions)}
