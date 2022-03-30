# -*- coding: utf-8 -*-

{
    'name': 'UPTAdmin Empleados',
    'version': '13.0',
    'summary': 'Extensión de Funcionalidades en Empleados del Sistema de Gestión Académico de la UPT Aragua La victoria',
    'category': 'extras',
    'author': 'T.S.U. Oliver Di Gregorio',
    'maintainer': 'T.S.U. Oliver Di Gregorio',
    'license': 'AGPL-3',
    'depends': ['base', 'hr', 'uptadmin'],
    'data': [
        'security/ir.model.access.csv',
        'views/upta_empleados.xml',
        'views/upta_departamentos.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
