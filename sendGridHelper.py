from sendgrid import Mail, SendGridAPIClient
from const import Const

class SendGridHelper:

    def send_email(self, df):
        receiver_email = Const.RECIEVING_EMAIL
        subject_email = 'Revenue stats - CB'
        html_table = df.to_html()

        email_body = ''' Stats for chaturbate revenueb  
        {}
        '''.format(html_table)

        message = Mail(
            from_email='CB_Rev@testemail.com',
            to_emails=receiver_email,
            subject=subject_email,
            html_content=email_body)

        try:
            sg = SendGridAPIClient(Const.SEND_GRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)

        except Exception as e:
            print(e.message)