# Copyright (C) 2022 Indoc Research
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests
from flask import request
from flask_restx import Resource
from requests.auth import HTTPBasicAuth

from app import app
from config import ConfigClass


class AuditAction(Resource):
    def get(self, guid):

        """Get the audit log from entity by guid."""
        count = request.args.get('count', 25)
        app.logger.info('Recieving the parameter: count %s, guid %s', count, guid)

        try:
            headers = {'content-type': 'application/json'}
            res = requests.get(ConfigClass.ATLAS_API + 'api/atlas/v2/entity/%s/audit?count=%d' % (guid, int(count)),
                               verify=False, headers=headers,
                               auth=HTTPBasicAuth(ConfigClass.ATLAS_ADMIN, ConfigClass.ATLAS_PASSWD)
                               )

            # log it if not 200 level response
            if res.status_code >= 300:
                app.logger.error('Error in response: %s', res.text)
                return {'result': res.text}, res.status_code
        except Exception as e:
            app.logger.error('Error in get the audit log: %s', str(e))
            return {'result': str(e)}, 403

        return {'result': res.json()}, res.status_code
