from modeltranslation.translator import register, TranslationOptions ,translator
from .models import Portfolio


# translator.register(Portfolio,TranslationOptions)


@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('title','description')
