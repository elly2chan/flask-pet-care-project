from flask import render_template
from flask_restful import Resource


class GetAboutPage(Resource):
    """
    Endpoint for serving the 'About' page.

    This endpoint renders and returns the 'about.html' page, which typically contains
    information about the application, its purpose, or the organization behind it.
    """

    def get(self):
        """
        Renders the 'About' page.
        """
        return render_template('about.html')
