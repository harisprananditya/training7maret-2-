# create new object 

from odoo import models

class TrainingModels(models.Model):
	"""docstring for ClassName"""
	_name= 'training.module'
	_description= 'Training Course'
	#create fields
	name= fields.Char(string='Name')
	registration_amount= fields.Float(string='registration_amount')
	date= fields.Date(string='Training Date')
	description= fields.Text(string='description')
	state= fields.Selection([('draft','Draft'),('inprogress', 'In Progress'),('done','Done')], string='Status')
	total_attendees= fields.Integer(string='Total Attendees')
	#many2one field
	trainer_id= fields.Many2one('res.users', string="Trainer")

#create new object.model
class TrainingAttendees(models.Model):
	
	_name= 'training.attendees'
	_description= 'Training Attendees'
	attendee.id= fields.Many2one('res.partner', string ='Attendee')
	presence= fields.Boolean(string='Presence')
	training_id= fields.Many2one('training.module', string='Training')
	#create one2many fields
	attendee_ids= fields.One2many('training.attendees','training id', string='Attendees')
	#many2many field
	assistant_ids= fields.Many2many('res.users', string='Assistant')
	#related fiend on object 
	phone= fields.Char(related='attendee_id.phone', string='Phone')




#Inherit object ( add field ex: 'traininig_ids' many2many fields)

class ResUsers(models.Model):
	_inherit= 'res.users'
	traininig_ids= fields.Many2many(
		'training.module', string = "Training")


