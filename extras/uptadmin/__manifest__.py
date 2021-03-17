# -*- coding: utf-8 -*-

{
    'name': 'UPTAdmin',
    'version': '1.0',
    'summary': 'Sistema de Gestión Académico de la UPT Aragua La victoria',
    'category': 'extras',
    'author': 'T.S.U. Oliver Di Gregorio',
    'maintainer': 'T.S.U. Oliver Di Gregorio',
    'license': 'AGPL-3',
    'depends': ['base', 'hr', 'website', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/upta_carreras.xml',
        'views/upta_mallas.xml',
        'views/upta_trayectos.xml',
        'views/upta_fases.xml',
        'views/upta_materias.xml',
        'views/upta_espacios.xml',
        'views/upta_empleados.xml',
        'views/upta_departamentos.xml',
        'views/upta_secciones.xml',
        'views/upta_horarios.xml',
        'views/upta_config.xml',
        'views/upta_plan_evaluacion.xml',
        'views/upta_plan_cronologico.xml',
        'report/upta_report_template.xml',
        'report/horarios_report.xml',
        'report/plan_evaluacion_report.xml',
        'report/plan_cronologico_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
