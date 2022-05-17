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

from app import create_app



app = create_app()
app.config['TESTING'] = True
app.config['DEBUG'] = True
test_client = app.test_client()


class SetUpTest:

    def __init__(self, log, test_app):
        self.log = log
        self.app = test_app

    def create_entity(self, payload):
        self.log.info(f"PREPARING TEST: START CREATING ENTITY")
        self.log.info(f"POST DATA: {payload}")
        res = self.app.post("/v1/entity", json=payload)
        self.log.info(f"RESPONSE DATA: {res.data}")
        self.log.info(F"RESPONSE STATUS: {res.status_code}")
        assert res.status_code == 200
        self.log.info(f"TESTING ENTITY CREATED")
        guid_res = res.json['result']
        guid_res = guid_res['mutatedEntities']['CREATE']
        guid = guid_res[0]['guid']
        self.log.info(f"SETUP GUID: {guid}")
        return guid

    def delete_entity(self, guid):
        self.log.info("Delete the testing entity".center(50, '='))
        self.log.warning(f"DELETING TESTING NODE: {guid}")
        res = self.app.delete('/v1/entity/guid/' + str(guid))
        self.log.info(f"DELETING STATUS: {res.status_code}")
        assert res.status_code == 200
        self.log.info(f"DELETING RESPONSE: {res.data}")
