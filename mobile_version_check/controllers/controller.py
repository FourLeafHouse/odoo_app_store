import requests
import re
from odoo import http
from odoo.http import request


class Controller(http.Controller):

    @http.route('/api/version-check', type='json', auth='public', methods=['POST'], csrf=False)
    def mobile_app_version_check(self, **kw):
        platform = kw.get('platform')
        data = { 'isSuccess': True,'message': 'Success'}
        package_name_android = request.env['ir.config_parameter'].sudo().get_param('android_package_name')
        package_name_ios = request.env['ir.config_parameter'].sudo().get_param('ios_package_name')
        if package_name_android == False or package_name_ios == False:
            return {
                'isSuccess': False,
                'message': "Error: Android or iOS package name not configured"
            }

        try:
            if platform == 'android':
                url = f"https://play.google.com/store/apps/details?id={package_name_android}&hl=en"
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
                }

                response = requests.get(url, headers=headers)
                match = re.search(r'\[\[\["([0-9]+(?:\.[0-9]+)+)"\]\]', response.text)
                if match:
                    data.update({
                        'storeVersion': match.group(1),
                        'storeUrl': url,
                        'packageName': package_name_android

                    })
                else:
                    raise ValueError("Version not found in Android store page")

            elif platform == 'ios':
                url = f'https://itunes.apple.com/lookup?bundleId={package_name_ios}&country=us'
                response = requests.get(url)

                if response.status_code == 200 and response.json()['results']:
                    result = response.json()['results'][0]
                    data.update({
                        'storeVersion': result.get('version'),
                        'storeUrl': result.get('trackViewUrl'),
                        'packageName': package_name_ios
                    })
                else:
                    raise ValueError("Version not found in iOS store response")

            else:
                raise ValueError("Unsupported platform")

        except Exception as e:
            data.update({
                'isSuccess': False,
                'message': f"Error: {str(e)}"
            })

        return data
