import json
import requests


class ImageBBStorage():

    def save(self, image_name, image):
        '''

        '''
        url = "https://api.imgbb.com/1/upload?key=13ca89c0545a9cef342bb94a3cc7fd8b&expiration=1200"
        payload = {}
        files = [('image', (image_name, image, 'image/jpeg'))]
        headers = {}
        response = requests.request(
            "POST",
            url,
            headers=headers,
            data=payload,
            files=files)

        json_response = json.loads(response.text)['data']['url']
        return json_response
