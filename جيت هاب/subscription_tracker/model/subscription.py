from odoo import models, fields, api

class ServiceSubscription(models.Model):
    _name = 'service.subscription'
    _description = 'Service Subscription'

    name = fields.Char(string='اسم الخدمة', required=True)
    provider = fields.Char(string='المزود')
    cost = fields.Float(string='التكلفة')
    
    billing_cycle = fields.Selection([
        ('monthly', 'شهري'),
        ('yearly', 'سنوي'),
    ], string='دورة الفوترة', default='monthly')
    
    next_renewal_date = fields.Date(string='تاريخ التجديد')
    
    state = fields.Selection([
        ('active', 'نشط'),
        ('expired', 'منتهي'),
        ('cancelled', 'ملغى'),
    ], string='الحالة', default='active')