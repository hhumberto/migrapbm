from django.shortcuts import render


def index(request):
      return render(request, 'indexnew.html')

#
# Upload registers to FHIR Server
#
