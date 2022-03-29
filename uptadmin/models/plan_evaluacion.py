from odoo import api, fields, models
from odoo.osv import expression
from datetime import datetime, timedelta

class UPTAPlanEvaluacion(models.Model):
    _name = 'upta.plan.evaluacion'
    _description = 'Planes de Evaluación de la UPT Aragua'

    name = fields.Char(string='Nombre', compute="_compute_name")
    profesores_id = fields.Many2one(comodel_name='hr.employee', string='Profesor', default= lambda self: self.env.user.employee_ids, help='Profesor que realiza el Plan de Evaluación')
    materias_id = fields.Many2one(comodel_name='upta.materias', string='Materia', help='Materia para el Plan de Evaluación')
    trayectos_id = fields.Many2one(comodel_name='upta.trayectos', string='Trayecto', help='Trayecto del Plan de Evaluación')
    fases_id = fields.Many2one(comodel_name='upta.fases', string='Fase', help='Fase del Plan de Evaluación')
    periodos_id = fields.Many2one(comodel_name='upta.agno.academico', string='Periodo', help='Periodo del Plan de Evaluación')
    fecha = fields.Date(string='Fecha',default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
    actividades_id = fields.One2many(comodel_name='upta.plan.evaluacion.actividades', inverse_name='evaluaciones_id', string=' Actividades')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")
    
    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

    @api.model
    def _compute_name(self):
        for item in self:
            nombre = 'Plan de Evaluación ' + item.materias_id.name + " Trayecto " + item.trayectos_id.identificador  + " " + item.periodos_id.name
            item.name = nombre

class UPTAPlanEvaluacionActividades(models.Model):
    _name = 'upta.plan.evaluacion.actividades'
    _description = 'Planes de Evaluación de la UPT Aragua'

    objetivos_id = fields.Many2one(comodel_name='upta.plan.evaluacion.objetivos', string='Objetivos de Aprendizaje', help='Objetivos de la Actividad')
    metas_id = fields.Many2one(comodel_name='upta.plan.evaluacion.metas', string='Metas', help='Metas de la Actividad')
    condiciones_id = fields.Many2one(comodel_name='upta.plan.evaluacion.condiciones', string='Condiciones para el Desarrollo del Aprendizaje', help='Condiciones de la Actividad')
    instrumentos_id = fields.Many2one(comodel_name='upta.plan.evaluacion.instrumentos', string='Instrumentos o Técnicas de Evaluación', help='Instrumentos de la Actividad')
    ponderaciones = fields.Float(string='Ponderación', default='1', help='Ponderación de la Actividad', size=10)
    semanas = fields.Integer(string='Semanas', default='1', help='Semana de la Actividad', size=10)
    evaluaciones_id = fields.Many2one(comodel_name='upta.plan.evaluacion', string='Plan de Evaluación')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")
    
    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

class UPTAPlanEvaluacionObjetivos(models.Model):
    _name = 'upta.plan.evaluacion.objetivos'
    _description = 'Objetivos de los Planes de Evaluación de la UPT Aragua'

    name = fields.Text(string='Descripción', help='Descripción de los Objetivos', size=100)
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")
    
    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

class UPTAPlanEvaluacionInstrumentos(models.Model):
    _name = 'upta.plan.evaluacion.instrumentos'
    _description = 'Instrumentos o Técnicas de Evaluación de los Planes de Evaluación de la UPT Aragua'

    name = fields.Text(string='Descripción', help='Descripción de los Instrumentos', size=100)
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")
    
    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

class UPTAPlanEvaluacionMetas(models.Model):
    _name = 'upta.plan.evaluacion.metas'
    _description = 'Metas de los Planes de Evaluación de la UPT Aragua'

    name = fields.Text(string='Descripción', help='Descripción de las Metas', size=100)
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")
    
    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

class UPTAPlanEvaluacionCondiciones(models.Model):
    _name = 'upta.plan.evaluacion.condiciones'
    _description = 'Condiciones para el Desarrollo del Aprendizaje de los Planes de Evaluación de la UPT Aragua'

    name = fields.Text(string='Descripción', help='Descripción de Condiciones', size=100)
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")
    
    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'


