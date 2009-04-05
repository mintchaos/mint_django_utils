from django import forms
from django.forms.util import ErrorList
    
def clean_unique_for_date(self, field, date_field='pub_date'):
    model = self.Meta.model
    if date_field in self.cleaned_data:
        date = self.cleaned_data[date_field]
        get_args = { field: self.cleaned_data[field],
                     "%s__year" % date_field: date.year,
                     "%s__month" % date_field: date.month,
                     "%s__day" % date_field: date.day }
        try:
            obj = model.objects.get(**get_args)
            if obj.id != self.instance.id:
                msg = u"Please enter a different %s. The one you entered is already being used for %s" % (field, date.strftime("%Y-%m-%d"))
                self._errors[field] = ErrorList([msg])
                del self.cleaned_data[field]
        except model.DoesNotExist:
            pass
    return self.cleaned_data
