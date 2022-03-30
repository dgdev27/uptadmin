from odoo import api, fields, models
from datetime import datetime, timedelta

class UPTADepartamentos(models.Model):
    _inherit = 'hr.department'

    edificios_id = fields.Many2one('upta.espacios.edificios', string='Edificio')
  
class UPTAEmpleados(models.Model):
    _inherit = 'hr.employee'
        
    nacionalidad = fields.Selection(string='Nacionalidad', selection=[('venezolano', 'Venezolano'), ('extranjero', 'Extranjero')])
    
    profesiones_id = fields.Many2one('upta.empleados.profesiones', string='Profesión')
    certificado_id = fields.Many2one('upta.empleados.certificado', string='Nivel de certificado')
    estudios_id = fields.Many2one('upta.empleados.estudios', string='Campo de estudio')
    institutos_id = fields.Many2one('upta.empleados.institutos', string='Instituto')

    @api.onchange('job_id')
    def onchange_job(self):
        self.job_title = self.job_id.name 

class UPTAEmpleadosProfesiones(models.Model):
    _name = 'upta.empleados.profesiones'
    _description = 'Profesiones de los Trabajadores de la UPT Aragua'

    name = fields.Char(string='Nombre')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

class UPTAEmpleadosCertificado(models.Model):
    _name = 'upta.empleados.certificado'
    _description = 'Nivel de certificado de los Trabajadores de la UPT Aragua'

    name = fields.Char(string='Nombre')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

class UPTAEmpleadosEstudios(models.Model):
    _name = 'upta.empleados.estudios'
    _description = 'Campo de Estudios de los Trabajadores de la UPT Aragua'

    name = fields.Char(string='Nombre')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

class UPTAEmpleadosInstitutos(models.Model):
    _name = 'upta.empleados.institutos'
    _description = 'Institutos de los Trabajadores de la UPT Aragua'

    name = fields.Char(string='Nombre')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

    