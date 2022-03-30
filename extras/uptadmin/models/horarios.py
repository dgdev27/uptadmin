from odoo import api, fields, models
from datetime import datetime, timedelta

class UPTAHorarios(models.Model):
    _name = 'upta.horarios'
    _description = 'Horarios de la UPT Aragua'

    name = fields.Char(string='Nombre', compute="_compute_nombre")
    secciones_id = fields.Many2one('upta.secciones', string='Sección', help='Sección a la cual se le está asignando el horario')
    carreras_id = fields.Many2one(comodel_name='upta.carreras', string='Carrera', help='Carrera a la que pertenece la sección del horario')
    mallas_id = fields.Many2one(comodel_name='upta.mallas', string='Mallas', help='Malla a la que pertenece la sección del horario')
    trayectos_id = fields.Many2one(comodel_name='upta.trayectos', string='Trayecto', help='Trayecto a la que pertenece la sección del horario')
    fases_id = fields.Many2one(comodel_name='upta.fases', string='Fase', help='Fase actual para el horario')
    clases_id = fields.One2many(comodel_name='upta.horarios.clases', inverse_name='horarios_id', string=' Clases', help='Clases asignadas')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

    @api.onchange('secciones_id')
    def _compute_secciones(self):
        for item in self:
            if item.secciones_id:
                item.carreras_id = item.secciones_id.carreras_id.id
                item.mallas_id = item.secciones_id.mallas_id.id
                item.trayectos_id = item.secciones_id.trayectos_id.id

    @api.model
    def _compute_nombre(self):
        for item in self:  
            if item.secciones_id:
                nombre = "Horario " + item.secciones_id.carreras_id.name
                nombre += " " + item.secciones_id.trayectos_id.name
                nombre += " Sección " + str(item.secciones_id.seccion)
                item.name = nombre            

class UPTAHorariosClases(models.Model):
    _name = 'upta.horarios.clases'

    dias = fields.Selection(string='Día', selection=[('lunes', 'Lunes'), ('martes', 'martes'), ('miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes')], help='Día en el cual se está asignando la clase')
    hora_ini = fields.Many2one(comodel_name='upta.horarios.horas', string='Hora de Inicio', help='Hora de inicio en la cual se está asignando la clase')
    hora_fin = fields.Many2one(comodel_name='upta.horarios.horas', string='Hora Final', help='Hora de finalización en la cual se termina la clase')
    duration = fields.Integer(string='Horas Académicas', compute='_compute_duration', help='Cantidad de horas que dura la clase')
    materias_id = fields.Many2one('upta.materias', string='Materia', help='Materia que se está asignando a la clase')
    profesores_id = fields.Many2one('hr.employee', string='Profesor', help='Profesor que se está asignando a la clase')
    espacios_id = fields.Many2one('upta.espacios', string='Espacio', help='Espacio que se está asignando a la clase')
    horarios_id = fields.Many2one(comodel_name='upta.horarios', string='Horario')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")
    minimo = fields.Integer(string='', default=1)
    
    @api.onchange('hora_ini')
    def _onchange_hora_fin(self):
        for item in self:
            if item.hora_ini:
                item.minimo = item.hora_ini.valor
                item.hora_fin = ''

    @api.model
    def _compute_duration(self):
        for item in self:
            if item.hora_ini and item.hora_fin:
                cantidad = item.hora_fin.valor - item.hora_ini.valor
                item.duration = cantidad
            else:
                item.duration = 0
    

class UPTAHorariosHoras(models.Model):
    _name = 'upta.horarios.horas'

    name = fields.Char(string='Nombre', help='Identificador de la hora de clase')
    valor = fields.Integer(string='Valor', help='Valor que define el orden de las horas de clase')
    tipo = fields.Selection(string='Tipo de hora', selection=[('entrada', 'Entrada'), ('salida', 'Salida')], help='Tipo de hora de clase')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

