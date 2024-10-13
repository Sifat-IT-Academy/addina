from modeltranslation.translator import register, TranslationOptions, translator 
from .models import Product

@register(Product)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('title','description','main_information','care_info','brand','purchased_place','color','size')