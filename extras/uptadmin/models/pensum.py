# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import datetime, timedelta

class UPTACarreras(models.Model):
    _name = 'upta.carreras'
    _description = 'Carreras de la UPT Aragua'

    name = fields.Char(string='Nombre', help='Inserte el nombre de la carrera a registrar', size=30)
    mallas_id = fields.One2many(comodel_name='upta.mallas', inverse_name='carreras_id', string='Mallas', help='Mallas con las que cuenta la carrera')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")
    
    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

class UPTAMallas(models.Model):
    _name = 'upta.mallas'
    _description = 'Mallas de la UPT Aragua'

    name = fields.Char(string="Nombre", compute="_compute_name", copy=False)
    identificador = fields.Char(string='Identificador', help='Inserte el identificador de la malla a registrar', size=10)
    turno = fields.Selection(string='Turno', selection=[('diurno', 'Diurno'), ('nocturno', 'Nocturno'),])
    carreras_id = fields.Many2one(comodel_name='upta.carreras', string='Carrera', help='Carrera con la que cuenta la malla', store=True)
    trayectos_id = fields.One2many(comodel_name='upta.trayectos', inverse_name='mallas_id', string=' Trayectos', help='Trayectos con las que cuenta la malla')
    materias_id = fields.One2many(comodel_name='upta.materias', inverse_name='mallas_id', string=' Materias', help='Materias con las que cuenta la malla')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")
    
    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

    def _compute_name(self):
        for item in self:
            item.name = "Malla " + item.identificador + " " + item.turno + " " + item.carreras_id.name

class UPTATrayectos(models.Model):
    _name = 'upta.trayectos'
    _description = 'Trayecto de la UPT Aragua'

    name = fields.Char(string="Nombre", compute="_compute_name", copy=False)
    identificador = fields.Char(string='Identificador', help='Inserte el identificador del trayecto a registrar', size=20)
    mallas_id = fields.Many2one(comodel_name='upta.mallas', string='Malla', help='Malla con la que cuenta el trayecto', store=True)
    fases_id = fields.One2many(comodel_name='upta.fases', inverse_name='trayectos_id', string=' Fases', help='Fases con las que cuenta el trayecto')
    materias_id = fields.One2many(comodel_name='upta.materias', inverse_name='trayecto_id', string=' Materias', help='Materias con las que cuenta el trayecto')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

    def _compute_name(self):
        for item in self:
            item.name = "Trayecto " + item.identificador + " " + item.mallas_id.name

class UPTAFases(models.Model):
    _name = 'upta.fases'
    _description = 'Fases de la UPT Aragua'

    name = fields.Char(string="Nombre", compute="_compute_name", copy=False)
    identificador = fields.Char(string='Identificador', help='Inserte el identificador de la fase a registrar', size=10)
    trayectos_id = fields.Many2one(comodel_name='upta.trayectos', string='Trayecto', help='Trayecto con el que cuenta la Fase', store=True)
    materias_id = fields.One2many(comodel_name='upta.materias', inverse_name='fases_id', string=' Materias', help='Materias con las que cuenta la fase')
    status = fields.Selection(string='Estado', selection=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default="activo")

    def status_activate(self):
        self.status = 'activo'

    def status_desactivate(self):
        self.status = 'inactivo'

    def _compute_name(self):
        for item in self:
            item.name = "Fase " + item.identificador + " " + item.trayectos_id.name
