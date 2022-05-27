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

import time

import requests

from config import ConfigClass
from models.meta_class import MetaService
from services.logger_services.logger_factory_service import SrvLoggerFactory


class SrvFileDataMgr(metaclass=MetaService):
    _logger = SrvLoggerFactory('api_file_data').get_logger()

    def __init__(self):
        self.base_url = ConfigClass.ATLAS_API
        self.entity_endpoint = 'api/atlas/v2/entity'
        self.search_endpoint = 'api/atlas/v2/search/attribute'
        self.entity_uniquename_endpoint = 'api/atlas/v2/entity/uniqueAttribute/type/{}?attr:qualifiedName={}'
        self.entity_type = 'file_data'

    def create(self, geid, uploader, path, file_name, file_size,
               description, namespace, project_code, project_name,
               labels, guid=None):
        """create data entity or update in Atlas."""
        headers = {'content-type': 'application/json'}

        attrs = {
            'global_entity_id': geid,
            'name': geid,
            'file_name': file_name,
            'path': path,
            'qualifiedName': geid,
            'full_path': geid,  # full path requires unique
            'file_size': file_size,
            'archived': False,
            'description': description,
            'owner': uploader,
            'time_created': time.time(),
            'time_lastmodified': time.time(),
            'namespace': namespace,
            'project_code': project_code,
            'bucketName': project_code,
            #
            'createTime': time.time(),
            'modifiedTime': 0,
            'replicatedTo': None,
            'userDescription': None,
            'isFile': False,
            'numberOfReplicas': 0,
            'replicatedFrom': None,
            'displayName': None,
            'extendedAttributes': None,
            'nameServiceId': None,
            'posixPermissions': None,
            'clusterName': None,
            'isSymlink': False,
            'group': None,
        }
        if project_name:
            attrs['project_name'] = project_name

        atlas_post_form_json = {
            'referredEntities': {},
            'entity': {
                'typeName': self.entity_type,
                'attributes': attrs,
                'isIncomplete': False,
                'status': 'ACTIVE',
                'createdBy': uploader,
                'version': 0,
                'relationshipAttributes': {
                    'schema': [],
                    'inputToProcesses': [],
                    'meanings': [],
                    'outputFromProcesses': []
                },
                'customAttributes': {},
                'labels': labels
            }
        }
        if guid:
            atlas_post_form_json['entity']['guid'] = guid

        res = requests.post(self.base_url + self.entity_endpoint,
                            verify=False, json=atlas_post_form_json,
                            auth=requests.auth.HTTPBasicAuth(ConfigClass.ATLAS_ADMIN,
                                                             ConfigClass.ATLAS_PASSWD),
                            headers=headers
                            )
        return res
