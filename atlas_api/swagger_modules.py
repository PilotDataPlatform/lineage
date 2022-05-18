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

from flask_restx import fields

from . import module_api

entity_attribute = module_api.model('entity_attribute', {
    # only samples
    'owner': fields.String(readOnly=True, description='Who owns the entity'),
    'qualifiedName': fields.String(readOnly=True, description='Name of the entity'),
    'path': fields.String(readOnly=True, description='In nfs, the path of the file'),
    'name': fields.String(readOnly=True, description='Name of the entity'),
    'updateBy': fields.String(readOnly=True, description='Who updated the entity last time'),

    # other options
    'other_property': fields.String(readOnly=True, description='Other entities')

})

entity = module_api.model('entity', {
    'typeName': fields.String(readOnly=True, description='The metadata type of entity'),
    'attributes': fields.Nested(entity_attribute, readOnly=True, description='Attribute that entity has'),
    'isIncomplete': fields.Boolean(readOnly=True, description='Is entity completed'),
    'status': fields.String(readOnly=True, description='Active/Inactive'),
    'createdBy': fields.String(readOnly=True, description='Who create the entity'),
    'version': fields.Integer(readOnly=True, description='Version number'),
})

create_update_entity = module_api.model('create_update_entity', {
    'entity': fields.Nested(entity, readOnly=True, description='entity description')
})
