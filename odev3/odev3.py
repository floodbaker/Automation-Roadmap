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
        self.send_date = send_date


class SegmentPush(WebPush):
    def __int__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                segment_name):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name


class PriceAlertPush(WebPush):
    def __int__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                price_info, discount_rate):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.price_info = price_info
        self.discount_rate = discount_rate

    def discountPrice(self, price_info, discount_rate):
        discount_price = price_info - (price_info / discount_rate)
        return discount_price


class InstockPush(WebPush):
    def __int__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, stock_info):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

    def stockUpdate(self, stock_info):
        if stock_info == True:
            self.stock_info = False
        else:
            self.stock_info = True


trigger = TriggerPush("Windows", "opt_in", "global", "start_date", "end_date", "TR", "Trigger Push", "Main Page",
                      "Bulk", "Segment")
print("Push Type: {}".format(trigger.push_type))
print("Trigger Page: {}".format(trigger.main_page))

bulk = BulkPush("Web", True, "global", "", "", "Tr", "Bulk push notifications", "Main Page", "bulk", "segment")
print("Push Type: {}".format(bulk.push_type))
print("Bulk Page: {}".format(bulk.bulk_page))
segment = SegmentPush("Web", True, "global", "", "", "Tr", "Segment push notifications", "trigger", "bulk", "segment")

print("Push Type: {}".format(segment.push_type))
print("Segment Page: {}".format(segment.main_page))

price_alert = PriceAlertPush("Web", True, "global", "", "", "Tr", "Price Alert push notifications", "trigger", "bulk",
                             "segment")
print("Push Type: {}".format(price_alert.push_type))
print("Segment Page: {}".format(price_alert.discountPrice(1000, 20)))

instock = InstockPush("Web", True, "global", "", "", "Tr", "Instock push notifications", "trigger", "bulk", "segment")
print("Push Type: {}".format(instock.push_type))
print("Segment Page: {}".format(instock.stockUpdate(True)))
