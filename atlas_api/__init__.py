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

from flask_restx import Api, Resource, fields
from config import ConfigClass

module_api = Api(version='1.0', title='Atlas API',
    description='Atlas API', doc='/v1/api-doc'
)

atlas_entity_ns = module_api.namespace('Atlas Entity Actions', description='Operation on Atlas Entity', path ='/')

from .entity_operation import EntityAction, EntityQueryBasic, EntityActionByGuid, EntityTagByGuid, EntityByGuidBulk
from .audit_operation import AuditAction
from .file_data_operations import FileDataOperations

######################################################### Entity API ###############################################
atlas_entity_ns.add_resource(EntityAction, '/v1/entity')
atlas_entity_ns.add_resource(EntityQueryBasic, '/v1/entity/basic')
atlas_entity_ns.add_resource(EntityByGuidBulk, '/v1/entity/guid/bulk')

atlas_entity_ns.add_resource(EntityActionByGuid, '/v1/entity/guid/<guid>')
atlas_entity_ns.add_resource(EntityTagByGuid, '/v1/entity/guid/<guid>/labels')

######################################################### Audit API ###############################################
atlas_entity_ns.add_resource(AuditAction, '/v1/entity/guid/<guid>/audit')

######################################################### File Meta API ############################################
atlas_entity_ns.add_resource(FileDataOperations, '/v2/filedata')