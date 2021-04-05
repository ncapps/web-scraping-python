import scrapy


def authentication_failed(response):
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
    pass


class LoginSpider(scrapy.Spider):
    name = 'app.courtreserve.com'
    start_urls = ['https://app.courtreserve.com/Online/Account/LogIn/6801']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formid='loginForm',
            formdata={'UserNameOrEmail': '',
                      'Password': ''},
            clickdata={'type': 'button', 'onclick': 'submitLoginForm()'},
            callback=self.after_login
        )

    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error("Login failed")
            return
