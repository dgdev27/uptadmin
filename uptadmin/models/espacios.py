from odoo import api, fields, models
from odoo.osv import expression
from datetime import datetime, timedelta

class UPTAEspacios(models.Model):
    _name = 'upta.espacios'
    _description = 'Espacios de estudio de la UPT Aragua'

    name = fields.Char(string='Nombre', help='Inserte el nombre del espacio a registrar', size=10)
    tipos_id = fields.Many2one(comodel_name='upta.espacios.tipos', string='Tipo de Espacio', help='Tipo de espacio (Aula/Laboratorio)')
    pc_num = fields.Integer(string='N° de Computadoras Funcionales', help='Inserte el número de computadoras que se encuentren operativas', size=2)
    edificios_id = fields.Many2one(comodel_name='upta.espacios.edificios', string='Edificio', help='Edificio al cual pertenece el espacio', )
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")
    
    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

class UPTAEspaciosTipos(models.Model):
    _name = 'upta.espacios.tipos'
    _description = 'Tipos de Espacios de estudio de la UPT Aragua'

    name = fields.Char(string='Nombre', help='Inserte el nombre del tipo de espacio a registrar', size=10)
    espacios_id = fields.One2many(comodel_name='upta.espacios', inverse_name='tipos_id', string=' Espacios')    
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

class UPTAEspaciosEdificios(models.Model):
    _name = 'upta.espacios.edificios'
    _description = 'Edificios de los Espacios de estudio de la UPT Aragua'

    name = fields.Char(string='Nombre', help='Inserte el nombre del edificio a registrar', size=10)
    espacios_id = fields.One2many(comodel_name='upta.espacios', inverse_name='edificios_id', string=' Espacios')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")
    
    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'
