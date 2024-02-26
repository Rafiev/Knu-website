from rest_framework import serializers

from applications.information.models import Сompound, News, Image

class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields = '__all__'


class CompoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Сompound
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.position = validated_data.get('position', instance.position)

        instance.save()
        return instance
    

class CompoundListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Сompound
        exclude = ['description']


class NewsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, required=False)


    class Meta:
        model = News
        fields = '__all__'


    def create(self, validated_data):
        request = self.context.get('request')
        new = News.objects.create(**validated_data)
        files = request.FILES
        for image in files.getlist('image'):
            Image.objects.create(news=new, image=image)
        return new
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        images = []
        for i in rep['images']:
            images.append(i['image'])
        rep['images'] = images
        return rep

class NewsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'title', 'created_at']