from odoo import api, fields, models
from odoo.osv import expression
from datetime import datetime, timedelta

class UPTAPlanificacionCronologica(models.Model):
    _name = "upta.plan.cronologico"

    name = fields.Char(string='Nombre', compute='_compute_name')
    materias_id = fields.Many2one(comodel_name='upta.materias', string='Materia', help='Materia del Plan de Cronológico')
    trayectos_id = fields.Many2one(comodel_name='upta.trayectos', string='Trayecto', help='Trayecto del Plan de Cronológico')
    profesores_id = fields.Many2one(comodel_name='hr.employee', string='Profesor Encargado', help='Profesor que realiza el Plan de Cronológico')
    agno_id = fields.Many2one(comodel_name='upta.agno.academico', string='Año Académico', help='Año Académico del Plan de Cronológico')
    plan_act_id = fields.One2many(comodel_name='upta.plan.cronologico.actividades', inverse_name='plan_prof_id', string=' Actividades de Planificación')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")
    tray_mat = fields.Char(default='I', compute='_compute_tray_mat')

    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

    @api.model
    def _compute_name(self):
        for item in self:
            item.name = 'Plan Cronológico ' + item.materias_id.name + " " + item.trayectos_id.name  + " " + item.agno_id.name

    @api.onchange('trayectos_id')
    def _compute_tray_mat(self):
        for item in self:
            if item.trayectos_id != False:
                item.tray_mat = item.trayectos_id.name

class UPTAPlanificacionCronologicaActividades(models.Model):
    _name = "upta.plan.cronologico.actividades"

    semana = fields.Integer(string='Semana', help='Semana de la Actividad')
    saberes_id = fields.Many2one(comodel_name='upta.plan.cronologico.saberes', string='Saberes', help='Saberes de la Actividad')
    estrategias_id = fields.Many2one(comodel_name='upta.plan.cronologico.estrategias', string='Estrategias de Enseñanza - Aprendizaje', help='Estrategias de la Actividad')
    plan_prof_id = fields.Many2one(comodel_name='upta.plan.cronologico', string='Planificación Profesor')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

class UPTAPlanificacionCronologicaSaberes(models.Model):
    _name = 'upta.plan.cronologico.saberes'

    name = fields.Text(string='Descripción', help='Descripción del saber que se está registrando')
    plan_id = fields.One2many(comodel_name='upta.plan.cronologico.actividades', inverse_name='saberes_id', string=' Actividades de Planificación')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

class UPTAPlanificacionCronologicaEstrategias(models.Model):
    _name = 'upta.plan.cronologico.estrategias'

    name = fields.Text(string='Descripción', help='Descripción de la estrategia que se está registrando')
    plan_id = fields.One2many(comodel_name='upta.plan.cronologico.actividades', inverse_name='estrategias_id', string=' Actividades de Planificación')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

