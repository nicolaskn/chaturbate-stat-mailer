import requests
import json
import pandas as pd
from sendGridHelper import SendGridHelper
from const import Const

class ChaturbateStatMailer:
    def __init__(self):
        self.emailer = SendGridHelper()
        self.username = Const.CB_USERNAME
        self.token = Const.CB_TOKEN
        self.url = 'https://chaturbate.com/affiliates/apistats/?username={}&token={}'.format(self.username, self.token)

    def get_stat(self):
        '''Retrieve the stats'''
        try:
            r = requests.get(self.url)
            response = json.loads(r.text)
            summary_data_dict =  response['stats'][0]['totals']
            daily_metric_df = pd.DataFrame.from_dict(summary_data_dict, orient='index', columns=[''])
            self.send_email(daily_metric_df)
        except:
            print('Retrieving stats failed')

    def send_email(self, df):
        try:
            self.emailer.send_email(df)
        except Exception as e:
            print('Failure trying to send email. {}'.format(e))

if __name__ == '__main__':
    cb = ChaturbateStatMailer()
    cb.get_stat()
