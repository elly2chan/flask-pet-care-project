from flask import render_template, make_response
from flask_restful import Resource


class GetAboutPage(Resource):
    def get(self):
        """
        Renders and returns the 'About' page.

        This endpoint serves the 'about.html' page, typically containing information
        about the application or organization.

        :return: rendered 'about.html' page
        """
        return make_response(render_template('about.html'))
