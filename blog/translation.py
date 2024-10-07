from modeltranslation.translator import register, TranslationOptions, translator
from .models import Blog,BlogCategory,BlogComment

@register(Blog)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title','description')

@register(BlogCategory)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name',)
    
@register(BlogComment)
class NewsTranslationOptions(TranslationOptions):
    fields = ('author','body')
# # 2 - usul
# translator.register(Product, NewsTranslationOptions)