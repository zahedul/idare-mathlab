from rest_framework.serializers import Serializer, CharField, FileField, BooleanField, IntegerField, ListField

class MatlabSerializer(Serializer):
    uuid = CharField(max_length=200)
    file = FileField()
    has_dependency = BooleanField()
    no_of_dependency = IntegerField()

    def __init__(self, *args, **kwargs):
        super(MatlabSerializer, self).__init__(*args, **kwargs)

        request = kwargs['context']['request']
        no_of_dependency = request.POST.get('no_of_dependency', False)

        if no_of_dependency:
            for i in range(int(no_of_dependency)):
                self.fields['dependency_' + str(i)] = FileField()