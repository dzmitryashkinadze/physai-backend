from flask_restful import Resource


class SesDestination:
    """Contains data about an email destination."""

    def __init__(self, tos, ccs=None, bccs=None):
        """
        :param tos: The list of recipients on the 'To:' line.
        :param ccs: The list of recipients on the 'CC:' line.
        :param bccs: The list of recipients on the 'BCC:' line.
        """
        self.tos = tos
        self.ccs = ccs
        self.bccs = bccs

    def to_service_format(self):
        """
        :return: The destination data in the format expected by Amazon SES.
        """
        svc_format = {'ToAddresses': self.tos}
        if self.ccs is not None:
            svc_format['CcAddresses'] = self.ccs
        if self.bccs is not None:
            svc_format['BccAddresses'] = self.bccs
        return svc_format


class Email(Resource):
    def __init__(self, ses_client):
        self.ses_client = ses_client

    def get(self):
        destination = SesDestination(tos=['dzmitry.ashkinadze@gmail.com'])
        # sending email with all details with amzon ses
        send_args = {
            'Source': 'info@physai.org',
            'Destination': destination.to_service_format(),
            'Template': 'CONFIRM_EMAIL',
            'TemplateData': '{ \"REPLACEMENT_TAG_NAME\":\"REPLACEMENT_VALUE\" }'}
        try:
            response = self.ses_client.send_templated_email(**send_args)
            message_id = response['MessageId']
            # logger.info(
            #    "Sent mail %s from %s to %s.", message_id, source, destination.tos)
        except Exception:
            # logger.exception(
            #    "Couldn't send mail from %s to %s.", source, destination.tos)
            raise
        else:
            return message_id, 401
