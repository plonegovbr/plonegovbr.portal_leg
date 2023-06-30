from plone import api
from plone.distribution.core import Distribution
from plonegovbr.portal_base.utils.handlers import ajusta_idioma
from plonegovbr.portal_base.utils.handlers import converte_logo_data
from plonegovbr.portal_leg import logger
from plonegovbr.portal_leg import PACKAGE_NAME
from Products.CMFPlone.Portal import PloneSite


def aplica_profile(profile_id: str):
    """Aplica um Generic Setup profile."""
    setup_tool = api.portal.get_tool("portal_setup")
    setup_tool.runAllImportStepsFromProfile(f"profile-{profile_id}")


def post_handler(
    distribution: Distribution, site: PloneSite, answers: dict
) -> PloneSite:
    """Processa o site criado e realiza pequenos ajustes."""
    name = distribution.name
    # Ajusta o idioma para pt-br
    ajusta_idioma(site)
    raw_logo = answers.get("logo")
    if raw_logo:
        logo = converte_logo_data(raw_logo)
        api.portal.set_registry_record("plone.site_logo", logo)
        logger.info(f"{name}: Logo atualizado")
    # Aplica profile especifico para o tipo de site
    tipo = answers.get("tipo")
    profile_id = f"{PACKAGE_NAME}:{tipo}"
    aplica_profile(profile_id)
    # Define contact.default_state
    estado = answers.get("estado")
    api.portal.set_registry_record("contact.default_state", estado)
    logger.info(f"{name}: Definido {estado} como padrão para endereços")
    return site
