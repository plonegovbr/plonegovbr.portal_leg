import pytest


@pytest.fixture()
def portal_municipal(app):
    return app["plone"]


@pytest.fixture()
def portal_estadual(app):
    return app["estadual"]


@pytest.fixture()
def portal_distrital(app):
    return app["distrital"]


@pytest.fixture()
def portal_federal_dep(app):
    return app["federal_dep"]


@pytest.fixture()
def portal_federal_sen(app):
    return app["federal_sen"]


@pytest.fixture()
def roles_vocabulary(portal, get_vocabulary):
    name = "collective.person.available_roles"
    return get_vocabulary(name, portal)
