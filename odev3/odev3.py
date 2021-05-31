import time
import datetime


class WebPush:
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = datetime.datetime.now()
        self.end_date = datetime.datetime.now()
        self.language = language
        self.push_type = push_type

    def send_push(self):
        print("Push gönderildi!")


class TriggerPush(WebPush):
    trigger_page = ""


class BulkPush(WebPush):
    send_data = ""


class SegmentPush(WebPush):
    segment_name = ""


class PriceAlertPush(WebPush):
    def discountPrice(self, price_info, discount_rate):
        self.price_info = price_info
        self.discount_rate = discount_rate

        result = (self.price_info * self.discount_rate) / 100
        print(result)
        return result


class InstockPush(WebPush):
    stock_info = False

    def stockUpdate(self):
        self.stock_info = not self.stock_info
        print(self.stock_info)


trigger = TriggerPush(
    "Web",
    True,
    "global",
    "",
    "",
    "Tr",
    "Recurrent push notifications",
)
bulk = BulkPush(
    "Web",
    True,
    "global",
    "",
    "",
    "Tr",
    "Recurrent push notifications",
)
segment = SegmentPush(
    "Web",
    True,
    "global",
    "",
    "",
    "Tr",
    "Recurrent push notifications",
)
price_alert = PriceAlertPush(
    "Web",
    True,
    "global",
    "",
    "",
    "Tr",
    "Recurrent push notifications",
)
instock = InstockPush(
    "Web",
    True,
    "global",
    "",
    "",
    "Tr",
    "Recurrent push notifications",
)


trigger.send_push()
bulk.send_push()
segment.send_push()
price_alert.discountPrice(10, 50)
instock.stockUpdate()
instock.send_push()


