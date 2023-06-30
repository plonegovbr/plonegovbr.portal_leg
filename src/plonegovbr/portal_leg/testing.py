from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.distribution.testing.layer import PloneDistributionFixture
from plone.testing.zope import WSGI_SERVER_FIXTURE

import plonegovbr.portal_leg  # noQA


ANSWERS = {
    "municipal": {
        "site_id": "plone",
        "tipo": "municipal",
        "estado": "SP",
        "title": "Câmara Municipal de Tupilândia",
        "description": "Site da Câmara Municipal de Tupilândia",
        "default_language": "pt-br",
        "portal_timezone": "America/Sao_Paulo",
        "setup_content": True,
    },
    "estadual": {
        "site_id": "estadual",
        "tipo": "estadual",
        "estado": "PR",
        "title": "Assembléia Legislativa do Paraná",
        "description": "Site da Assembléia Legislativa do Paraná",
        "default_language": "pt-br",
        "portal_timezone": "America/Sao_Paulo",
        "setup_content": True,
    },
    "distrital": {
        "site_id": "distrital",
        "tipo": "distrital",
        "estado": "DF",
        "title": "Câmara Legislativa do Distrito Federal",
        "description": "Site da Câmara Legislativa do Distrito Federal",
        "default_language": "pt-br",
        "portal_timezone": "America/Sao_Paulo",
        "setup_content": True,
    },
    "federal_dep": {
        "site_id": "federal_dep",
        "tipo": "federal_dep",
        "estado": "DF",
        "title": "Câmara dos Deputados",
        "description": "Site da Câmara dos Deputados",
        "default_language": "pt-br",
        "portal_timezone": "America/Sao_Paulo",
        "setup_content": True,
    },
    "federal_sen": {
        "site_id": "federal_sen",
        "tipo": "federal_sen",
        "estado": "DF",
        "title": "Senado Federal",
        "description": "Site do Senado Federal",
        "default_language": "pt-br",
        "portal_timezone": "America/Sao_Paulo",
        "setup_content": True,
    },
}


class BaseFixture(PloneDistributionFixture):
    PACKAGE_NAME = "plonegovbr.portal_leg"

    SITES = (
        ("portal_leg", ANSWERS["municipal"]),
        ("portal_leg", ANSWERS["estadual"]),
        ("portal_leg", ANSWERS["distrital"]),
        ("portal_leg", ANSWERS["federal_dep"]),
        ("portal_leg", ANSWERS["federal_sen"]),
    )


BASE_FIXTURE = BaseFixture()


class Layer(PloneSandboxLayer):
    defaultBases = (BASE_FIXTURE,)


FIXTURE = Layer()


INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="PBLegLayer:IntegrationTesting",
)


FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, WSGI_SERVER_FIXTURE),
    name="PBLegLayer:FunctionalTesting",
)
