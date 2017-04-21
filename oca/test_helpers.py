# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo.tests import common


__all__ = [
    'AbstractModelTestHelper',
]


class AbstractModelTestHelper(common.SavepointCase):

    @classmethod
    def _init_test_model(cls, model_cls):
        """ Build a model from model_cls in order to test abstract models.

        Args:
            model_cls (odoo.models.BaseModel): Class of model to initialize
        Returns:
            model_cls: Instance
        """
        registry = cls.env.registry
        cr = cls.env.cr
        inst = model_cls._build_model(registry, cr)
        model = cls.env[model_cls._name].with_context(todo=[])
        model._prepare_setup()
        model._setup_base(partial=False)
        model._setup_fields(partial=False)
        model._setup_complete()
        model._auto_init()
        model.init()
        model._auto_end()
        return inst

    @classmethod
    def setUpClass(cls):
        super(AbstractModelTestHelper, cls).setUpClass()
        cls.env.registry.enter_test_mode()
        cls._init_test_model(MultiCompanyAbstractTester)

    @classmethod
    def tearDownClass(cls):
        cls.env.registry.leave_test_mode()
        super(AbstractModelTestHelper, cls).tearDownClass()
