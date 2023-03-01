# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionRequest(Action):

    def name(self) -> Text:
        return "action_request"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # extract necessary entities from user input
        leave_type = tracker.get_slot("leave_type")
        start_date = tracker.get_slot("start_date")
        end_date = tracker.get_slot("end_date")

        # send request to HRIS system
        # replace this with your own code to interact with your HRIS system
        response = requests.post(url="http://hris-system.com/leave_request",
                                 data={
                                       "leave_type": leave_type,
                                       "start_date": start_date,
                                       "end_date": end_date
                                    })
        
        # send response message to user
        message = "Your {} leave request from {} to {} has been submitted.".format(leave_type, start_date, end_date)
        dispatcher.utter_message(text=message)

        return []

class ActionClaim(Action):

    def name(self) -> Text:
        return "action_claim"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # extract necessary entities from user input
        claim_type = tracker.get_slot("claim_type")
        amount = tracker.get_slot("amount")

        # send request to HRIS system
        # replace this with your own code to interact with your HRIS system
        response = requests.post(url="http://hris-system.com/claim_request",
                                 data={
                                       "claim_type": claim_type,
                                       "amount": amount
                                    })

        # send response message to user
        message = "Your {} claim request of {} has been submitted.".format(claim_type, amount)
        dispatcher.utter_message(text=message)

        return []

class ActionAnalytics(Action):

    def name(self) -> Text:
        return "action_analytics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # get the necessary data from HRIS system
        # replace this with your own code to interact with your HRIS system
        data = requests.get(url="http://hris-system.com/analytics")

        # generate analytics report
        # replace this with your own code to generate the analytics report
        report = "Here is your analytics report: {}".format(data)

        # send response message to user
        dispatcher.utter_message(text=report)

        return []
