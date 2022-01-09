from django import forms

class CalcPlusForm(forms.Form):
 # IntefeField数字を扱う専用のフォーム
    val1 = forms.IntegerField()
    val2 = forms.IntegerField()
