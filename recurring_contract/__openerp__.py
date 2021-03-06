# -*- encoding: utf-8 -*-
##############################################################################
#
#       ______ Releasing children from poverty      _
#      / ____/___  ____ ___  ____  ____ ___________(_)___  ____
#     / /   / __ \/ __ `__ \/ __ \/ __ `/ ___/ ___/ / __ \/ __ \
#    / /___/ /_/ / / / / / / /_/ / /_/ (__  |__  ) / /_/ / / / /
#    \____/\____/_/ /_/ /_/ .___/\__,_/____/____/_/\____/_/ /_/
#                        /_/
#                            in Jesus' name
#
#    Copyright (C) 2014 Compassion CH (http://www.compassion.ch)
#    @author: Cyril Sester <csester@compassion.ch>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Recurring contract',
    'summary': 'Contract for recurring invoicing',
    'version': '1.2',
    'license': 'AGPL-3',
    'author': 'Compassion CH',
    'website': 'http://www.compassion.ch',
    'category': 'Other',
    'depends': ['base', 'sale'],
    'external_dependencies': {},
    'data': [
        'view/contract_group_view.xml',
        'view/recurring_contract_view.xml',
        'view/res_partner_view.xml',
        'view/recurring_invoicer_view.xml',
        'view/recurring_invoicer_wizard_view.xml',
        'workflow/recurring_contract_workflow.xml',
        'data/recurring_contract_sequence.xml',
        'data/recurring_invoicer_sequence.xml',
        'data/contract_expire_cron.xml',
        'data/daily_invoicer_cron.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/contract_demo.xml'
    ],
    'description': '''
        Recurring contracts are made to handle recurring invoice generation.
        Each contract is part of a contract group. This way, only one invoice
        is generated for each group.
    ''',
    'active': False,
    'installable': True,
}
