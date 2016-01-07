__author__ = 'betulyildirim'


from django import forms


class Course(forms.Form):
    c_classroom = forms.CharField(max_length=50)
    c_time = forms.CharField(max_length=50)
   # c_teacher = forms.OneToOneField(Teacher)
    #c_students = forms.ManyToManyField(Student)
    c_code = forms.CharField(max_length=7)


class Student(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(label ='Your e-mail address')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        num_words = len(first_name.split())
        if num_words > 3:
            raise forms.ValidationError("Not a valid name!")
        return first_name


class Teacher(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    office_number = forms.CharField(max_length=7)
    email = forms.EmailField()
    phone = forms.IntegerField()


def f():
    d=["1","2","3"]
    return d