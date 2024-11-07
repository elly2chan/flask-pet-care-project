from flask import render_template, make_response
from flask_restful import Resource


class GetDocumentationPage(Resource):
    def get(self):
        """
        Renders and returns the 'Documentation' page.

        This endpoint serves the 'documentation.html' page that contains the API documentation for the project.

        :return: rendered 'documentation.html' page
        """
        return make_response(render_template('documentation.html'))
