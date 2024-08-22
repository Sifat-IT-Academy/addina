from modeltranslation.translator import register, TranslationOptions, translator
from .models import Product

# @register(Product)
# class NewsTranslationOptions(TranslationOptions):
#     fields = ('title')

# # 2 - usul
# translator.register(Product, NewsTranslationOptions)