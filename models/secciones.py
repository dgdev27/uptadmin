from odoo import api, fields, models
from odoo.osv import expression
from datetime import datetime, timedelta

class UPTASecciones(models.Model):
    _name = 'upta.secciones'
    _description = 'Secciones de la UPT Aragua'

    name = fields.Char(string='Nombre', compute='_compute_name')
    seccion = fields.Integer(string='Nº de la Sección', default=1, help='Inserte el número identificador de la sección')
    carreras_id = fields.Many2one('upta.carreras',string='Carrera', help='Carrera a la que pertenece la sección')
    mallas_id = fields.Many2one('upta.mallas',string='Malla', help='Malla a la que pertenece la sección')
    trayectos_id = fields.Many2one('upta.trayectos',string='Trayecto', help='Trayecto al que pertenece la sección')
    materias_id = fields.Many2many('upta.materias',string='Materias', help='Materias con las que cuenta la sección')
    agno_id = fields.Many2many(comodel_name='upta.agno.academico', string='Años Académicos', help='Años académicos en los que ha estado presente la sección')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

    def _compute_name(self):
        for item in self:
            nombre = 'Sección ' + str(item.seccion) + ' ' + item.carreras_id.name + ' ' + item.trayectos_id.name
            item.name = nombre

class UPTAAgnoAcademico(models.Model):
    _name = 'upta.agno.academico'
    _description = 'Años académicos de la UPT Aragua'

    name = fields.Char(string='Nombre', help='Inserte el nombre del año académico a registrar')
    fecha_ini = fields.Date(string='Fecha de Inicio', help='Fecha de inicio del año académico')
    fecha_fin = fields.Date(string='Fecha Final', help='Fecha de Finalización del año académico')
    secciones_id = fields.Many2many(comodel_name='upta.secciones', string='Sección', help='Secciones con las que cuenta el año académico')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")
    
    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'
