from django.forms import ModelForm
from .models import Candidate, Vote, Position


class PositionModelForm(ModelForm):
    class Meta():
        model = Position
        exclude = ['id']

class CandidateModelForm(ModelForm):
    class Meta():
        model = Candidate
        fields = ['firstname','lastname','birthdate','platform']

class VoteModelForm(ModelForm):
    class Meta():
        model = Vote
        exclude = ['id']
