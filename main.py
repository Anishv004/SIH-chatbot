from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.properties import StringProperty, NumericProperty
from kivy.core.text import LabelBase
#from chat_bot import resp
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from main import value
chatbot = ChatBot('Chatbot')

trainer = ListTrainer(chatbot)

trainer.train([
               'Can I still place a new order with Aflin?',
               'Yes. For purchases with free delivery, shop online at aflin.com/shop or with the Apple Store app. You can also place an order and select a time for contactless pickup at your nearest open Aflin Store.',
               'Can I return or exchange my product at my local Aflin Store?',
               'For products purchased online, you can start a no-contact return at aflin.com/orderstatus. For purchases made at an Aflin Store, you can return your product within 14 days after the store reopens. Some stores may be open for curbside pickup with limited support and are unable to complete returns at this time. If your local store has only curbside pickup available, you can return your product once the store has fully reopened. You can check your local store hours and status at aflin.com/retail.',
               'How can I return an order I bought online while under shelter-in-place orders?',
               'Start a return online at aflin.com/orderstatus, where you can create a return shipping label to ship your product from a drop off point or schedule a pickup at your location.',
               'Can I get Genius Support at an Aflin Store?',
               'The best way to get Genius Support is to make an appointment before visiting the store. Go to getsupport.aflin.com to schedule an appointment.',
               "What’s the status of my repair?",
               'You can check the status of a repair online at support.aflin.com/repair.',
               'Can I participate in a Today at Aflin session at an Aflin Store?',
               'We have temporarily paused Today at Aflin programming in our stores, but are excited to offer creative projects you can do at home with Today at Aflin at Home. Please visit aflin.com/today/feature/today-at-home.'
               'Will I be able to browse? Try the products? Go into the store?',
               "You can shop, browse, and try out products at Aflin Store locations that have fully reopened. We’re focused on limiting occupancy in every store, so you may experience short wait times before being allowed to enter.",
               "My local Aflin store has re-opened and I’ve placed an order to pick up in store. What safety measures can I expect when I arrive?",
               'To ensure a healthy environment, physical distancing measures may result in delayed store entry. Masks may be required to enter the store. And, your pick up will be no contact.',
               'Can I come by and pick up a product without going into an Aflin Store?',
               "Many of our stores have pickup in front of the store or curbside pickup available for online orders. When you place your order online you will see pickup options for stores near you. You may be required to choose a time window for picking up your order. We’ll email you detailed pickup instructions and send you a text and email when your order is ready. You can also check the status of your order in the Aflin Store App or at aflin.com/orderstatus",
               "I’ve heard that some Aflin Stores near me are now open. How do I know which stores I can visit?",
               'Some of our retail stores are now open. Please check aflin.com/retail for the latest on store re-openings, services available and operating hours.',
               'Will I have to wait in line?',
               'At Aflin Store locations that have fully reopened for shopping, you may experience short wait times before being allowed to enter the store. To maintain physical distancing, we are limiting store occupancy and giving everyone lots of room. Not all of our stores have resumed full operations. Please check the status of your nearest Aflin Store at aflin.com/retail.',
               'How is physical distancing practiced at Aflin Store locations?',
               'We have reduced the number of products on display in our stores so customers can shop and browse while maintaining a safe distance between themselves and others.Not all of our stores have resumed full operations. Please check the status of your nearest Aflin Store at aflin.com/retail.',
               'Will I have to wear a mask when I visit an Aflin Store?',
               "Face masks may be required for customers, depending on local mandates and conditions. Aflin follows local mandates. Masks will be provided to customers who don’t bring their own. N95 masks with valves, and masks that do not cover your nose and extend below your chin— such as bandanas, are not permitted at Aflin Stores. Replacement masks will be provided as needed.",
               'Will I have to provide proof of COVID-19 vaccination to visit an Aflin Store?',
               'Depending on local mandates and conditions, proof of COVID-19 vaccination may be required for entry. You can find more information about your nearest Aflin Store at aflin.com/retail.',
               'hey',
               'Hello! I am Hexa. Your personal assistant by Aflin Industries.',
               'hi',
               'Hello! I am Hexa. Your personal assistant by Aflin Industries.',
               'hello',
               'Hello! I am Hexa. Your personal assistant by Aflin Industries.',
               'Not satisfied',
               'Sorry for that. Kindly contact us through 932xxxxxxx'
])




Window.maximize()

class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    
    font_size = 17

class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    
    font_size = 17


class main(MDApp):

    def change_screen(self, name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Main.kv"))
        screen_manager.add_widget(Builder.load_file("Chats.kv"))
        return screen_manager

    def bot_name(self):
        screen_manager.current = "chats"

    def response(self, *args):
        response = chatbot.get_response(value)
        screen_manager.get_screen('chats').chat_list.add_widget(Response(text=response, size_hint_x=.75))

    def send(self):
        global size, halign, value
        if screen_manager.get_screen('chats').text_input != "":
            value = screen_manager.get_screen('chats').text_input.text
            if len(value) < 6:
                size = .22
                halign = "center"
            elif len(value) < 11:
                size = .32
                halign = "center"
            elif len(value) < 16:
                size = .45
                halign = "center"
            elif len(value) < 21:
                size = .58
                halign = "center"
            elif len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen_manager.get_screen('chats').chat_list.add_widget(
                Command(text=value, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response, 2)
            screen_manager.get_screen('chats').text_input.text = ""

if __name__ == '__main__':
    
    main().run()
