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
    segment_name = "asdsad"


class PriceAlertPush(WebPush):
    price_info = 0
    discount_rate = 0.0

    def discountPrice(self, price_info, discount_rate):
        self.price_info = price_info
        self.discount_rate = discount_rate

        return (self.price_info * self.discount_rate) / 100


class InstockPush(WebPush):
    stock_info = True

    def stockUpdate(self):
        self.stock_info = not self.stock_info


test = SegmentPush(
    "Web",
    True,
    "global",
    "",
    "",
    "Tr",
    "Recurrent push notifications",
)


test.send_push()
