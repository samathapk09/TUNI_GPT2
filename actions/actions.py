# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet

# class ActionStoreProductInfo(Action):

#     def name(self) -> Text:
#         return "action_store_product_info"

#     async def run(self, dispatcher: CollectingDispatcher,
#                   tracker: Tracker,
#                   domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         product_id = next(tracker.get_latest_entity_values("product_id"), None)
#         product_name = next(tracker.get_latest_entity_values("product_name"), None)
#         product_price = next(tracker.get_latest_entity_values("product_price"), None)

#         return [SlotSet("product_id", product_id),
#                 SlotSet("product_name", product_name),
#                 SlotSet("product_price", product_price)]




# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet

# class ActionStoreProductInfo(Action):
#     def name(self) -> str:
#         return "action_store_product_info"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
#         product_info = {
#             'pid': '1720074722477',
#             'link': 'https://firebasestorage.googleapis.com/v0/b/tunitest-e022d.appspot.com/o/product_images%2F_1720074722477?alt=media&token=c1931d80-29ab-4d2f-a325-7303de97b00d'
#         }

#         # Set slot values
#         return [
#             SlotSet("pid", product_info['pid']),
#             SlotSet("link", product_info['link']),
#             # Optionally: send response to the user here if desired
#         ]
