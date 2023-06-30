from plone import api
from Products.CMFCore.WorkflowCore import WorkflowException
from zope.component.hooks import setSite

import pytest


TITLE = "Câmara Legislativa do Distrito Federal"


@pytest.fixture()
def portal(portal_distrital):
    """Site é criado pelo arquivo testing.py"""
    setSite(portal_distrital)
    return portal_distrital


class TestPortalLegDistrital:
    @pytest.fixture(autouse=True)
    def _init(self, portal):
        self.portal = portal

    @pytest.mark.parametrize(
        "attr,expected",
        [
            ("title", TITLE),
            ("description", "Site da Câmara Legislativa do Distrito Federal"),
            ("exclude_from_nav", False),
        ],
    )
    def test_plone_site_attributes(self, attr, expected):
        assert getattr(self.portal, attr) == expected

    @pytest.mark.parametrize(
        "package,expected",
        [
            ("plone.app.contenttypes", True),
            ("plone.app.caching", True),
            ("plonetheme.barceloneta", True),
            ("plone.restapi", True),
            ("plone.volto", True),
            ("plonegovbr.portal_base", True),
            ("collective.contact_behaviors", True),
            ("collective.person", True),
        ],
    )
    def test_dependencies_installed(self, installer, package, expected):
        assert installer.is_product_installed(package) is expected

    @pytest.mark.parametrize(
        "path,title,portal_type,review_state",
        [
            ("/", TITLE, "Plone Site", ""),
            ("/informacao", "Informação", "Document", "published"),
            ("/informacao/noticias", "Notícias", "Document", "published"),
            ("/institucional", "Institucional", "Document", "published"),
        ],
    )
    def test_content_created(self, path, title, portal_type, review_state):
        with api.env.adopt_roles(
            [
                "Manager",
            ]
        ):
            content = api.content.get(path=path)
        assert content.title == title
        assert content.portal_type == portal_type
        if review_state:
            assert api.content.get_state(content) == review_state
        else:
            with pytest.raises(WorkflowException) as exc:
                api.content.get_state(content)
            assert "No workflow provides" in str(exc)

    @pytest.mark.parametrize(
        "portal_type,global_allow",
        [
            ("Person", True),
        ],
    )
    def test_types_available(self, get_fti, portal_type, global_allow):
        fti = get_fti(portal_type)
        assert fti.global_allow is global_allow

    @pytest.mark.parametrize(
        "portal_type,allowed",
        [
            ("Person", False),
        ],
    )
    def test_types_in_navigation(self, portal_type, allowed):
        types = api.portal.get_registry_record("plone.displayed_types")
        is_in_navigation = portal_type in types
        assert is_in_navigation is allowed

    @pytest.mark.parametrize(
        "key,expected",
        [
            ["contact.default_state", "DF"],
        ],
    )
    def test_registry_keys(self, key, expected):
        """Test if registry keys are set."""
        value = api.portal.get_registry_record(key, default=None)
        assert value == expected

    @pytest.mark.parametrize(
        "token,title",
        [
            ["deputado", "Deputado(a) Distrital"],
            ["presidente", "Presidente da Câmara"],
        ],
    )
    def test_person_roles_vocabulary(self, roles_vocabulary, token, title):
        """Test if registry keys are set."""
        term = roles_vocabulary.getTerm(token)
        assert title == term.title
