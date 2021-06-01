import time
import datetime


class WebPush:
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, main_page,
                 bulk_page, segment_page):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = datetime.datetime.now()
        self.end_date = datetime.datetime.now()
        self.language = language
        self.push_type = push_type
        self.main_page = main_page
        self.bulk_page = bulk_page
        self.segment_page = segment_page

    def send_push(self):
        print("Push gönderildi!")


class TriggerPush(WebPush):
    def __int__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                trigger_page):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page


class BulkPush(WebPush):
    def __int__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, send_data):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_data = send_data


class SegmentPush(WebPush):
    def __int__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                segment_name):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name


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
    "opt_in",
    "global",
    "start_date",
    "end_date",
    "Tr",
    "Trigger Push",
    "Main Page",
    "bulk",
    "segment",
)

bulk = BulkPush(
    "Web",
    True,
    "global",
    "",
    "",
    "Tr",
    "Recurrent push notifications",
    "Main Page",
    "bulk",
    "segment"
)

segment = SegmentPush(
    "Web",
    True,
    "global",
    "",
    "",
    "Tr",
    "Recurrent push notifications",
    "trigger",
    "bulk",
    "segment",
)

price_alert = PriceAlertPush(
    "Web",
    True,
    "global",
    "",
    "",
    "Tr",
    "Recurrent push notifications",
    "trigger",
    "bulk",
    "segment"
)
instock = InstockPush(
    "Web",
    True,
    "global",
    "",
    "",
    "Tr",
    "Recurrent push notifications",
    "trigger",
    "bulk",
    "segment"
)

trigger.send_push()
print("Push Type: {}".format(trigger.push_type))
print("Trigger Page: {}".format(trigger.main_page))
print("-----")
bulk.send_push()
print("Push Type: {}".format(bulk.push_type))
print("Bulk Page: {}".format(bulk.bulk_page))
print("-----")
segment.send_push()
print("Push Type: {}".format(segment.push_type))
print("Segment Page: {}".format(segment.main_page))
print("-----")
price_alert.discountPrice(10, 50)
print("-----")
instock.stockUpdate()
instock.send_push()
