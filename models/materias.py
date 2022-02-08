from odoo import api, fields, models
from odoo.osv import expression
from datetime import datetime, timedelta

class UPTAMaterias(models.Model):
    _name = 'upta.materias'
    _description = 'Materias de la UPT Aragua'

    name = fields.Char(string='Nombre', help='Inserte el nombre de la materia a registrar', size=30)
    codigo = fields.Char(string='Código', help='Inserte el código de la materia a registrar')
    mallas_id = fields.Many2one(comodel_name='upta.mallas', string='Malla', help='Malla a la que está asignada la materia')
    trayecto_id = fields.Many2one(comodel_name='upta.trayectos', string='Trayecto', help='Trayecto al que está asignada la materia')
    seccion_id = fields.Many2many(comodel_name='upta.secciones', string='Secciones', help='Sección a la que está asignada la materia')
    fases_id = fields.Many2one(comodel_name='upta.fases', string='Fase', help='Fase a la que está asignada la materia')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'
