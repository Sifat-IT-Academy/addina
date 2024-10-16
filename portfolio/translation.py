from modeltranslation.translator import register, TranslationOptions
from .models import  Portfolio,PortfolioCategory,Portfolio_details

@register(PortfolioCategory)
class PortfolioCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)

@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'client', 'location',  )

@register(Portfolio_details)
class PortfolioDetailsTranslationOptions(TranslationOptions):
    fields = ("title", "description")
