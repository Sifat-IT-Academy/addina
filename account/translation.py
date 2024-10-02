from modeltranslation.translator import register, TranslationOptions ,translator
from .models import Account


@register(Account)
class AccountTranslationOptions(TranslationOptions):
    fields = ('title','description')
